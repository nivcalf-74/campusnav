"""
app.py — CampusNav v2
ממשק משתמש משופר עם כל הפיצ'רים החדשים
"""

import streamlit as st
from campus_nav import (
    load_data, build_graph, find_shortest_path,
    get_node_options, format_time, get_graph_stats,
)

st.set_page_config(
    page_title="CampusNav — מכללת עזריאלי",
    page_icon="🧭",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
  body, [class*="css"], .stMarkdown, .stSelectbox label,
  .stRadio label, p, h1, h2, h3, li {
    direction: rtl !important;
    text-align: right !important;
    font-family: 'Segoe UI', Arial, sans-serif;
  }
  .main-title { text-align: center !important; font-size: 2rem; font-weight: 800; color: #1a1a2e; margin-bottom: 0; }
  .sub-title  { text-align: center !important; color: #555; font-size: 0.95rem; margin-top: 2px; margin-bottom: 24px; }
  .metric-row { display: flex; gap: 12px; margin: 18px 0; direction: rtl; }
  .metric-card {
    flex: 1; background: #f8faff; border: 1.5px solid #dce8ff;
    border-radius: 14px; padding: 16px 10px; text-align: center;
    box-shadow: 0 2px 8px rgba(30,80,180,0.06);
  }
  .metric-icon { font-size: 1.6rem; }
  .metric-val  { font-size: 1.25rem; font-weight: 700; color: #1a3a8f; margin: 4px 0 2px; }
  .metric-lbl  { font-size: 0.78rem; color: #777; }
  .stButton > button {
    background: linear-gradient(135deg, #1a6fe8, #0d4fc4) !important;
    color: white !important; border: none !important; border-radius: 12px !important;
    font-size: 1.05rem !important; font-weight: 700 !important;
    padding: 0.6rem 1.2rem !important;
    box-shadow: 0 3px 12px rgba(26,111,232,0.35) !important;
  }
  .stButton > button:hover {
    background: linear-gradient(135deg, #1560d0, #0a3da0) !important;
    box-shadow: 0 5px 18px rgba(26,111,232,0.45) !important;
  }
  .route-card {
    background: #ffffff; border: 1.5px solid #e8eef8; border-radius: 14px;
    padding: 16px 20px; margin-top: 12px; box-shadow: 0 2px 10px rgba(0,0,0,0.04);
  }
  .step-row {
    display: flex; align-items: flex-start; gap: 12px;
    padding: 10px 0; border-bottom: 1px solid #f0f4ff; direction: rtl;
  }
  .step-row:last-child { border-bottom: none; }
  .step-icon { font-size: 1.3rem; min-width: 28px; }
  .step-text { font-size: 1rem; color: #1a1a2e; line-height: 1.4; direction: rtl; }
  .step-label { font-size: 0.75rem; color: #888; margin-top: 1px; }
  .success-banner {
    background: #e6f9f0; border: 1.5px solid #2db87a; border-radius: 12px;
    padding: 12px 18px; color: #155c3a; font-weight: 600;
    text-align: center !important; margin-bottom: 10px;
  }
  .error-banner {
    background: #fff0f0; border: 1.5px solid #e05050; border-radius: 12px;
    padding: 12px 18px; color: #7a1515; font-weight: 600;
    text-align: center !important; margin-bottom: 10px;
  }
  .route-type-badge {
    display: inline-block; background: #eaf0ff; color: #1a4fc4;
    border-radius: 20px; padding: 3px 14px; font-size: 0.82rem; font-weight: 600; margin-bottom: 10px;
  }
  .section-label { font-size: 0.82rem; color: #888; margin-bottom: 4px; direction: rtl; }
  .spacer { margin: 20px 0; }
</style>
""", unsafe_allow_html=True)


@st.cache_data
def get_data(weight_mode):
    nodes_df, edges_df = load_data()
    G = build_graph(nodes_df, edges_df, weight=weight_mode)
    options = get_node_options(nodes_df)
    return G, options, nodes_df

if "src_key" not in st.session_state:
    st.session_state["src_key"] = None
if "tgt_key" not in st.session_state:
    st.session_state["tgt_key"] = None


# ── כותרת ────────────────────────────────────────────────────────────────────
st.markdown('<div class="main-title">🧭 CampusNav</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">מערכת ניווט חכמה · מכללת עזריאלי ירושלים</div>', unsafe_allow_html=True)
st.markdown('<hr style="margin:10px 0 22px 0; border-color:#e8eef8;">', unsafe_allow_html=True)


# ── הגדרות ───────────────────────────────────────────────────────────────────
col_opt, col_acc = st.columns(2)
with col_opt:
    weight_choice = st.radio("אופטימיזציה לפי:", ["⏱️ זמן הליכה", "📏 מרחק פיזי"], index=0)
with col_acc:
    accessibility = st.radio("סוג מסלול:", ["🚶 מסלול רגיל", "♿ מסלול נגיש"], index=0)

weight_mode = "time" if "זמן" in weight_choice else "distance"
accessible_mode = "♿" in accessibility

G, options, nodes_df = get_data(weight_mode)

st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)


# ── פילטר קומה ───────────────────────────────────────────────────────────────
with st.expander("🔍 סנן לפי קומה (אופציונלי)"):
    floors = sorted(nodes_df["floor"].astype(str).unique())
    selected_floor = st.selectbox("הצג רק צמתים מקומה:", ["הכל"] + floors)

if selected_floor != "הכל":
    filtered_ids = set(nodes_df[nodes_df["floor"].astype(str) == selected_floor]["id"].astype(int))
    options_filtered = {k: v for k, v in options.items() if v in filtered_ids}
else:
    options_filtered = options

options_list = list(options_filtered.keys()) if options_filtered else list(options.keys())


# ── מוצא ויעד ────────────────────────────────────────────────────────────────
default_src = next((k for k in options_list if "שער כניסה למכללה ראשי" in k), options_list[0])
default_tgt = next((k for k in options_list if "ספריה" in k), options_list[-1])

src_key = st.session_state["src_key"] if st.session_state["src_key"] in options_list else default_src
tgt_key = st.session_state["tgt_key"] if st.session_state["tgt_key"] in options_list else default_tgt

st.markdown('<p class="section-label">📍 בחר את המיקום הנוכחי שלך</p>', unsafe_allow_html=True)
source_display = st.selectbox("נקודת מוצא", options_list,
    index=options_list.index(src_key), label_visibility="collapsed", key="source_sel")

c1, c2, c3 = st.columns([3, 2, 3])
with c2:
    if st.button("🔄 החלף", use_container_width=True):
        st.session_state["src_key"] = tgt_key
        st.session_state["tgt_key"] = src_key
        st.rerun()

st.markdown('<p class="section-label">🎯 בחר את היעד שאליו תרצה להגיע</p>', unsafe_allow_html=True)
target_display = st.selectbox("יעד", options_list,
    index=options_list.index(tgt_key), label_visibility="collapsed", key="target_sel")

st.session_state["src_key"] = source_display
st.session_state["tgt_key"] = target_display

source_id = options_filtered.get(source_display) or options.get(source_display)
target_id = options_filtered.get(target_display) or options.get(target_display)

st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)


# ── חישוב ────────────────────────────────────────────────────────────────────
calc = st.button("🔍  חשב מסלול", type="primary", use_container_width=True)

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

    # תגית סוג מסלול
    badge = "♿ מסלול נגיש" if accessible_mode else ("⚡ מסלול מהיר ביותר" if weight_mode == "time" else "📏 מסלול קצר ביותר")
    st.markdown(f'<div style="text-align:center"><span class="route-type-badge">{badge}</span></div>', unsafe_allow_html=True)

    # כרטיסי מדד
    total_min = int(result["total_time"]) // 60
    total_sec = int(result["total_time"]) % 60
    time_str  = f"{total_min}:{total_sec:02d} דק׳" if total_min > 0 else f"{total_sec} שנ׳"

    st.markdown(f"""
    <div class="metric-row">
      <div class="metric-card"><div class="metric-icon">⏱️</div>
        <div class="metric-val">{time_str}</div><div class="metric-lbl">זמן משוער</div></div>
      <div class="metric-card"><div class="metric-icon">📏</div>
        <div class="metric-val">{result["total_dist"]} מ׳</div><div class="metric-lbl">מרחק</div></div>
      <div class="metric-card"><div class="metric-icon">🚩</div>
        <div class="metric-val">{len(result["path"]) - 1}</div><div class="metric-lbl">עצירות</div></div>
    </div>""", unsafe_allow_html=True)

    # מסלול שלב-שלב בניסוח טבעי
    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
    st.markdown("#### 🗺️ המסלול המלא")

    path_names = result["path_names"]
    steps_html = '<div class="route-card">'
    for i, name in enumerate(path_names):
        if i == 0:
            icon, label, verb = "🟢", "התחל כאן", f"<strong>התחל</strong> ב{name}"
        elif i == len(path_names) - 1:
            icon, label, verb = "🔴", "יעד — הגעת! 🎉", f"<strong>הגעת</strong> ל{name}"
        elif i == 1:
            icon, label, verb = "🔵", f"שלב {i}", f"<strong>המשך</strong> אל {name}"
        else:
            icon, label, verb = "🔵", f"שלב {i}", f"<strong>עבור</strong> אל {name}"
        steps_html += f"""
        <div class="step-row">
          <div class="step-icon">{icon}</div>
          <div><div class="step-text">{verb}</div><div class="step-label">{label}</div></div>
        </div>"""
    steps_html += '</div>'
    st.markdown(steps_html, unsafe_allow_html=True)

    if accessible_mode:
        st.info("♿ מצב נגישות פעיל — בגרסה הבאה המסלול יסנן מדרגות אוטומטית.")


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
