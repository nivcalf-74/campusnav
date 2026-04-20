"""
app.py — CampusNav v2
"""
import streamlit as st
import base64, os
from campus_nav import (
    load_data, build_graph, find_shortest_path,
    get_node_options, get_graph_stats,
)

st.set_page_config(
    page_title="CampusNav — מכללת עזריאלי",
    page_icon="🧭",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
  body,[class*="css"],.stMarkdown,.stSelectbox label,.stRadio label,p,h1,h2,h3,li{
    direction:rtl!important;text-align:right!important;
    font-family:'Segoe UI',Arial,sans-serif;
  }
  .main-title{text-align:center!important;font-size:1.9rem;font-weight:800;
    color:#1a1a2e;margin:8px 0 2px;}
  .sub-title{text-align:center!important;color:#666;font-size:.9rem;margin-bottom:18px;}
  .metric-row{display:flex;gap:10px;margin:16px 0;direction:rtl;}
  .metric-card{flex:1;background:#f8faff;border:1.5px solid #dce8ff;
    border-radius:14px;padding:14px 8px;text-align:center;
    box-shadow:0 2px 8px rgba(30,80,180,.06);}
  .metric-icon{font-size:1.5rem;}
  .metric-val{font-size:1.2rem;font-weight:700;color:#1a3a8f;margin:3px 0 2px;}
  .metric-lbl{font-size:.75rem;color:#888;}
  /* כפתור חשב — כחול */
  div[data-testid="stButton"] button{
    background:linear-gradient(135deg,#1a6fe8,#0d4fc4)!important;
    color:#fff!important;border:none!important;border-radius:12px!important;
    font-size:1.05rem!important;font-weight:700!important;
    box-shadow:0 3px 12px rgba(26,111,232,.35)!important;
  }
  div[data-testid="stButton"] button:hover{
    background:linear-gradient(135deg,#1560d0,#0a3da0)!important;
  }
  .route-card{background:#fff;border:1.5px solid #e8eef8;border-radius:14px;
    padding:14px 18px;margin-top:10px;box-shadow:0 2px 10px rgba(0,0,0,.04);}
  .step-row{display:flex;align-items:flex-start;gap:10px;
    padding:9px 0;border-bottom:1px solid #f0f4ff;direction:rtl;}
  .step-row:last-child{border-bottom:none;}
  .step-icon{font-size:1.25rem;min-width:26px;}
  .step-name{font-size:1rem;color:#1a1a2e;font-weight:600;}
  .step-instruction{font-size:.82rem;color:#1a6fe8;margin-top:2px;font-weight:500;}
  .step-label{font-size:.72rem;color:#aaa;margin-top:1px;}
  .success-banner{background:#e6f9f0;border:1.5px solid #2db87a;border-radius:12px;
    padding:11px 16px;color:#155c3a;font-weight:600;
    text-align:center!important;margin-bottom:10px;}
  .error-banner{background:#fff0f0;border:1.5px solid #e05050;border-radius:12px;
    padding:11px 16px;color:#7a1515;font-weight:600;
    text-align:center!important;margin-bottom:10px;}
  .route-badge{display:inline-block;background:#eaf0ff;color:#1a4fc4;
    border-radius:20px;padding:3px 14px;font-size:.82rem;font-weight:600;margin:6px 0 10px;}
  .field-label{font-size:.82rem;color:#666;margin-bottom:4px;}
  .spacer{margin:18px 0;}
  .logo-wrap{display:flex;justify-content:center;margin-bottom:8px;}
</style>
""", unsafe_allow_html=True)


# ── לוגו ────────────────────────────────────────────────────────────────────
logo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "azrieli_logo.png")
if os.path.exists(logo_path):
    with open(logo_path, "rb") as f:
        logo_b64 = base64.b64encode(f.read()).decode()
    st.markdown(
        f'<div class="logo-wrap"><img src="data:image/png;base64,{logo_b64}" height="70"/></div>',
        unsafe_allow_html=True
    )

st.markdown('<div class="main-title">🧭 CampusNav</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">מערכת ניווט חכמה · מכללת עזריאלי ירושלים</div>', unsafe_allow_html=True)
st.markdown('<hr style="margin:8px 0 20px;border-color:#e8eef8;">', unsafe_allow_html=True)


# ── טעינת נתונים ─────────────────────────────────────────────────────────────
@st.cache_data
def get_data(weight_mode):
    nodes_df, edges_df = load_data()
    G = build_graph(nodes_df, edges_df, weight=weight_mode)
    options = get_node_options(nodes_df)
    return G, options, nodes_df, edges_df


# ── אופטימיזציה ──────────────────────────────────────────────────────────────
weight_choice = st.radio(
    "אופטימיזציה לפי:",
    ["⏱️ זמן הליכה", "📏 מרחק פיזי"],
    horizontal=True, index=0
)
weight_mode = "time" if "זמן" in weight_choice else "distance"
G, options, nodes_df, edges_df = get_data(weight_mode)

st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)


# ── פילטר קומה ───────────────────────────────────────────────────────────────
with st.expander("🔍 סנן לפי קומה (אופציונלי)"):
    floors = sorted(nodes_df["floor"].astype(str).unique())
    sel_floor = st.selectbox("הצג רק צמתים מקומה:", ["הכל"] + floors)

if sel_floor != "הכל":
    fids = set(nodes_df[nodes_df["floor"].astype(str) == sel_floor]["id"].astype(int))
    opts = {k: v for k, v in options.items() if v in fids}
else:
    opts = options

opts_list = list(opts.keys())


# ── מוצא ויעד + כפתור החלפה ─────────────────────────────────────────────────
# הגדרת ברירות מחדל
default_src = next((k for k in opts_list if "שער כניסה למכללה ראשי" in k), opts_list[0])
default_tgt = next((k for k in opts_list if "ספריה" in k), opts_list[-1])

# אתחול session state — רק בפעם הראשונה
if "source_sel" not in st.session_state:
    st.session_state["source_sel"] = default_src
if "target_sel" not in st.session_state:
    st.session_state["target_sel"] = default_tgt

# ודא שהערכים קיימים ברשימה הנוכחית
if st.session_state["source_sel"] not in opts_list:
    st.session_state["source_sel"] = default_src
if st.session_state["target_sel"] not in opts_list:
    st.session_state["target_sel"] = default_tgt

st.markdown('<p class="field-label">📍 בחר את המיקום הנוכחי שלך</p>', unsafe_allow_html=True)
source_display = st.selectbox(
    "מוצא", opts_list,
    index=opts_list.index(st.session_state["source_sel"]),
    label_visibility="collapsed"
)

# ── כפתור החלפה ──
_, mid, _ = st.columns([3, 2, 3])
with mid:
    if st.button("🔄 החלף", use_container_width=True):
        # מחליפים ישירות בין הערכים השמורים
        src_tmp = source_display
        tgt_tmp = st.session_state["target_sel"]
        st.session_state["source_sel"] = tgt_tmp
        st.session_state["target_sel"] = src_tmp
        st.rerun()

# שמור בחירת מוצא עדכנית
st.session_state["source_sel"] = source_display

st.markdown('<p class="field-label">🎯 בחר את היעד שאליו תרצה להגיע</p>', unsafe_allow_html=True)
target_display = st.selectbox(
    "יעד", opts_list,
    index=opts_list.index(st.session_state["target_sel"]),
    label_visibility="collapsed"
)
st.session_state["target_sel"] = target_display

source_id = opts.get(source_display) or options.get(source_display)
target_id = opts.get(target_display) or options.get(target_display)

st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)


# ── כפתור חישוב ──────────────────────────────────────────────────────────────
calc = st.button("🔍  חשב מסלול", type="primary", use_container_width=True)


# ── תוצאה ────────────────────────────────────────────────────────────────────
if calc:
    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

    if source_id == target_id:
        st.markdown('<div class="success-banner">📍 אתה כבר נמצא ביעד!</div>', unsafe_allow_html=True)
        st.stop()

    result = find_shortest_path(G, source_id, target_id, weight=weight_mode)

    if not result["found"]:
        st.markdown(
            '<div class="error-banner">❌ לא נמצא מסלול בין הנקודות הנבחרות.<br>'
            'ייתכן שאחד הצמתים עדיין מנותק מהגרף.</div>',
            unsafe_allow_html=True
        )
        st.stop()

    # הודעת הצלחה
    st.markdown('<div class="success-banner">✅ המסלול חושב בהצלחה!</div>', unsafe_allow_html=True)

    # תגית
    badge = "⚡ מסלול מהיר ביותר" if weight_mode == "time" else "📏 מסלול קצר ביותר"
    st.markdown(f'<div style="text-align:center"><span class="route-badge">{badge}</span></div>',
                unsafe_allow_html=True)

    # כרטיסי מדד
    total_sec = int(result["total_time"])
    m, s = total_sec // 60, total_sec % 60
    time_str = f"{m}:{s:02d} דק׳" if m > 0 else f"{s} שנ׳"

    st.markdown(f"""
    <div class="metric-row">
      <div class="metric-card">
        <div class="metric-icon">⏱️</div>
        <div class="metric-val">{time_str}</div>
        <div class="metric-lbl">זמן משוער</div>
      </div>
      <div class="metric-card">
        <div class="metric-icon">📏</div>
        <div class="metric-val">{result["total_dist"]} מ׳</div>
        <div class="metric-lbl">מרחק</div>
      </div>
      <div class="metric-card">
        <div class="metric-icon">🚩</div>
        <div class="metric-val">{len(result["path"]) - 1}</div>
        <div class="metric-lbl">עצירות</div>
      </div>
    </div>""", unsafe_allow_html=True)

    # ── מסלול שלב-שלב עם הוראות ──
    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
    st.markdown("#### 🗺️ המסלול המלא")

    path     = result["path"]
    path_names = result["path_names"]

    # בניית מילון הוראות לפי קשתות
    instr_map = {}
    for _, row in edges_df.iterrows():
        instr_map[(int(row["source"]), int(row["target"]))] = row.get("instruction", "המשך ישר")
        instr_map[(int(row["target"]), int(row["source"]))] = row.get("instruction", "המשך ישר")

    steps_html = '<div class="route-card">'
    for i, (node_id, name) in enumerate(zip(path, path_names)):
        if i == 0:
            icon  = "🟢"
            label = "נקודת מוצא"
            verb  = f"התחל ב<strong>{name}</strong>"
            instr = ""
        elif i == len(path) - 1:
            icon  = "🔴"
            label = "יעד"
            verb  = f"הגעת ל<strong>{name}</strong> 🎉"
            instr = ""
        else:
            icon  = "🔵"
            label = f"שלב {i}"
            prev_id = path[i - 1]
            instr = instr_map.get((prev_id, node_id), "המשך ישר")
            verb  = f"<strong>{name}</strong>"

        instr_html = f'<div class="step-instruction">↩ {instr}</div>' if instr else ""

        steps_html += f"""
        <div class="step-row">
          <div class="step-icon">{icon}</div>
          <div>
            <div class="step-name">{verb}</div>
            {instr_html}
            <div class="step-label">{label}</div>
          </div>
        </div>"""

    steps_html += '</div>'
    st.markdown(steps_html, unsafe_allow_html=True)


# ── פאנל גרף ─────────────────────────────────────────────────────────────────
st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
with st.expander("📊 מידע על הגרף"):
    stats = get_graph_stats(G)
    c1, c2, c3 = st.columns(3)
    c1.metric("צמתים", stats["nodes"])
    c2.metric("קשתות", stats["edges"])
    c3.metric("מחובר?", "✓ כן" if stats["connected"] else "✗ חלקי")
    if not stats["connected"]:
        st.warning("⚠️ מעלית ופינת ישיבה מרכזית עדיין מנותקים — יש להוסיף קשתות ב-edges.csv")

st.markdown("---")
st.caption("CampusNav v2 · מכללת עזריאלי · אלגוריתם דייקסטרה · פרויקט חקר ביצועים 2")
