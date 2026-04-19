"""
app.py
------
ממשק משתמש של CampusNav — מבוסס Streamlit.
הפעלה:  streamlit run app.py
"""

import streamlit as st
from campus_nav import (
    load_data,
    build_graph,
    find_shortest_path,
    get_node_options,
    format_time,
    get_graph_stats,
)

# ──────────────────────────────────────────────
# הגדרות עמוד
# ──────────────────────────────────────────────

st.set_page_config(
    page_title="CampusNav — מכללת עזריאלי",
    page_icon="🧭",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# CSS בסיסי — כיוון RTL וסגנון עברי
st.markdown("""
<style>
    body, [class*="css"] { direction: rtl; text-align: right; }
    .stSelectbox label, .stRadio label { font-weight: 600; }
    .result-box {
        background: #f0f7ff;
        border-right: 5px solid #1976D2;
        border-radius: 8px;
        padding: 16px 20px;
        margin: 12px 0;
    }
    .step-item {
        padding: 6px 0;
        border-bottom: 1px solid #e0e0e0;
        font-size: 1rem;
    }
    .step-item:last-child { border-bottom: none; }
    .warn-box {
        background: #fff8e1;
        border-right: 5px solid #FFA000;
        border-radius: 8px;
        padding: 12px 16px;
        margin: 8px 0;
    }
</style>
""", unsafe_allow_html=True)


# ──────────────────────────────────────────────
# טעינת נתונים (cache — נטען פעם אחת)
# ──────────────────────────────────────────────

@st.cache_data
def get_graph_data(weight_mode):
    nodes_df, edges_df = load_data()
    G = build_graph(nodes_df, edges_df, weight=weight_mode)
    options = get_node_options(nodes_df)
    return G, options


# ──────────────────────────────────────────────
# כותרת ראשית
# ──────────────────────────────────────────────

st.title("🧭 CampusNav")
st.subheader("מערכת ניווט חכמה — מכללת עזריאלי")
st.markdown("---")


# ──────────────────────────────────────────────
# בחירת מצב משקל
# ──────────────────────────────────────────────

weight_choice = st.radio(
    "אופטימיזציה לפי:",
    options=["זמן הליכה ⏱️", "מרחק פיזי 📏"],
    horizontal=True,
    index=0
)
weight_mode = "time" if "זמן" in weight_choice else "distance"

G, options = get_graph_data(weight_mode)

# ──────────────────────────────────────────────
# בחירת נקודת מוצא ויעד
# ──────────────────────────────────────────────

st.markdown("### 📍 נקודת מוצא")
source_display = st.selectbox(
    "מאיפה אתה מתחיל?",
    options=list(options.keys()),
    index=list(options.keys()).index(
        [k for k in options if "שער כניסה למכללה ראשי" in k][0]
    ),
    label_visibility="collapsed"
)

st.markdown("### 🎯 יעד")
target_display = st.selectbox(
    "לאן אתה רוצה להגיע?",
    options=list(options.keys()),
    index=list(options.keys()).index(
        [k for k in options if "ספריה" in k][0]
    ),
    label_visibility="collapsed"
)

source_id = options[source_display]
target_id = options[target_display]

# ──────────────────────────────────────────────
# כפתור חישוב
# ──────────────────────────────────────────────

st.markdown("")
calc_btn = st.button("🔍 חשב מסלול", type="primary", use_container_width=True)

# ──────────────────────────────────────────────
# הצגת תוצאה
# ──────────────────────────────────────────────

if calc_btn:
    if source_id == target_id:
        st.info("נקודת המוצא והיעד זהות — כבר שם! 😄")
    else:
        result = find_shortest_path(G, source_id, target_id, weight=weight_mode)

        if not result["found"]:
            st.error(f"❌ {result['error']}")
        else:
            # סיכום עליון
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("⏱️ זמן משוער", format_time(result["total_time"]))
            with col2:
                st.metric("📏 מרחק", f"{result['total_dist']} מ׳")
            with col3:
                st.metric("🚩 עצירות", len(result["path"]) - 1)

            st.markdown("---")

            # מסלול שלב-שלב
            st.markdown("### 🗺️ המסלול המלא")
            path_names = result["path_names"]

            for i, name in enumerate(path_names):
                if i == 0:
                    icon = "🟢"
                    label = "התחלה"
                elif i == len(path_names) - 1:
                    icon = "🔴"
                    label = "יעד"
                else:
                    icon = "🔵"
                    label = f"שלב {i}"

                st.markdown(
                    f'<div class="step-item">{icon} <strong>{label}</strong> — {name}</div>',
                    unsafe_allow_html=True
                )

            st.markdown("")

            # אזהרות על צמתים מנותקים (TODO)
            disconnected_in_path = [
                n for n in result["path"]
                if n in (4, 5)  # מעלית ופינת ישיבה — עדיין TODO
            ]
            if disconnected_in_path:
                st.markdown(
                    '<div class="warn-box">⚠️ המסלול עובר דרך צמתים שנתוניהם עדיין חסרים (מעלית / פינת ישיבה). המשקלים יעודכנו בקרוב.</div>',
                    unsafe_allow_html=True
                )

# ──────────────────────────────────────────────
# פאנל מידע על הגרף (מכווץ)
# ──────────────────────────────────────────────

with st.expander("📊 מידע על הגרף"):
    stats = get_graph_stats(G)
    c1, c2, c3 = st.columns(3)
    c1.metric("צמתים", stats["nodes"])
    c2.metric("קשתות", stats["edges"])
    c3.metric("מחובר?", "✓ כן" if stats["connected"] else "✗ חלקי")

    if not stats["connected"]:
        st.warning(
            "הגרף אינו מחובר לחלוטין. "
            "הצמתים הבאים מנותקים: **מעלית** (Node 4), **פינת ישיבה מרכזית** (Node 5). "
            "יש להוסיף קשתות חסרות ב-edges.csv."
        )

# ──────────────────────────────────────────────
# Footer
# ──────────────────────────────────────────────

st.markdown("---")
st.caption("CampusNav · מכללת עזריאלי · אלגוריתם דייקסטרה · פרויקט חקר ביצועים 2")
