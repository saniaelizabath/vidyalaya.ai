# import streamlit as st
# import json
# import html
# from datetime import datetime, date
# import random

# # ── Page config (must be first) ─────────────────────────────────────────────
# st.set_page_config(
#     page_title="Vidyalaya AI — Multigrade Teaching Assistant",
#     page_icon="🪔",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# from hardcoded_data import (
#     NCERT_CURRICULUM,
#     HARDCODED_COURSE_PLANS,
#     HARDCODED_ACTIVITIES,
#     HARDCODED_WORKSHEETS,
#     HARDCODED_ASSESSMENTS,
#     HARDCODED_VISUAL_AIDS,
#     HARDCODED_PEER_ACTIVITIES,
#     STUDENT_DATA,
#     WEEKLY_SUMMARY,
# )

# # ── Global CSS ───────────────────────────────────────────────────────────────
# def inject_css():
#     st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800&family=DM+Sans:wght@300;400;500;600&family=DM+Mono:wght@400;500&display=swap');

# /* ── Reset & Base ── */
# *, *::before, *::after { box-sizing: border-box; }
# html, body, [data-testid="stAppViewContainer"] {
#     background: #0f1117 !important;
#     color: #e8eaf0 !important;
#     font-family: 'DM Sans', sans-serif;
# }
# [data-testid="stSidebar"] { background: #13151f !important; border-right: 1px solid rgba(255,255,255,.07) !important; }
# .block-container { padding: 1.5rem 2rem 3rem !important; max-width: 1320px !important; }

# /* ── Hide default Streamlit decoration ── */
# #MainMenu, footer, header { visibility: hidden; }
# [data-testid="stDecoration"] { display: none; }
# .stDeployButton { display: none; }

# /* ── Typography ── */
# h1 { font-family: 'Playfair Display', serif !important; font-weight: 800 !important; font-size: 2.1rem !important; letter-spacing: -0.5px; line-height: 1.1; }
# h2 { font-family: 'Playfair Display', serif !important; font-weight: 700 !important; font-size: 1.55rem !important; }
# h3 { font-family: 'DM Sans', sans-serif !important; font-weight: 600 !important; font-size: 1.1rem !important; letter-spacing: .1px; }
# code, pre { font-family: 'DM Mono', monospace !important; }

# /* ── Sidebar ── */
# .sidebar-logo {
#     font-family: 'Playfair Display', serif;
#     font-size: 1.35rem;
#     font-weight: 800;
#     color: #f5c842;
#     letter-spacing: -0.5px;
#     padding: 0.25rem 0 0.75rem 0;
#     border-bottom: 1px solid rgba(245,200,66,.2);
#     margin-bottom: 1rem;
# }
# .sidebar-logo span { color: #e8eaf0; font-weight: 300; font-family: 'DM Sans',sans-serif; font-size: .85rem; display:block; margin-top:2px; letter-spacing:.5px; }

# /* ── Nav buttons in sidebar ── */
# div[data-testid="stRadio"] > label { display:none; }
# div[data-testid="stRadio"] > div { gap: 4px !important; }
# div[data-testid="stRadio"] > div > label {
#     display: flex !important;
#     align-items: center !important;
#     gap: 10px !important;
#     padding: 10px 14px !important;
#     border-radius: 10px !important;
#     border: 1px solid transparent !important;
#     cursor: pointer !important;
#     transition: all .18s ease !important;
#     font-size: .95rem !important;
#     font-weight: 500 !important;
#     color: rgba(232,234,240,.75) !important;
#     background: transparent !important;
#     width: 100% !important;
# }
# div[data-testid="stRadio"] > div > label:hover {
#     background: rgba(245,200,66,.07) !important;
#     border-color: rgba(245,200,66,.15) !important;
#     color: #f5c842 !important;
# }
# div[data-testid="stRadio"] > div > label[data-checked="true"],
# div[data-testid="stRadio"] > div > label[aria-checked="true"] {
#     background: rgba(245,200,66,.12) !important;
#     border-color: rgba(245,200,66,.35) !important;
#     color: #f5c842 !important;
#     font-weight: 600 !important;
# }

# /* ── Buttons ── */
# .stButton > button {
#     background: linear-gradient(135deg, #f5c842 0%, #e8a21a 100%) !important;
#     color: #0f1117 !important;
#     font-family: 'DM Sans', sans-serif !important;
#     font-weight: 600 !important;
#     font-size: .95rem !important;
#     border: none !important;
#     border-radius: 10px !important;
#     padding: 0.55rem 1.4rem !important;
#     cursor: pointer !important;
#     transition: all .18s ease !important;
#     box-shadow: 0 4px 14px rgba(245,200,66,.25) !important;
# }
# .stButton > button:hover {
#     transform: translateY(-1px) !important;
#     box-shadow: 0 6px 20px rgba(245,200,66,.35) !important;
# }
# .stButton > button[kind="secondary"] {
#     background: rgba(255,255,255,.06) !important;
#     color: #e8eaf0 !important;
#     border: 1px solid rgba(255,255,255,.12) !important;
#     box-shadow: none !important;
# }

# /* ── Inputs ── */
# .stTextInput > div > div > input,
# .stTextArea > div > div > textarea,
# .stSelectbox > div > div {
#     background: rgba(255,255,255,.05) !important;
#     border: 1px solid rgba(255,255,255,.12) !important;
#     border-radius: 10px !important;
#     color: #e8eaf0 !important;
#     font-family: 'DM Sans', sans-serif !important;
# }
# .stTextInput > div > div > input:focus,
# .stTextArea > div > div > textarea:focus {
#     border-color: rgba(245,200,66,.5) !important;
#     box-shadow: 0 0 0 3px rgba(245,200,66,.1) !important;
# }

# /* ── Multiselect ── */
# .stMultiSelect > div > div {
#     background: rgba(255,255,255,.05) !important;
#     border: 1px solid rgba(255,255,255,.12) !important;
#     border-radius: 10px !important;
# }

# /* ── Sliders ── */
# .stSlider > div > div > div { background: rgba(245,200,66,.3) !important; }
# .stSlider > div > div > div > div { background: #f5c842 !important; }

# /* ── Expanders ── */
# .stExpander { border: 1px solid rgba(255,255,255,.08) !important; border-radius: 12px !important; background: rgba(255,255,255,.02) !important; margin-bottom: 6px !important; }
# .stExpander > div:first-child { border-radius: 12px !important; padding: 10px 14px !important; }
# .stExpander > div:first-child:hover { background: rgba(255,255,255,.04) !important; }
# .stExpander summary { font-weight: 500 !important; }

# /* ── Tabs ── */
# .stTabs [data-baseweb="tab-list"] {
#     gap: 4px !important;
#     background: rgba(255,255,255,.03) !important;
#     border-radius: 12px !important;
#     padding: 4px !important;
#     border: 1px solid rgba(255,255,255,.07) !important;
# }
# .stTabs [data-baseweb="tab"] {
#     border-radius: 9px !important;
#     padding: 7px 14px !important;
#     font-family: 'DM Sans', sans-serif !important;
#     font-weight: 500 !important;
#     font-size: .9rem !important;
#     color: rgba(232,234,240,.65) !important;
#     border: none !important;
#     background: transparent !important;
#     transition: all .15s !important;
# }
# .stTabs [aria-selected="true"] {
#     background: rgba(245,200,66,.15) !important;
#     color: #f5c842 !important;
#     font-weight: 600 !important;
# }

# /* ── Metrics / KPI cards ── */
# [data-testid="stMetric"] {
#     background: rgba(255,255,255,.04) !important;
#     border: 1px solid rgba(255,255,255,.09) !important;
#     border-radius: 14px !important;
#     padding: 14px 16px !important;
# }
# [data-testid="stMetricValue"] { font-size: 1.6rem !important; font-weight: 700 !important; color: #f5c842 !important; }
# [data-testid="stMetricLabel"] { font-size: .8rem !important; opacity: .7 !important; text-transform: uppercase !important; letter-spacing: .08em !important; }

# /* ── Alert/Info boxes ── */
# .stAlert { border-radius: 12px !important; }
# .stInfo { background: rgba(59,130,246,.12) !important; border: 1px solid rgba(59,130,246,.25) !important; }
# .stSuccess { background: rgba(16,185,129,.12) !important; border: 1px solid rgba(16,185,129,.25) !important; }
# .stWarning { background: rgba(245,158,11,.12) !important; border: 1px solid rgba(245,158,11,.25) !important; }

# /* ── Divider ── */
# hr { border-color: rgba(255,255,255,.07) !important; margin: 1.2rem 0 !important; }

# /* ── Dataframes ── */
# [data-testid="stDataFrame"] { border-radius: 12px !important; overflow: hidden !important; }

# /* ── Progress bar ── */
# .stProgress > div > div > div { background: linear-gradient(90deg, #f5c842, #e8a21a) !important; border-radius: 99px !important; }
# .stProgress > div > div { background: rgba(255,255,255,.08) !important; border-radius: 99px !important; }

# /* ── Custom component classes ── */
# .vd-hero {
#     background: linear-gradient(135deg, rgba(245,200,66,.08) 0%, rgba(232,162,26,.04) 50%, rgba(15,17,23,0) 100%);
#     border: 1px solid rgba(245,200,66,.15);
#     border-radius: 20px;
#     padding: 28px 32px;
#     margin-bottom: 24px;
#     position: relative;
#     overflow: hidden;
# }
# .vd-hero::before {
#     content: '';
#     position: absolute;
#     top: -60px; right: -60px;
#     width: 240px; height: 240px;
#     background: radial-gradient(circle, rgba(245,200,66,.12), transparent 70%);
#     pointer-events: none;
# }
# .vd-hero-title { font-family: 'Playfair Display', serif; font-size: 1.7rem; font-weight: 800; color: #f5c842; margin: 0 0 6px 0; line-height: 1.15; }
# .vd-hero-sub { color: rgba(232,234,240,.7); font-size: .98rem; margin: 0 0 18px 0; }
# .vd-kpis { display: flex; gap: 12px; flex-wrap: wrap; }
# .vd-kpi {
#     background: rgba(0,0,0,.25);
#     border: 1px solid rgba(255,255,255,.10);
#     border-radius: 12px;
#     padding: 10px 16px;
#     min-width: 130px;
# }
# .vd-kpi-label { font-size: .68rem; letter-spacing: .12em; text-transform: uppercase; color: rgba(232,234,240,.55); margin-bottom: 3px; }
# .vd-kpi-value { font-size: 1.05rem; font-weight: 700; color: #e8eaf0; }

# .vd-card {
#     background: rgba(255,255,255,.03);
#     border: 1px solid rgba(255,255,255,.09);
#     border-radius: 16px;
#     padding: 18px 20px;
#     margin-bottom: 12px;
#     transition: border-color .18s;
# }
# .vd-card:hover { border-color: rgba(245,200,66,.2); }
# .vd-card-title { font-size: 1.02rem; font-weight: 600; margin: 0 0 6px 0; }
# .vd-card-meta { font-size: .85rem; color: rgba(232,234,240,.6); }

# .vd-badge {
#     display: inline-flex;
#     align-items: center;
#     padding: 3px 11px;
#     border-radius: 999px;
#     font-size: .80rem;
#     font-weight: 600;
#     margin-right: 6px;
#     margin-bottom: 4px;
# }
# .vd-section-label {
#     font-size: .72rem;
#     font-weight: 600;
#     letter-spacing: .12em;
#     text-transform: uppercase;
#     color: rgba(232,234,240,.5);
#     margin-bottom: 10px;
#     padding-left: 2px;
# }
# .vd-timeline-row {
#     display: flex;
#     gap: 0;
#     border-radius: 12px;
#     overflow: hidden;
#     margin-bottom: 8px;
#     border: 1px solid rgba(255,255,255,.07);
# }
# .vd-timeline-time {
#     background: rgba(245,200,66,.1);
#     border-right: 1px solid rgba(245,200,66,.2);
#     color: #f5c842;
#     font-size: .82rem;
#     font-weight: 600;
#     font-family: 'DM Mono', monospace;
#     padding: 10px 12px;
#     min-width: 90px;
#     display: flex;
#     align-items: center;
# }
# .vd-timeline-content {
#     padding: 10px 14px;
#     flex: 1;
#     background: rgba(255,255,255,.025);
# }
# .vd-timeline-activity { font-weight: 600; font-size: .92rem; margin-bottom: 4px; }
# .vd-timeline-sub { font-size: .82rem; color: rgba(232,234,240,.65); }

# .vd-grade-band {
#     border-radius: 14px;
#     padding: 14px 16px;
#     margin-bottom: 10px;
#     border-left: 4px solid;
# }
# .g1 { background: rgba(16,185,129,.07); border-color: #10b981; }
# .g2 { background: rgba(59,130,246,.07); border-color: #3b82f6; }
# .g3 { background: rgba(245,158,11,.07); border-color: #f59e0b; }
# .g4 { background: rgba(239,68,68,.07); border-color: #ef4444; }

# .vd-q-card {
#     background: rgba(255,255,255,.03);
#     border: 1px solid rgba(255,255,255,.09);
#     border-radius: 12px;
#     padding: 14px 16px;
#     margin-bottom: 8px;
# }
# .vd-q-number {
#     display: inline-flex;
#     align-items: center;
#     justify-content: center;
#     width: 26px; height: 26px;
#     background: rgba(245,200,66,.15);
#     border-radius: 50%;
#     font-size: .78rem;
#     font-weight: 700;
#     color: #f5c842;
#     margin-right: 10px;
#     flex-shrink: 0;
# }
# .vd-rubric-row { display: grid; grid-template-columns: 1.5fr 1fr 1fr 1fr 1fr; gap: 6px; margin-bottom: 6px; }
# .vd-rubric-cell { background: rgba(255,255,255,.04); border-radius: 8px; padding: 8px 10px; font-size: .82rem; }
# .vd-rubric-header { font-weight: 700; font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; }
# .vd-rubric-exc { background: rgba(16,185,129,.12) !important; }
# .vd-rubric-gd { background: rgba(59,130,246,.10) !important; }
# .vd-rubric-sat { background: rgba(245,158,11,.10) !important; }
# .vd-rubric-ni { background: rgba(239,68,68,.10) !important; }

# .vd-progress-outer {
#     background: rgba(255,255,255,.08);
#     border-radius: 99px;
#     height: 8px;
#     margin-top: 4px;
#     overflow: hidden;
# }
# .vd-progress-inner {
#     height: 100%;
#     border-radius: 99px;
#     background: linear-gradient(90deg, #f5c842, #e8a21a);
#     transition: width .5s ease;
# }
# .vd-topic-pill {
#     display: inline-flex;
#     align-items: center;
#     gap: 5px;
#     padding: 4px 10px;
#     border-radius: 8px;
#     font-size: .80rem;
#     font-weight: 500;
#     margin: 2px;
# }
# .pill-done { background: rgba(16,185,129,.15); color: #10b981; border: 1px solid rgba(16,185,129,.25); }
# .pill-pending { background: rgba(239,68,68,.10); color: rgba(239,68,68,.85); border: 1px solid rgba(239,68,68,.2); }

# .vd-student-card {
#     background: rgba(255,255,255,.03);
#     border: 1px solid rgba(255,255,255,.09);
#     border-radius: 14px;
#     padding: 14px 16px;
#     display: flex;
#     align-items: center;
#     gap: 12px;
#     cursor: pointer;
#     transition: all .15s;
# }
# .vd-student-card:hover { border-color: rgba(245,200,66,.25); background: rgba(245,200,66,.04); }
# .vd-avatar { font-size: 1.8rem; width: 44px; height: 44px; display:flex; align-items:center; justify-content:center; }
# .vd-student-name { font-weight: 600; font-size: .95rem; }
# .vd-student-meta { font-size: .80rem; color: rgba(232,234,240,.55); }

# .vd-log-row {
#     display: grid;
#     grid-template-columns: 90px 90px 1fr auto;
#     align-items: center;
#     gap: 12px;
#     padding: 10px 14px;
#     border-radius: 10px;
#     background: rgba(255,255,255,.025);
#     border: 1px solid rgba(255,255,255,.07);
#     margin-bottom: 6px;
#     font-size: .88rem;
# }
# .vd-log-date { font-family: 'DM Mono', monospace; color: rgba(232,234,240,.55); font-size: .80rem; }
# .vd-log-subject { }
# .vd-log-topic { color: rgba(232,234,240,.75); }
# .vd-log-completion { font-weight: 700; color: #10b981; font-size: .88rem; }

# .vd-week-card {
#     background: rgba(255,255,255,.025);
#     border: 1px solid rgba(255,255,255,.08);
#     border-radius: 14px;
#     padding: 14px 16px;
#     margin-bottom: 8px;
# }
# .vd-highlight-item { display: flex; gap: 8px; align-items: flex-start; margin-bottom: 6px; font-size: .90rem; }
# .vd-dot-green { width: 8px; height: 8px; border-radius: 50%; background: #10b981; margin-top: 5px; flex-shrink: 0; }
# .vd-dot-amber { width: 8px; height: 8px; border-radius: 50%; background: #f59e0b; margin-top: 5px; flex-shrink: 0; }
# .vd-dot-blue { width: 8px; height: 8px; border-radius: 50%; background: #3b82f6; margin-top: 5px; flex-shrink: 0; }

# .vd-gantt-row { display: flex; align-items: center; gap: 8px; margin-bottom: 6px; }
# .vd-gantt-label { width: 80px; font-size: .78rem; color: rgba(232,234,240,.65); text-align: right; flex-shrink: 0; }
# .vd-gantt-bar-wrap { flex: 1; height: 24px; background: rgba(255,255,255,.05); border-radius: 6px; overflow: hidden; }
# .vd-gantt-bar { height: 100%; border-radius: 6px; display: flex; align-items: center; padding-left: 8px; font-size: .75rem; font-weight: 600; color: #0f1117; }
# </style>
# """, unsafe_allow_html=True)


# # ── Grade colour helpers ─────────────────────────────────────────────────────
# GRADE_COLORS = {"Class 1": "#10b981", "Class 2": "#3b82f6", "Class 3": "#f59e0b", "Class 4": "#ef4444"}
# GRADE_CSS   = {"Class 1": "g1",       "Class 2": "g2",       "Class 3": "g3",       "Class 4": "g4"}

# def badge(label, color="#f5c842", bg_alpha=0.15):
#     rgb = hex_to_rgb(color)
#     return (f'<span class="vd-badge" style="background:rgba({rgb},{bg_alpha});'
#             f'color:{color};border:1px solid rgba({rgb},0.3)">{html.escape(str(label))}</span>')

# def hex_to_rgb(h):
#     h = h.lstrip('#')
#     r,g,b = int(h[0:2],16), int(h[2:4],16), int(h[4:6],16)
#     return f"{r},{g},{b}"

# def kpi_html(label, value, sub=""):
#     return (f'<div class="vd-kpi"><div class="vd-kpi-label">{html.escape(str(label))}</div>'
#             f'<div class="vd-kpi-value">{html.escape(str(value))}</div>'
#             + (f'<div style="font-size:.75rem;color:rgba(232,234,240,.45);margin-top:1px">{html.escape(str(sub))}</div>' if sub else "")
#             + '</div>')

# def section_label(text):
#     st.markdown(f'<div class="vd-section-label">{html.escape(text)}</div>', unsafe_allow_html=True)

# def progress_bar(pct, color="#f5c842"):
#     return (f'<div class="vd-progress-outer"><div class="vd-progress-inner" '
#             f'style="width:{pct}%;background:{color}"></div></div>')


# # ── Sidebar ──────────────────────────────────────────────────────────────────
# def render_sidebar():
#     with st.sidebar:
#         st.markdown(
#             '<div class="sidebar-logo">🪔 Vidyalaya AI<span>Multigrade Teaching Assistant · Prototype</span></div>',
#             unsafe_allow_html=True
#         )

#         st.markdown('<div class="vd-section-label" style="padding-left:4px">Navigation</div>', unsafe_allow_html=True)
#         page = st.radio("Navigation", [
#             "🏠  Dashboard",
#             "📅  Course Planner",
#             "🎯  Activity Generator",
#             "📝  Worksheet Generator",
#             "📊  Assessment Generator",
#             "🎨  Visual Aids",
#             "🤝  Peer Activities",
#             "📈  Progress Tracker",
#             "📚  NCERT Explorer",
#         ], label_visibility="collapsed")

#         st.divider()
#         st.markdown('<div class="vd-section-label" style="padding-left:4px">Classroom Context</div>', unsafe_allow_html=True)

#         grades = st.multiselect("Grades", ["Class 1","Class 2","Class 3","Class 4"],
#                                 default=["Class 1","Class 2","Class 3","Class 4"],
#                                 label_visibility="visible")
#         subjects = st.multiselect("Subjects", ["Mathematics","English","EVS","Science","Hindi"],
#                                   default=["Mathematics","English"],
#                                   label_visibility="visible")
#         class_size = st.slider("Class Size", 8, 50, 26)
#         duration   = st.slider("Duration (min)", 20, 90, 45)

#         st.divider()
#         today_str = datetime.now().strftime("%A, %d %b %Y")
#         st.caption(f"📆 {today_str}")
#         st.caption("🏫 Government Primary School · Demo")

#     return page.strip(), grades, subjects, class_size, duration


# # ══════════════════════════════════════════════════════════════════════════════
# #  DASHBOARD
# # ══════════════════════════════════════════════════════════════════════════════
# def page_dashboard():
#     st.markdown("## 🏠 Teacher Dashboard")

#     logs = STUDENT_DATA["lesson_logs"]
#     students = STUDENT_DATA["students"]
#     coverage = STUDENT_DATA["curriculum_coverage"]

#     # ── KPIs ─────────────────────────────────────────────────────────────────
#     c1,c2,c3,c4 = st.columns(4)
#     c1.metric("📚 Lessons This Month", len(logs), "+3 vs last month")
#     c2.metric("👩‍🎓 Total Students", len(students), "4 classes")
#     c3.metric("✅ Avg Completion", "91%", "+4% this week")
#     c4.metric("🌟 Top Performer", "Meera Gupta", "Class 4 · 98%")

#     st.divider()

#     left, right = st.columns([3,2], gap="large")

#     with left:
#         st.markdown("### 📅 Recent Lesson Logs")
#         section_label("Last 7 Sessions")
#         for log in logs[-7:]:
#             subject_color = {"Mathematics":"#3b82f6","English":"#10b981","EVS":"#f59e0b","Science":"#8b5cf6","Hindi":"#ec4899"}.get(log["subject"],"#6b7280")
#             grades_str = " ".join([badge(g, GRADE_COLORS.get(g,"#aaa")) for g in log["grades"]])
#             comp_col = "#10b981" if log["completion"]==100 else ("#f59e0b" if log["completion"]>=80 else "#ef4444")
#             st.markdown(f"""
# <div class="vd-log-row">
#   <span class="vd-log-date">{log['date'][5:]}</span>
#   <span style="color:{subject_color};font-weight:600;font-size:.85rem">{log['subject']}</span>
#   <span class="vd-log-topic">{log['topic']} &nbsp;{grades_str}</span>
#   <span style="color:{comp_col};font-weight:700;font-size:.88rem">{log['completion']}%</span>
# </div>""", unsafe_allow_html=True)

#     with right:
#         st.markdown("### 📊 Curriculum Coverage")
#         section_label("By Subject & Class")
#         for subject, cls_data in coverage.items():
#             with st.expander(f"**{subject}**", expanded=False):
#                 for cls, info in cls_data.items():
#                     pct = info["percent"]
#                     col_c = GRADE_COLORS.get(cls,"#aaa")
#                     st.markdown(
#                         f'{badge(cls, col_c)} &nbsp;<span style="font-size:.82rem;color:rgba(232,234,240,.6)">{pct}% covered</span>'
#                         + progress_bar(pct, col_c),
#                         unsafe_allow_html=True
#                     )
#                     st.markdown("")

#     st.divider()

#     st.markdown("### 📋 Weekly Summary")
#     ws = WEEKLY_SUMMARY
#     col_a, col_b, col_c = st.columns(3)

#     with col_a:
#         section_label("✅ Highlights")
#         for h in ws["highlights"]:
#             st.markdown(f'<div class="vd-highlight-item"><div class="vd-dot-green"></div><span>{h}</span></div>', unsafe_allow_html=True)

#     with col_b:
#         section_label("⚠️ Needs Attention")
#         for a in ws["areas_for_improvement"]:
#             st.markdown(f'<div class="vd-highlight-item"><div class="vd-dot-amber"></div><span>{a}</span></div>', unsafe_allow_html=True)

#     with col_c:
#         section_label("📅 Next Week")
#         for n in ws["next_week_focus"]:
#             st.markdown(f'<div class="vd-highlight-item"><div class="vd-dot-blue"></div><span>{n}</span></div>', unsafe_allow_html=True)


# # ══════════════════════════════════════════════════════════════════════════════
# #  COURSE PLANNER
# # ══════════════════════════════════════════════════════════════════════════════
# def page_course_planner(grades, subjects, class_size, duration):
#     st.markdown("## 📅 Daily Course Planner")

#     c1, c2 = st.columns([3,2], gap="large")
#     with c1:
#         topic = st.text_input("Lesson Topic", value="Numbers and Basic Operations",
#                               placeholder="e.g. Addition and Subtraction")
#         objectives = st.text_area("Learning Objectives (one per line)",
#             value="Class 1: Count and add up to 20\nClass 2: Two-digit addition\nClass 3: Multiplication basics\nClass 4: Problem solving with large numbers",
#             height=100)
#     with c2:
#         st.markdown('<div class="vd-card"><div class="vd-card-title">Session Setup</div>', unsafe_allow_html=True)
#         st.info(f"**Grades:** {', '.join(grades) if grades else 'None selected'}\n\n"
#                 f"**Subjects:** {', '.join(subjects) if subjects else 'None'}\n\n"
#                 f"**Class size:** {class_size} &nbsp;·&nbsp; **Duration:** {duration} min")
#         st.markdown('</div>', unsafe_allow_html=True)

#     if st.button("🚀 Generate Course Plan", type="primary"):
#         with st.spinner("Building your multigrade lesson plan…"):
#             import time; time.sleep(1.2)
#         st.success("✅ Lesson plan generated from NCERT curriculum data!")
#         render_course_plan(HARDCODED_COURSE_PLANS["default"])

#     st.markdown("---")
#     st.markdown('<div style="font-size:.82rem;color:rgba(232,234,240,.4)">💡 Sample plan shown below — click Generate to re-render</div>', unsafe_allow_html=True)
#     render_course_plan(HARDCODED_COURSE_PLANS["default"])


# def render_course_plan(plan):
#     p = plan
#     kpis = "".join([
#         kpi_html("Duration", f"{p['total_duration']} min"),
#         kpi_html("Grade groups", len(p["grade_groupings"])),
#         kpi_html("Timeline slots", len(p["timeline"])),
#         kpi_html("Homework tasks", len(p["homework_assignments"])),
#     ])
#     st.markdown(f"""
# <div class="vd-hero">
#   <div class="vd-hero-title">📅 {html.escape(p['lesson_title'])}</div>
#   <div class="vd-hero-sub">Differentiated multigrade lesson plan · NCERT aligned</div>
#   <div class="vd-kpis">{kpis}</div>
# </div>""", unsafe_allow_html=True)

#     tabs = st.tabs(["🗂️ Overview", "👥 Grade Groups", "⏱️ Timeline", "📋 Notes & HW"])

#     with tabs[0]:
#         section_label("Lesson at a glance")
#         for grp in p["grade_groupings"]:
#             c = GRADE_COLORS.get(grp["grade"],"#aaa")
#             css_c = GRADE_CSS.get(grp["grade"],"g1")
#             objs  = " &nbsp;·&nbsp; ".join(grp["specific_objectives"])
#             mats  = ", ".join(grp["materials"])
#             st.markdown(f"""
# <div class="vd-grade-band {css_c}">
#   <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:6px">
#     {badge(grp['grade'], c)}
#     <span style="font-size:.82rem;color:rgba(232,234,240,.55)">{grp['group_size']} students</span>
#   </div>
#   <div style="font-size:.88rem;color:rgba(232,234,240,.8);margin-bottom:4px">🎯 {objs}</div>
#   <div style="font-size:.82rem;color:rgba(232,234,240,.55)">📦 {mats}</div>
# </div>""", unsafe_allow_html=True)

#     with tabs[1]:
#         section_label("Differentiated objectives by grade")
#         for grp in p["grade_groupings"]:
#             c = GRADE_COLORS.get(grp["grade"],"#aaa")
#             css_c = GRADE_CSS.get(grp["grade"],"g1")
#             with st.expander(f"**{grp['grade']}** — {grp['group_size']} students", expanded=True):
#                 ca, cb = st.columns(2)
#                 with ca:
#                     st.markdown("**Objectives**")
#                     for obj in grp["specific_objectives"]:
#                         st.markdown(f'<div style="font-size:.88rem;padding:3px 0;color:rgba(232,234,240,.85)">✦ {obj}</div>', unsafe_allow_html=True)
#                 with cb:
#                     st.markdown("**Materials needed**")
#                     for mat in grp["materials"]:
#                         st.markdown(f'<div style="font-size:.88rem;padding:3px 0;color:rgba(232,234,240,.85)">📦 {mat}</div>', unsafe_allow_html=True)

#     with tabs[2]:
#         section_label("Minute-by-minute lesson flow")
#         for slot in p["timeline"]:
#             with st.expander(f"**{slot['time_slot']}** — {slot['activity']}", expanded=False):
#                 gcols = st.columns(4)
#                 grade_task_map = {
#                     "Class 1": slot.get("class_1_task",""),
#                     "Class 2": slot.get("class_2_task",""),
#                     "Class 3": slot.get("class_3_task",""),
#                     "Class 4": slot.get("class_4_task",""),
#                 }
#                 for i,(g,task) in enumerate(grade_task_map.items()):
#                     c = GRADE_COLORS.get(g,"#aaa")
#                     css_c = GRADE_CSS.get(g,"g1")
#                     with gcols[i]:
#                         st.markdown(f"""
# <div class="vd-grade-band {css_c}" style="height:100%">
#   {badge(g, c)}
#   <div style="font-size:.85rem;color:rgba(232,234,240,.8);margin-top:6px">{html.escape(task)}</div>
# </div>""", unsafe_allow_html=True)
#                 st.markdown(f"""
# <div style="margin-top:10px;padding:10px 14px;background:rgba(245,200,66,.06);border-radius:10px;border:1px solid rgba(245,200,66,.15)">
#   <span style="font-weight:600;color:#f5c842;font-size:.82rem">👩‍🏫 Teacher Role:</span>
#   <span style="font-size:.85rem;color:rgba(232,234,240,.8);margin-left:6px">{html.escape(slot.get('teacher_role',''))}</span>
# </div>""", unsafe_allow_html=True)

#     with tabs[3]:
#         col_n, col_h = st.columns(2)
#         with col_n:
#             section_label("Classroom Management")
#             cm = p["classroom_management"]
#             st.markdown(f'**Setup:** {cm["setup"]}')
#             st.markdown("**Attention signals:**")
#             for sig in cm["attention_signals"]:
#                 st.markdown(f'<div style="font-size:.87rem;padding:2px 0">🔔 {sig}</div>', unsafe_allow_html=True)
#             st.markdown("**Behaviour strategies:**")
#             for b_item in cm["behavior_strategies"]:
#                 st.markdown(f'<div style="font-size:.87rem;padding:2px 0">✦ {b_item}</div>', unsafe_allow_html=True)

#         with col_h:
#             section_label("Homework Assignments")
#             for hw in p["homework_assignments"]:
#                 c = GRADE_COLORS.get(hw["grade"],"#aaa")
#                 st.markdown(f"""
# <div class="vd-card" style="margin-bottom:8px">
#   <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px">
#     {badge(hw['grade'], c)}
#     <span style="font-size:.78rem;color:rgba(232,234,240,.45)">{hw['estimated_time']} min</span>
#   </div>
#   <div style="font-size:.88rem;color:rgba(232,234,240,.8)">{html.escape(hw['task'])}</div>
# </div>""", unsafe_allow_html=True)

#         st.divider()
#         section_label("Differentiation Strategies")
#         d = p["differentiation_strategies"]
#         da, db, dc = st.columns(3)
#         with da:
#             st.markdown("**🤝 Support students**")
#             for s in d["support_students"]: st.markdown(f'<div style="font-size:.84rem;padding:2px 0">• {s}</div>', unsafe_allow_html=True)
#         with db:
#             st.markdown("**🚀 Advanced students**")
#             for s in d["advanced_students"]: st.markdown(f'<div style="font-size:.84rem;padding:2px 0">• {s}</div>', unsafe_allow_html=True)
#         with dc:
#             st.markdown("**🌍 English learners**")
#             for s in d["english_learners"]: st.markdown(f'<div style="font-size:.84rem;padding:2px 0">• {s}</div>', unsafe_allow_html=True)

#         if st.button("💾 Mark as Taught & Log Lesson", key="log_course"):
#             st.success("✅ Lesson logged! Progress tracker updated.")


# # ══════════════════════════════════════════════════════════════════════════════
# #  ACTIVITY GENERATOR
# # ══════════════════════════════════════════════════════════════════════════════
# def page_activity_generator(grades, subjects, class_size, duration):
#     st.markdown("## 🎯 Learning Activity Generator")

#     c1, c2 = st.columns([3,2])
#     with c1:
#         topic = st.text_input("Activity Topic", value="Plant Life Cycle", placeholder="e.g. Water Cycle")
#         act_type = st.selectbox("Activity Type", ["Outdoor Exploration","Group Activity","Individual Work","Learning Stations","Whole Class"])
#     with c2:
#         st.info(f"**Grades:** {', '.join(grades) if grades else 'None'}\n\n**Subjects:** {', '.join(subjects) if subjects else 'None'}")

#     if st.button("🎯 Generate Activity", type="primary"):
#         with st.spinner("Crafting an engaging multigrade activity…"):
#             import time; time.sleep(1.0)
#         st.success("✅ Activity ready!")
#         render_activity(HARDCODED_ACTIVITIES["default"])
#     else:
#         render_activity(HARDCODED_ACTIVITIES["default"])


# def render_activity(act):
#     kpis = "".join([
#         kpi_html("Type", act["activity_type"]),
#         kpi_html("Duration", f"{act['estimated_duration']} min"),
#         kpi_html("Grade groups", len(act["grade_adaptations"])),
#         kpi_html("Steps", len(act["step_by_step_process"])),
#     ])
#     st.markdown(f"""
# <div class="vd-hero">
#   <div class="vd-hero-title">🎯 {html.escape(act['activity_title'])}</div>
#   <div class="vd-hero-sub">Ready-to-run activity with grade-wise adaptations and assessment rubric</div>
#   <div class="vd-kpis">{kpis}</div>
# </div>""", unsafe_allow_html=True)

#     tabs = st.tabs(["📋 Setup", "👥 Grade Adaptations", "🔢 Steps", "📊 Rubric", "🔄 Variations"])

#     with tabs[0]:
#         ca, cb = st.columns([2,1])
#         with ca:
#             section_label("Setup Instructions")
#             st.markdown(f'<div style="font-size:.92rem;line-height:1.7">{html.escape(act["setup_instructions"])}</div>', unsafe_allow_html=True)
#         with cb:
#             section_label("Materials Needed")
#             for m in act["materials_needed"]:
#                 st.markdown(f'<div style="font-size:.88rem;padding:3px 0">📦 {m}</div>', unsafe_allow_html=True)

#     with tabs[1]:
#         for g in act["grade_adaptations"]:
#             grade_name = g["grade"]
#             c = GRADE_COLORS.get(grade_name,"#aaa")
#             css_c = GRADE_CSS.get(grade_name,"g1")
#             with st.expander(f"**{grade_name}** Adaptation", expanded=grade_name=="Class 1"):
#                 st.markdown(f"""
# <div class="vd-grade-band {css_c}">
#   {badge(grade_name, c)}
#   <div style="font-size:.90rem;color:rgba(232,234,240,.85);margin-top:8px;line-height:1.6">{html.escape(g['instructions'])}</div>
# </div>""", unsafe_allow_html=True)
#                 col_ex, col_sc, col_ext = st.columns(3)
#                 with col_ex:
#                     st.markdown("**Examples**")
#                     for e in g["examples"]: st.markdown(f'<div style="font-size:.82rem;padding:2px 0">💡 {e}</div>', unsafe_allow_html=True)
#                 with col_sc:
#                     st.markdown("**Success Criteria**")
#                     for s in g["success_criteria"]: st.markdown(f'<div style="font-size:.82rem;padding:2px 0">✅ {s}</div>', unsafe_allow_html=True)
#                 with col_ext:
#                     st.markdown("**Extensions**")
#                     for ex in g["extension_activities"]: st.markdown(f'<div style="font-size:.82rem;padding:2px 0">🚀 {ex}</div>', unsafe_allow_html=True)

#     with tabs[2]:
#         section_label("Step-by-step process")
#         for step in act["step_by_step_process"]:
#             col_s, col_c = st.columns([1,8])
#             with col_s:
#                 st.markdown(f'<div class="vd-q-number" style="margin-top:8px">{step["step"]}</div>', unsafe_allow_html=True)
#             with col_c:
#                 with st.expander(f"**{step['time_estimate']} min** — {step['instruction'][:60]}…", expanded=step["step"]==1):
#                     st.markdown(f'<div style="font-size:.90rem;line-height:1.65">{html.escape(step["instruction"])}</div>', unsafe_allow_html=True)
#                     if step.get("teacher_notes"):
#                         st.markdown(f"""
# <div style="margin-top:8px;padding:8px 12px;background:rgba(245,200,66,.06);border-radius:8px;border-left:3px solid #f5c842;font-size:.83rem;color:rgba(232,234,240,.75)">
#   👩‍🏫 <em>{html.escape(step['teacher_notes'])}</em>
# </div>""", unsafe_allow_html=True)

#     with tabs[3]:
#         section_label("Assessment Rubric")
#         header = '<div class="vd-rubric-row"><div class="vd-rubric-cell vd-rubric-header">Criteria</div><div class="vd-rubric-cell vd-rubric-header">Beginner</div><div class="vd-rubric-cell vd-rubric-header">Developing</div><div class="vd-rubric-cell vd-rubric-header">Proficient</div><div class="vd-rubric-cell vd-rubric-header">Advanced</div></div>'
#         rows = ""
#         for r in act["assessment_rubric"]:
#             rows += f'<div class="vd-rubric-row"><div class="vd-rubric-cell"><b>{r["criteria"]}</b></div><div class="vd-rubric-cell vd-rubric-ni">{r["beginner"]}</div><div class="vd-rubric-cell vd-rubric-sat">{r["developing"]}</div><div class="vd-rubric-cell vd-rubric-gd">{r["proficient"]}</div><div class="vd-rubric-cell vd-rubric-exc">{r["advanced"]}</div></div>'
#         st.markdown(header + rows, unsafe_allow_html=True)

#     with tabs[4]:
#         for v in act["variations"]:
#             with st.expander(f"🔄 {v['variation_name']}"):
#                 st.markdown(v["description"])
#                 for s in v["suitable_for"]:
#                     st.markdown(badge(s), unsafe_allow_html=True)


# # ══════════════════════════════════════════════════════════════════════════════
# #  WORKSHEET GENERATOR
# # ══════════════════════════════════════════════════════════════════════════════
# def page_worksheet_generator(grades, subjects, class_size, duration):
#     st.markdown("## 📝 Worksheet Generator")

#     c1, c2 = st.columns([3,2])
#     with c1:
#         topic = st.text_input("Worksheet Topic", value="Numbers, Sentences and Everyday Life")
#         diff = st.selectbox("Difficulty Range", ["Mixed Levels", "Beginner to Intermediate", "Intermediate to Advanced"])
#     with c2:
#         st.info(f"**Grades:** {', '.join(grades) if grades else 'None'}\n\n**Subjects:** {', '.join(subjects) if subjects else 'None'}")

#     if st.button("📝 Generate Worksheet", type="primary"):
#         with st.spinner("Creating differentiated worksheets…"):
#             import time; time.sleep(1.0)
#         st.success("✅ Worksheets ready — all 4 grade levels!")
#         render_worksheet(HARDCODED_WORKSHEETS["default"])
#     else:
#         render_worksheet(HARDCODED_WORKSHEETS["default"])


# def render_worksheet(ws):
#     instr = ws["instructions"]
#     kpis = "".join([
#         kpi_html("Subject", ws["subject"].split("+")[0].strip()),
#         kpi_html("Grades", len(ws["grade_levels"])),
#         kpi_html("Sections", len(ws["sections"])),
#         kpi_html("Est. Time", f"{instr.get('time_estimate','?')} min"),
#     ])
#     st.markdown(f"""
# <div class="vd-hero">
#   <div class="vd-hero-title">📝 {html.escape(ws['worksheet_title'])}</div>
#   <div class="vd-hero-sub">{html.escape(ws['subject'])} &nbsp;·&nbsp; {html.escape(ws['topic'])}</div>
#   <div class="vd-kpis">{kpis}</div>
# </div>""", unsafe_allow_html=True)

#     q_type_icons = {"fill_blank":"✏️","drawing":"🖼️","multiple_choice":"🔘","short_answer":"✍️","matching":"🔗"}

#     tabs = st.tabs(["📄 Instructions", "📋 Questions", "🔑 Answer Key", "➕ Extensions"])

#     with tabs[0]:
#         ca, cb = st.columns(2)
#         with ca:
#             section_label("Student Instructions")
#             st.markdown(f'<div style="font-size:.92rem;line-height:1.7;padding:14px;background:rgba(255,255,255,.03);border-radius:12px;border:1px solid rgba(255,255,255,.08)">{html.escape(instr["student_instructions"])}</div>', unsafe_allow_html=True)
#         with cb:
#             section_label("Teacher Notes")
#             st.markdown(f'<div style="font-size:.88rem;line-height:1.7;color:rgba(232,234,240,.75)">{html.escape(instr["teacher_notes"])}</div>', unsafe_allow_html=True)

#     with tabs[1]:
#         grade_sections = {}
#         for sec in ws["sections"]:
#             g = sec["grade_target"]
#             grade_sections.setdefault(g,[]).append(sec)

#         grade_tabs = st.tabs([g for g in grade_sections.keys()])
#         for i,(g,secs) in enumerate(grade_sections.items()):
#             with grade_tabs[i]:
#                 c_color = GRADE_COLORS.get(g,"#aaa")
#                 st.markdown(badge(g, c_color), unsafe_allow_html=True)
#                 for sec in secs:
#                     section_label(f"{sec['section_title']} — {sec['difficulty_level']}")
#                     for q in sec["questions"]:
#                         icon = q_type_icons.get(q["question_type"],"❓")
#                         st.markdown(f"""
# <div class="vd-q-card">
#   <div style="display:flex;align-items:flex-start;gap:0">
#     <span class="vd-q-number">{q['question_number']}</span>
#     <div style="flex:1">
#       <div style="display:flex;align-items:center;gap:8px;margin-bottom:6px">
#         <span style="font-size:.85rem;font-weight:600">{html.escape(q['question_text'])}</span>
#       </div>
#       <div style="display:flex;align-items:center;gap:8px">
#         <span style="font-size:.75rem;padding:2px 8px;border-radius:6px;background:rgba(255,255,255,.06);color:rgba(232,234,240,.6)">{icon} {q['question_type'].replace('_',' ').title()}</span>
#         <span style="font-size:.75rem;color:rgba(232,234,240,.4)">{q['points']} pt{'s' if q['points']!=1 else ''}</span>
#       </div>
#       {('<div style="margin-top:6px;display:flex;flex-wrap:wrap;gap:4px">' + "".join([f'<span style="padding:2px 10px;border-radius:6px;background:rgba(255,255,255,.05);font-size:.80rem">{o}</span>' for o in (q.get("options") or [])]) + '</div>') if q.get("options") else ''}
#     </div>
#   </div>
# </div>""", unsafe_allow_html=True)

#     with tabs[2]:
#         section_label("Answer Key — Teacher Reference")
#         for sa in ws["answer_key"]["section_answers"]:
#             with st.expander(f"**{sa['section']}**"):
#                 ca, cb = st.columns(2)
#                 with ca:
#                     st.markdown("**Answers**")
#                     for j,ans in enumerate(sa["answers"]):
#                         st.markdown(f'<div style="font-size:.88rem;padding:2px 0">Q{j+1}: <b style="color:#10b981">{ans}</b></div>', unsafe_allow_html=True)
#                 with cb:
#                     st.markdown("**Explanations**")
#                     for exp in sa["explanations"]:
#                         st.markdown(f'<div style="font-size:.83rem;padding:2px 0;color:rgba(232,234,240,.7)">💡 {exp}</div>', unsafe_allow_html=True)

#     with tabs[3]:
#         section_label("Extension Activities")
#         for ex in ws["extension_activities"]:
#             st.markdown(f"""
# <div class="vd-card">
#   <div class="vd-card-title">🚀 {html.escape(ex['activity'])}</div>
#   <div class="vd-card-meta">For: {ex['suitable_for']} &nbsp;·&nbsp; Materials: {', '.join(ex['materials_needed'])}</div>
# </div>""", unsafe_allow_html=True)

#     if st.button("🖨️ Export Worksheet as PDF", key="export_ws"):
#         st.success("✅ PDF export ready! (In production, this would generate a print-ready PDF)")


# # ══════════════════════════════════════════════════════════════════════════════
# #  ASSESSMENT GENERATOR
# # ══════════════════════════════════════════════════════════════════════════════
# def page_assessment_generator(grades, subjects, class_size, duration):
#     st.markdown("## 📊 Assessment Generator")

#     c1, c2 = st.columns([3,2])
#     with c1:
#         topic = st.text_input("Assessment Topic", value="Term 1 Core Concepts")
#         atype = st.selectbox("Assessment Type", ["Summative + Formative Mix","Formative","Summative","Diagnostic"])
#     with c2:
#         st.info(f"**Grades:** {', '.join(grades) if grades else 'None'}\n\n**Subjects:** {', '.join(subjects) if subjects else 'None'}")

#     if st.button("📊 Generate Assessment Plan", type="primary"):
#         with st.spinner("Designing comprehensive multigrade assessment…"):
#             import time; time.sleep(1.1)
#         st.success("✅ Assessment plan ready — fully differentiated!")
#         render_assessment(HARDCODED_ASSESSMENTS["default"])
#     else:
#         render_assessment(HARDCODED_ASSESSMENTS["default"])


# def render_assessment(asmnt):
#     kpis = "".join([
#         kpi_html("Type", asmnt["assessment_type"]),
#         kpi_html("Duration", f"{asmnt['duration']} min"),
#         kpi_html("Components", len(asmnt["assessment_components"])),
#         kpi_html("Formative checks", len(asmnt["formative_checks"])),
#     ])
#     st.markdown(f"""
# <div class="vd-hero">
#   <div class="vd-hero-title">📊 {html.escape(asmnt['assessment_title'])}</div>
#   <div class="vd-hero-sub">Grade-adapted assessment with rubrics, formative checks & data collection</div>
#   <div class="vd-kpis">{kpis}</div>
# </div>""", unsafe_allow_html=True)

#     tabs = st.tabs(["👥 Grade Adaptations", "📦 Components & Rubrics", "🔁 Formative Checks", "📂 Data Collection"])

#     with tabs[0]:
#         for a in asmnt["grade_adaptations"]:
#             grade = a["grade"]
#             c = GRADE_COLORS.get(grade,"#aaa")
#             css_c = GRADE_CSS.get(grade,"g1")
#             with st.expander(f"**{grade}** — {a['assessment_method'][:50]}…", expanded=False):
#                 st.markdown(f"""
# <div class="vd-grade-band {css_c}">
#   {badge(grade, c)}
#   <div style="font-size:.90rem;color:rgba(232,234,240,.8);margin-top:6px"><b>Method:</b> {html.escape(a['assessment_method'])}</div>
# </div>""", unsafe_allow_html=True)
#                 ca, cb = st.columns(2)
#                 with ca:
#                     st.markdown("**Success Criteria**")
#                     for s in a["success_criteria"]: st.markdown(f'<div style="font-size:.85rem;padding:2px 0">✅ {s}</div>', unsafe_allow_html=True)
#                 with cb:
#                     st.markdown("**Accommodations**")
#                     for ac in a["accommodations"]: st.markdown(f'<div style="font-size:.85rem;padding:2px 0">🤝 {ac}</div>', unsafe_allow_html=True)

#     with tabs[1]:
#         for comp in asmnt["assessment_components"]:
#             with st.expander(f"**{comp['component_name']}** — {comp['weight_percentage']}% of total", expanded=False):
#                 st.markdown(f'<div style="font-size:.88rem;color:rgba(232,234,240,.7);margin-bottom:12px">{html.escape(comp["description"])}</div>', unsafe_allow_html=True)
#                 for t in comp["grade_specific_tasks"]:
#                     grade = t["grade"]
#                     c = GRADE_COLORS.get(grade,"#aaa")
#                     css_c = GRADE_CSS.get(grade,"g1")
#                     r = t["scoring_rubric"]
#                     st.markdown(f"""
# <div class="vd-grade-band {css_c}" style="margin-bottom:8px">
#   {badge(grade, c)} <span style="font-size:.85rem;margin-left:6px;color:rgba(232,234,240,.8)">{html.escape(t['task'])}</span>
#   <div class="vd-rubric-row" style="margin-top:8px">
#     <div class="vd-rubric-cell vd-rubric-exc">⭐ <b>Excellent:</b> {r['excellent']}</div>
#     <div class="vd-rubric-cell vd-rubric-gd">👍 <b>Good:</b> {r['good']}</div>
#     <div class="vd-rubric-cell vd-rubric-sat" style="grid-column:span 1">📝 <b>Satisfactory:</b> {r['satisfactory']}</div>
#     <div class="vd-rubric-cell vd-rubric-ni">⚠️ <b>Needs work:</b> {r['needs_improvement']}</div>
#   </div>
# </div>""", unsafe_allow_html=True)

#     with tabs[2]:
#         section_label("Ongoing formative assessment checkpoints")
#         for fc in asmnt["formative_checks"]:
#             st.markdown(f"""
# <div class="vd-card">
#   <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
#     <div class="vd-card-title">🔁 {html.escape(fc['checkpoint'])}</div>
#     <span style="font-size:.78rem;padding:2px 8px;background:rgba(245,200,66,.1);border-radius:6px;color:#f5c842">{fc['frequency']}</span>
#   </div>
#   <div style="font-size:.85rem;color:rgba(232,234,240,.7)"><b>Method:</b> {html.escape(fc['method'])}</div>
#   <div style="font-size:.85rem;color:rgba(232,234,240,.65);margin-top:3px"><b>Feedback:</b> {html.escape(fc['feedback_strategy'])}</div>
# </div>""", unsafe_allow_html=True)

#     with tabs[3]:
#         dc = asmnt["data_collection"]
#         ca, cb, cc = st.columns(3)
#         with ca:
#             section_label("Observation Checklist")
#             for item in dc["observation_checklist"]:
#                 st.checkbox(item, key=f"obs_{item[:20]}")
#         with cb:
#             section_label("Portfolio Items")
#             for item in dc["portfolio_items"]:
#                 st.markdown(f'<div style="font-size:.85rem;padding:3px 0">📁 {item}</div>', unsafe_allow_html=True)
#         with cc:
#             section_label("Self-Assessment Tools")
#             for item in dc["self_assessment_tools"]:
#                 st.markdown(f'<div style="font-size:.85rem;padding:3px 0">🪞 {item}</div>', unsafe_allow_html=True)


# # ══════════════════════════════════════════════════════════════════════════════
# #  VISUAL AIDS
# # ══════════════════════════════════════════════════════════════════════════════
# def page_visual_aids(grades, subjects, class_size, duration):
#     st.markdown("## 🎨 Visual Aids Generator")

#     c1, c2 = st.columns([3,2])
#     with c1:
#         topic = st.text_input("Visual Aid Topic", value="The Living World — Plants & Numbers")
#         aid_type = st.selectbox("Aid Type", ["Interactive Wall Display","Poster","Chart","Diagram","Manipulatives"])
#     with c2:
#         st.info(f"**Grades:** {', '.join(grades) if grades else 'None'}\n\n**Subjects:** {', '.join(subjects) if subjects else 'None'}")

#     if st.button("🎨 Generate Visual Aid Design", type="primary"):
#         with st.spinner("Designing multigrade visual learning aid…"):
#             import time; time.sleep(1.0)
#         st.success("✅ Visual aid design ready!")
#         render_visual_aid(HARDCODED_VISUAL_AIDS["default"])
#     else:
#         render_visual_aid(HARDCODED_VISUAL_AIDS["default"])


# def render_visual_aid(va):
#     kpis = "".join([
#         kpi_html("Type", va["aid_type"]),
#         kpi_html("Size", va["size_specifications"][:20]+"…"),
#         kpi_html("Materials", len(va["materials_needed"])),
#         kpi_html("Digital alts", len(va["digital_alternatives"])),
#     ])
#     st.markdown(f"""
# <div class="vd-hero">
#   <div class="vd-hero-title">🎨 {html.escape(va['visual_aid_title'])}</div>
#   <div class="vd-hero-sub">Classroom display design with grade-specific interaction zones</div>
#   <div class="vd-kpis">{kpis}</div>
# </div>""", unsafe_allow_html=True)

#     tabs = st.tabs(["🖼️ Design Spec", "👥 Grade Zones", "📖 Usage Guide", "💻 Digital Alternatives"])

#     with tabs[0]:
#         ca, cb = st.columns([3,2])
#         d = va["content_description"]
#         with ca:
#             section_label("Main Visual Concept")
#             st.markdown(f'<div style="font-size:.92rem;line-height:1.7;padding:14px;background:rgba(255,255,255,.03);border-radius:12px;border:1px solid rgba(255,255,255,.08)">{html.escape(d["main_visual"])}</div>', unsafe_allow_html=True)
#             st.markdown("**Layout Description**")
#             st.markdown(f'<div style="font-size:.88rem;color:rgba(232,234,240,.75);margin-top:4px">{html.escape(d["layout_description"])}</div>', unsafe_allow_html=True)
#         with cb:
#             section_label("Visual Elements")
#             st.markdown(f"**Colour Scheme:** {d['color_scheme']}")
#             st.markdown("**Text Elements:**")
#             for t in d["text_elements"]: st.markdown(f'<div style="font-size:.83rem;padding:2px 0">🏷️ {t}</div>', unsafe_allow_html=True)
#             st.markdown("**Materials:**")
#             for m in va["materials_needed"]: st.markdown(f'<div style="font-size:.83rem;padding:2px 0">📦 {m}</div>', unsafe_allow_html=True)

#     with tabs[1]:
#         for ge in va["grade_specific_elements"]:
#             grade = ge["grade"]
#             c = GRADE_COLORS.get(grade,"#aaa")
#             css_c = GRADE_CSS.get(grade,"g1")
#             with st.expander(f"**{grade}** Zone", expanded=False):
#                 st.markdown(f"""
# <div class="vd-grade-band {css_c}">
#   {badge(grade, c)}
#   <div style="margin-top:8px"><b style="font-size:.82rem;color:rgba(232,234,240,.55)">VISUAL FOCUS</b><br>
#   <span style="font-size:.90rem">{html.escape(ge['visual_focus'])}</span></div>
#   <div style="margin-top:8px"><b style="font-size:.82rem;color:rgba(232,234,240,.55)">INTERACTION METHOD</b><br>
#   <span style="font-size:.90rem">{html.escape(ge['interaction_method'])}</span></div>
#   <div style="margin-top:8px"><b style="font-size:.82rem;color:rgba(232,234,240,.55)">LEARNING SUPPORT</b><br>
#   <span style="font-size:.90rem">{html.escape(ge['learning_support'])}</span></div>
# </div>""", unsafe_allow_html=True)

#     with tabs[2]:
#         u = va["usage_instructions"]
#         section_label("Setup")
#         st.markdown(f'<div style="font-size:.90rem;line-height:1.65">{html.escape(u["setup"])}</div>', unsafe_allow_html=True)
#         section_label("Introduction Script")
#         st.markdown(f"""
# <div style="padding:14px 16px;background:rgba(245,200,66,.06);border-radius:12px;border:1px solid rgba(245,200,66,.15);font-size:.90rem;line-height:1.7;color:rgba(232,234,240,.85);font-style:italic">
#   💬 "{html.escape(u['introduction_script'])}"
# </div>""", unsafe_allow_html=True)
#         ca, cb = st.columns(2)
#         with ca:
#             section_label("Interaction Activities")
#             for act in u["interaction_activities"]: st.markdown(f'<div style="font-size:.85rem;padding:3px 0">▶ {act}</div>', unsafe_allow_html=True)
#         with cb:
#             section_label("Maintenance Tips")
#             for tip in u["maintenance_tips"]: st.markdown(f'<div style="font-size:.85rem;padding:3px 0">🔧 {tip}</div>', unsafe_allow_html=True)

#     with tabs[3]:
#         for d in va["digital_alternatives"]:
#             with st.expander(f"💻 {d['platform']}"):
#                 st.markdown(d["description"])
#                 st.markdown("**Accessibility features:**")
#                 for f in d["accessibility_features"]: st.markdown(f'<div style="font-size:.83rem;padding:2px 0">♿ {f}</div>', unsafe_allow_html=True)


# # ══════════════════════════════════════════════════════════════════════════════
# #  PEER ACTIVITIES
# # ══════════════════════════════════════════════════════════════════════════════
# def page_peer_activities(grades, subjects, class_size, duration):
#     st.markdown("## 🤝 Peer Activity Generator")

#     c1, c2 = st.columns([3,2])
#     with c1:
#         topic = st.text_input("Collaboration Topic", value="Cross-Grade Story Relay")
#         collab_type = st.selectbox("Collaboration Type", ["Mixed Groups with Role Rotation","Buddy System","Mentoring Pairs","Learning Stations"])
#     with c2:
#         st.info(f"**Grades:** {', '.join(grades) if grades else 'None'}\n\n**Class size:** {class_size}")

#     if st.button("🤝 Generate Peer Activity", type="primary"):
#         with st.spinner("Designing cross-grade collaboration activity…"):
#             import time; time.sleep(1.0)
#         st.success("✅ Peer activity ready!")
#         render_peer_activity(HARDCODED_PEER_ACTIVITIES["default"])
#     else:
#         render_peer_activity(HARDCODED_PEER_ACTIVITIES["default"])


# def render_peer_activity(pa):
#     gs = pa["grouping_strategy"]
#     kpis = "".join([
#         kpi_html("Type", pa["collaboration_type"].split(" ")[0]),
#         kpi_html("Duration", f"{pa['duration']} min"),
#         kpi_html("Stations", len(pa["activity_stations"])),
#         kpi_html("Group size", gs["group_size"]),
#     ])
#     st.markdown(f"""
# <div class="vd-hero">
#   <div class="vd-hero-title">🤝 {html.escape(pa['activity_title'])}</div>
#   <div class="vd-hero-sub">Cross-grade collaboration with defined roles, stations, and reflection tools</div>
#   <div class="vd-kpis">{kpis}</div>
# </div>""", unsafe_allow_html=True)

#     tabs = st.tabs(["👥 Groups & Roles", "🏫 Stations", "🪞 Assessment", "🌈 Differentiation"])

#     with tabs[0]:
#         ca, cb = st.columns([1,1])
#         with ca:
#             section_label("Grouping Strategy")
#             st.markdown(f"""
# <div class="vd-card">
#   <div style="font-size:.88rem;margin-bottom:6px">👥 <b>Group size:</b> {gs['group_size']} students (one per grade)</div>
#   <div style="font-size:.88rem;margin-bottom:6px">🔀 <b>Mixing:</b> {gs['grade_mixing']}</div>
#   <div style="font-size:.88rem;margin-bottom:6px">🔄 <b>Rotation:</b> {gs['rotation_schedule']}</div>
# </div>""", unsafe_allow_html=True)
#             section_label("Pairing Criteria")
#             for p_item in gs["pairing_criteria"]:
#                 st.markdown(f'<div style="font-size:.85rem;padding:2px 0">• {p_item}</div>', unsafe_allow_html=True)
#         with cb:
#             section_label("Role Definitions")
#             for role in pa["role_definitions"]:
#                 grades_suitable = " ".join([badge(g, GRADE_COLORS.get(g,"#aaa")) for g in role["suitable_grades"]])
#                 with st.expander(f"**{role['role_name']}**"):
#                     st.markdown(grades_suitable, unsafe_allow_html=True)
#                     ca2, cb2 = st.columns(2)
#                     with ca2:
#                         st.markdown("**Responsibilities**")
#                         for r in role["responsibilities"]: st.markdown(f'<div style="font-size:.82rem;padding:2px 0">• {r}</div>', unsafe_allow_html=True)
#                     with cb2:
#                         st.markdown("**Skills Built**")
#                         for s in role["skills_developed"]: st.markdown(f'<div style="font-size:.82rem;padding:2px 0">🌱 {s}</div>', unsafe_allow_html=True)

#     with tabs[1]:
#         for station in pa["activity_stations"]:
#             with st.expander(f"**{station['station_name']}** — {station['time_allocation']} min", expanded=False):
#                 st.markdown(f'<div style="font-size:.88rem;margin-bottom:10px;color:rgba(232,234,240,.75)">🎯 <b>Objective:</b> {html.escape(station["learning_objective"])}</div>', unsafe_allow_html=True)
#                 inst = station["instructions"]
#                 ca, cb = st.columns(2)
#                 with ca:
#                     st.markdown(f"""
# <div style="padding:10px 12px;background:rgba(245,200,66,.06);border-radius:10px;border:1px solid rgba(245,200,66,.15);font-size:.85rem">
#   <b style="color:#f5c842">👩‍🏫 Mentor Guide:</b><br>{html.escape(inst['mentor_guide'])}
# </div>""", unsafe_allow_html=True)
#                     st.markdown("**Collaboration Prompts:**")
#                     for pr in inst["collaboration_prompts"]:
#                         st.markdown(f'<div style="font-size:.82rem;padding:2px 0;color:rgba(232,234,240,.7)">💬 "{pr}"</div>', unsafe_allow_html=True)
#                 with cb:
#                     st.markdown(f"""
# <div style="padding:10px 12px;background:rgba(59,130,246,.06);border-radius:10px;border:1px solid rgba(59,130,246,.15);font-size:.85rem">
#   <b style="color:#3b82f6">📝 Learner Tasks:</b><br>{html.escape(inst['learner_tasks'])}
# </div>""", unsafe_allow_html=True)
#                     if station.get("materials"):
#                         st.markdown("**Materials:**")
#                         for m in station["materials"]: st.markdown(f'<div style="font-size:.82rem;padding:2px 0">📦 {m}</div>', unsafe_allow_html=True)

#     with tabs[2]:
#         ass = pa["assessment_strategies"]
#         ca, cb, cc = st.columns(3)
#         with ca:
#             section_label("Peer Feedback Forms")
#             for pf in ass["peer_feedback_forms"]:
#                 st.text_area("", value="", placeholder=pf, height=50, key=f"pf_{pf[:15]}", label_visibility="collapsed")
#         with cb:
#             section_label("Self Reflection")
#             for sr in ass["self_reflection_prompts"]:
#                 st.markdown(f'<div style="font-size:.83rem;padding:4px 0;color:rgba(232,234,240,.75)">🪞 {sr}</div>', unsafe_allow_html=True)
#         with cc:
#             section_label("Teacher Observation")
#             for obs in ass["teacher_observation_points"]:
#                 st.checkbox(obs[:50]+"…" if len(obs)>50 else obs, key=f"to_{obs[:15]}")

#     with tabs[3]:
#         diff = pa["differentiation"]
#         ca, cb, cc = st.columns(3)
#         with ca:
#             section_label("Support Strategies")
#             for s in diff["support_strategies"]: st.markdown(f'<div style="font-size:.85rem;padding:3px 0">🤝 {s}</div>', unsafe_allow_html=True)
#         with cb:
#             section_label("Challenge Extensions")
#             for s in diff["challenge_extensions"]: st.markdown(f'<div style="font-size:.85rem;padding:3px 0">🚀 {s}</div>', unsafe_allow_html=True)
#         with cc:
#             section_label("Inclusion Accommodations")
#             for s in diff["inclusion_accommodations"]: st.markdown(f'<div style="font-size:.85rem;padding:3px 0">♿ {s}</div>', unsafe_allow_html=True)


# # ══════════════════════════════════════════════════════════════════════════════
# #  PROGRESS TRACKER
# # ══════════════════════════════════════════════════════════════════════════════
# def page_progress_tracker():
#     st.markdown("## 📈 Progress Tracker")

#     students = STUDENT_DATA["students"]
#     scores = STUDENT_DATA["progress_scores"]
#     logs = STUDENT_DATA["lesson_logs"]
#     coverage = STUDENT_DATA["curriculum_coverage"]

#     tabs = st.tabs(["👩‍🎓 Students", "📊 Class Overview", "📅 Lesson Logs", "🗺️ Curriculum Map"])

#     with tabs[0]:
#         selected_grade = st.selectbox("Filter by Grade", ["All Grades","Class 1","Class 2","Class 3","Class 4"])
#         filtered = students if selected_grade=="All Grades" else [s for s in students if s["class"]==selected_grade]

#         cols = st.columns(3)
#         for i, student in enumerate(filtered):
#             with cols[i % 3]:
#                 stu_scores = scores.get(student["id"], {})
#                 # Last score avg
#                 latest_avgs = [v[-1] for v in stu_scores.values() if v]
#                 avg = round(sum(latest_avgs)/len(latest_avgs)) if latest_avgs else 0
#                 trend = "↑" if avg >= 70 else ("→" if avg >= 55 else "↓")
#                 trend_col = "#10b981" if avg >= 70 else ("#f59e0b" if avg >= 55 else "#ef4444")
#                 grade_c = GRADE_COLORS.get(student["class"],"#aaa")
#                 st.markdown(f"""
# <div class="vd-student-card">
#   <div class="vd-avatar">{student['avatar']}</div>
#   <div style="flex:1">
#     <div class="vd-student-name">{html.escape(student['name'])}</div>
#     <div class="vd-student-meta">{badge(student['class'], grade_c)} Roll {student['roll']}</div>
#   </div>
#   <div style="text-align:right">
#     <div style="font-size:1.2rem;font-weight:700;color:{trend_col}">{avg}%</div>
#     <div style="font-size:.85rem;color:{trend_col}">{trend}</div>
#   </div>
# </div>""", unsafe_allow_html=True)

#                 with st.expander("View progress"):
#                     if stu_scores:
#                         weeks = ["Wk1","Wk2","Wk3","Wk4","Wk5"]
#                         for subject, s_scores in stu_scores.items():
#                             cols_prog = st.columns([2,1])
#                             with cols_prog[0]:
#                                 last = s_scores[-1]
#                                 pct_color = "#10b981" if last>=70 else ("#f59e0b" if last>=55 else "#ef4444")
#                                 st.markdown(f'<div style="font-size:.82rem;margin-bottom:2px">{subject}</div>', unsafe_allow_html=True)
#                                 st.markdown(progress_bar(last, pct_color), unsafe_allow_html=True)
#                             with cols_prog[1]:
#                                 st.markdown(f'<div style="font-size:.88rem;font-weight:700;color:{pct_color};text-align:right;margin-top:2px">{last}%</div>', unsafe_allow_html=True)
#                     if st.button("📝 Add Score", key=f"add_score_{student['id']}"):
#                         st.success("✅ Score added to tracker!")

#     with tabs[1]:
#         section_label("Class-wide performance overview")

#         # Grade performance bars
#         grade_avgs = {}
#         for g in ["Class 1","Class 2","Class 3","Class 4"]:
#             g_students = [s["id"] for s in students if s["class"]==g]
#             all_scores = []
#             for sid in g_students:
#                 for subj_scores in scores.get(sid,{}).values():
#                     all_scores.extend(subj_scores)
#             grade_avgs[g] = round(sum(all_scores)/len(all_scores)) if all_scores else 0

#         ca, cb = st.columns(2)
#         with ca:
#             section_label("Average Score by Grade")
#             for g, avg in grade_avgs.items():
#                 c = GRADE_COLORS.get(g,"#aaa")
#                 st.markdown(
#                     f'{badge(g,c)} <span style="font-size:.82rem;color:rgba(232,234,240,.6)">{avg}% average</span>'
#                     + progress_bar(avg, c),
#                     unsafe_allow_html=True
#                 )
#                 st.markdown("")

#         with cb:
#             section_label("Subject Performance (Class Average)")
#             subj_avgs = {}
#             for subj in ["Maths","English","EVS"]:
#                 all_s = [scores[sid][subj][-1] for sid in scores if subj in scores[sid]]
#                 subj_avgs[subj] = round(sum(all_s)/len(all_s)) if all_s else 0
#             subj_colors = {"Maths":"#3b82f6","English":"#10b981","EVS":"#f59e0b"}
#             for subj, avg in subj_avgs.items():
#                 c = subj_colors.get(subj,"#aaa")
#                 st.markdown(
#                     f'{badge(subj,c)} <span style="font-size:.82rem;color:rgba(232,234,240,.6)">{avg}% average</span>'
#                     + progress_bar(avg, c),
#                     unsafe_allow_html=True
#                 )
#                 st.markdown("")

#         section_label("Top Performers")
#         all_student_avgs = []
#         for s in students:
#             stu_s = scores.get(s["id"],{})
#             vals = [v[-1] for v in stu_s.values() if v]
#             avg = round(sum(vals)/len(vals)) if vals else 0
#             all_student_avgs.append((s,avg))
#         all_student_avgs.sort(key=lambda x: x[1], reverse=True)
#         top_cols = st.columns(3)
#         medals = ["🥇","🥈","🥉"]
#         for i,(s,avg) in enumerate(all_student_avgs[:3]):
#             c = GRADE_COLORS.get(s["class"],"#aaa")
#             with top_cols[i]:
#                 st.markdown(f"""
# <div class="vd-card" style="text-align:center">
#   <div style="font-size:1.8rem">{medals[i]}</div>
#   <div style="font-weight:600;margin-top:4px">{s['name']}</div>
#   <div>{badge(s['class'],c)}</div>
#   <div style="font-size:1.1rem;font-weight:700;color:#f5c842;margin-top:4px">{avg}%</div>
# </div>""", unsafe_allow_html=True)

#     with tabs[2]:
#         section_label("All lesson logs")
#         log_filter = st.selectbox("Filter by subject", ["All"]+["Mathematics","English","EVS","Science","Hindi"])
#         filtered_logs = logs if log_filter=="All" else [l for l in logs if l["subject"]==log_filter]

#         for log in reversed(filtered_logs):
#             subject_color = {"Mathematics":"#3b82f6","English":"#10b981","EVS":"#f59e0b","Science":"#8b5cf6","Hindi":"#ec4899"}.get(log["subject"],"#6b7280")
#             grades_html = " ".join([badge(g, GRADE_COLORS.get(g,"#aaa")) for g in log["grades"]])
#             comp_col = "#10b981" if log["completion"]==100 else ("#f59e0b" if log["completion"]>=80 else "#ef4444")
#             with st.expander(f"**{log['date']}** — {log['subject']} · {log['topic']}"):
#                 ca, cb = st.columns([2,1])
#                 with ca:
#                     st.markdown(f"**Topic:** {log['topic']}")
#                     st.markdown(f"**Grades:** {grades_html}", unsafe_allow_html=True)
#                     st.markdown(f"**Duration:** {log['duration']} minutes")
#                     st.markdown(f"**Notes:** _{log['notes']}_")
#                 with cb:
#                     st.metric("Completion", f"{log['completion']}%")
#                     if st.button("✏️ Edit Log", key=f"edit_{log['date']}_{log['topic'][:5]}"):
#                         st.success("✅ Log updated!")

#         if st.button("➕ Add New Lesson Log", type="primary"):
#             st.success("✅ New lesson log added to tracker!")

#     with tabs[3]:
#         section_label("Curriculum coverage map")
#         subject_sel = st.selectbox("Select Subject", list(coverage.keys()))
#         if subject_sel:
#             subj_coverage = coverage[subject_sel]
#             for cls, info in subj_coverage.items():
#                 c = GRADE_COLORS.get(cls,"#aaa")
#                 st.markdown(f"""
# <div style="margin-bottom:16px">
#   <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px">
#     {badge(cls,c)}
#     <span style="font-size:.85rem;color:rgba(232,234,240,.6)">{info['percent']}% complete</span>
#     {progress_bar(info['percent'],c)}
#   </div>
#   <div style="display:flex;flex-wrap:wrap;gap:4px;margin-bottom:6px">
# """, unsafe_allow_html=True)
#                 pills = ""
#                 for t in info["covered"]:
#                     pills += f'<span class="vd-topic-pill pill-done">✅ {t}</span>'
#                 for t in info["pending"]:
#                     pills += f'<span class="vd-topic-pill pill-pending">⏳ {t}</span>'
#                 st.markdown(pills + "</div></div>", unsafe_allow_html=True)


# # ══════════════════════════════════════════════════════════════════════════════
# #  NCERT EXPLORER
# # ══════════════════════════════════════════════════════════════════════════════
# def page_ncert_explorer():
#     st.markdown("## 📚 NCERT Curriculum Explorer")
#     st.markdown("Browse NCERT content for Classes 1–4 across all subjects.")

#     class_sel = st.selectbox("Select Class", list(NCERT_CURRICULUM.keys()))
#     if class_sel:
#         class_data = NCERT_CURRICULUM[class_sel]
#         subject_tabs = st.tabs(list(class_data.keys()))

#         for i, (subj, subj_data) in enumerate(class_data.items()):
#             with subject_tabs[i]:
#                 kpis = "".join([
#                     kpi_html("Chapters", len(subj_data["chapters"])),
#                     kpi_html("Topics", len(subj_data["topics"])),
#                     kpi_html("Key Concepts", len(subj_data["key_concepts"])),
#                 ])
#                 st.markdown(f"""
# <div class="vd-hero">
#   <div class="vd-hero-title">{html.escape(class_sel)} {html.escape(subj)}</div>
#   <div class="vd-hero-sub">NCERT curriculum content overview</div>
#   <div class="vd-kpis">{kpis}</div>
# </div>""", unsafe_allow_html=True)

#                 ca, cb, cc = st.columns(3)
#                 with ca:
#                     section_label("Chapters")
#                     for ch in subj_data["chapters"]:
#                         st.markdown(f'<div style="font-size:.87rem;padding:4px 0;border-bottom:1px solid rgba(255,255,255,.05)">📖 {ch}</div>', unsafe_allow_html=True)
#                 with cb:
#                     section_label("Topics Covered")
#                     for t in subj_data["topics"]:
#                         st.markdown(f'<div class="vd-topic-pill pill-done" style="margin-bottom:4px;display:flex">🏷️ {t}</div>', unsafe_allow_html=True)
#                 with cc:
#                     section_label("Key Concepts")
#                     for k in subj_data["key_concepts"]:
#                         st.markdown(f'<div style="font-size:.85rem;padding:3px 0">💡 {k}</div>', unsafe_allow_html=True)

#                 st.divider()
#                 if st.button(f"🚀 Generate Content for {class_sel} {subj}", key=f"gen_{class_sel}_{subj}"):
#                     st.success(f"✅ Redirecting to Course Planner with {class_sel} {subj} pre-loaded!")
#                     st.info("In full app: this would pre-fill the Course Planner with this subject's context.")


# # ══════════════════════════════════════════════════════════════════════════════
# #  MAIN
# # ══════════════════════════════════════════════════════════════════════════════
# def main():
#     inject_css()
#     page, grades, subjects, class_size, duration = render_sidebar()

#     page_key = page.split("  ", 1)[-1].strip().lower()

#     if "dashboard" in page_key:
#         page_dashboard()
#     elif "course" in page_key:
#         page_course_planner(grades, subjects, class_size, duration)
#     elif "activity" in page_key:
#         page_activity_generator(grades, subjects, class_size, duration)
#     elif "worksheet" in page_key:
#         page_worksheet_generator(grades, subjects, class_size, duration)
#     elif "assessment" in page_key:
#         page_assessment_generator(grades, subjects, class_size, duration)
#     elif "visual" in page_key:
#         page_visual_aids(grades, subjects, class_size, duration)
#     elif "peer" in page_key:
#         page_peer_activities(grades, subjects, class_size, duration)
#     elif "progress" in page_key:
#         page_progress_tracker()
#     elif "ncert" in page_key:
#         page_ncert_explorer()
#     else:
#         page_dashboard()


# if __name__ == "__main__":
#     main()


import streamlit as st
import html
from datetime import datetime

st.set_page_config(
    page_title="Vidyalaya AI — Multigrade Teaching Assistant",
    page_icon="🪔",
    layout="wide",
    initial_sidebar_state="expanded"
)

from hardcoded_data import (
    NCERT_CURRICULUM,
    TOPIC_COURSE_PLANS,
    TOPIC_WORKSHEETS,
    TOPIC_ASSESSMENTS,
    HARDCODED_VISUAL_AIDS,
    HARDCODED_PEER_ACTIVITIES,
    STUDENT_DATA,
    WEEKLY_SUMMARY,
    get_course_plan,
    get_worksheet,
    get_assessment,
)

# ─────────────────────────────────────────────────────────────
# CSS
# ─────────────────────────────────────────────────────────────
def inject_css():
    st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800&family=DM+Sans:wght@300;400;500;600&family=DM+Mono:wght@400;500&display=swap');

*, *::before, *::after { box-sizing: border-box; }
html, body, [data-testid="stAppViewContainer"] {
    background: #0f1117 !important; color: #e8eaf0 !important;
    font-family: 'DM Sans', sans-serif;
}
[data-testid="stSidebar"] {
    background: #13151f !important;
    border-right: 1px solid rgba(255,255,255,.07) !important;
}
.block-container { padding: 1.5rem 2rem 3rem !important; max-width: 1400px !important; }
#MainMenu, footer, header { visibility: hidden; }
[data-testid="stDecoration"], .stDeployButton { display: none; }

h1 { font-family: 'Playfair Display', serif !important; font-weight: 800 !important; font-size: 2rem !important; }
h2 { font-family: 'Playfair Display', serif !important; font-weight: 700 !important; font-size: 1.5rem !important; }
h3 { font-family: 'DM Sans', sans-serif !important; font-weight: 600 !important; font-size: 1.05rem !important; }

.sidebar-logo {
    font-family: 'Playfair Display', serif; font-size: 1.3rem; font-weight: 800;
    color: #f5c842; padding: .25rem 0 .75rem;
    border-bottom: 1px solid rgba(245,200,66,.2); margin-bottom: 1rem;
}
.sidebar-logo span {
    color: #e8eaf0; font-weight: 300; font-family: 'DM Sans', sans-serif;
    font-size: .82rem; display: block; margin-top: 2px;
}

div[data-testid="stRadio"] > label { display: none; }
div[data-testid="stRadio"] > div { gap: 3px !important; }
div[data-testid="stRadio"] > div > label {
    display: flex !important; align-items: center !important; gap: 10px !important;
    padding: 9px 13px !important; border-radius: 10px !important;
    border: 1px solid transparent !important; cursor: pointer !important;
    transition: all .15s !important; font-size: .93rem !important;
    font-weight: 500 !important; color: rgba(232,234,240,.72) !important;
    background: transparent !important; width: 100% !important;
}
div[data-testid="stRadio"] > div > label:hover {
    background: rgba(245,200,66,.07) !important;
    border-color: rgba(245,200,66,.15) !important; color: #f5c842 !important;
}
div[data-testid="stRadio"] > div > label[data-checked="true"],
div[data-testid="stRadio"] > div > label[aria-checked="true"] {
    background: rgba(245,200,66,.12) !important;
    border-color: rgba(245,200,66,.35) !important;
    color: #f5c842 !important; font-weight: 600 !important;
}

.stButton > button {
    background: linear-gradient(135deg, #f5c842, #e8a21a) !important;
    color: #0f1117 !important; font-family: 'DM Sans', sans-serif !important;
    font-weight: 600 !important; border: none !important; border-radius: 10px !important;
    padding: .52rem 1.3rem !important; cursor: pointer !important;
    transition: all .15s !important; box-shadow: 0 4px 14px rgba(245,200,66,.25) !important;
}
.stButton > button:hover { transform: translateY(-1px) !important; box-shadow: 0 6px 20px rgba(245,200,66,.35) !important; }
.stButton > button[kind="secondary"] {
    background: rgba(255,255,255,.06) !important; color: #e8eaf0 !important;
    border: 1px solid rgba(255,255,255,.12) !important; box-shadow: none !important;
}

.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stSelectbox > div > div {
    background: rgba(255,255,255,.05) !important;
    border: 1px solid rgba(255,255,255,.12) !important;
    border-radius: 10px !important; color: #e8eaf0 !important;
    font-family: 'DM Sans', sans-serif !important;
}
.stMultiSelect > div > div {
    background: rgba(255,255,255,.05) !important;
    border: 1px solid rgba(255,255,255,.12) !important; border-radius: 10px !important;
}
.stSlider > div > div > div { background: rgba(245,200,66,.3) !important; }
.stSlider > div > div > div > div { background: #f5c842 !important; }

.stExpander { border: 1px solid rgba(255,255,255,.08) !important; border-radius: 12px !important; background: rgba(255,255,255,.02) !important; margin-bottom: 5px !important; }

.stTabs [data-baseweb="tab-list"] { gap: 3px !important; background: rgba(255,255,255,.03) !important; border-radius: 12px !important; padding: 4px !important; border: 1px solid rgba(255,255,255,.07) !important; }
.stTabs [data-baseweb="tab"] { border-radius: 9px !important; padding: 7px 13px !important; font-family: 'DM Sans', sans-serif !important; font-weight: 500 !important; font-size: .88rem !important; color: rgba(232,234,240,.62) !important; border: none !important; background: transparent !important; }
.stTabs [aria-selected="true"] { background: rgba(245,200,66,.15) !important; color: #f5c842 !important; font-weight: 600 !important; }

[data-testid="stMetric"] { background: rgba(255,255,255,.04) !important; border: 1px solid rgba(255,255,255,.09) !important; border-radius: 14px !important; padding: 14px 16px !important; }
[data-testid="stMetricValue"] { font-size: 1.55rem !important; font-weight: 700 !important; color: #f5c842 !important; }
[data-testid="stMetricLabel"] { font-size: .78rem !important; opacity: .7 !important; text-transform: uppercase !important; }

hr { border-color: rgba(255,255,255,.07) !important; margin: 1.2rem 0 !important; }
.stProgress > div > div > div { background: linear-gradient(90deg, #f5c842, #e8a21a) !important; border-radius: 99px !important; }
.stProgress > div > div { background: rgba(255,255,255,.08) !important; border-radius: 99px !important; }

.vd-hero { background: linear-gradient(135deg, rgba(245,200,66,.08), rgba(232,162,26,.03), transparent); border: 1px solid rgba(245,200,66,.15); border-radius: 20px; padding: 22px 26px; margin-bottom: 18px; }
.vd-hero-title { font-family: 'Playfair Display', serif; font-size: 1.55rem; font-weight: 800; color: #f5c842; margin: 0 0 4px; line-height: 1.15; }
.vd-hero-sub { color: rgba(232,234,240,.68); font-size: .93rem; margin: 0 0 14px; }
.vd-kpis { display: flex; gap: 8px; flex-wrap: wrap; }
.vd-kpi { background: rgba(0,0,0,.25); border: 1px solid rgba(255,255,255,.10); border-radius: 12px; padding: 9px 15px; min-width: 110px; }
.vd-kpi-label { font-size: .63rem; letter-spacing: .12em; text-transform: uppercase; color: rgba(232,234,240,.48); margin-bottom: 3px; }
.vd-kpi-value { font-size: .98rem; font-weight: 700; color: #e8eaf0; }
.vd-kpi-sub { font-size: .70rem; color: rgba(232,234,240,.38); margin-top: 1px; }

.vd-card { background: rgba(255,255,255,.03); border: 1px solid rgba(255,255,255,.09); border-radius: 14px; padding: 14px 16px; margin-bottom: 8px; transition: border-color .15s; }
.vd-card:hover { border-color: rgba(245,200,66,.2); }
.vd-card-title { font-size: .97rem; font-weight: 600; margin: 0 0 4px; }
.vd-card-meta { font-size: .81rem; color: rgba(232,234,240,.58); }

.vd-badge { display: inline-flex; align-items: center; padding: 3px 10px; border-radius: 999px; font-size: .76rem; font-weight: 600; margin-right: 4px; margin-bottom: 3px; }
.vd-section-label { font-size: .68rem; font-weight: 600; letter-spacing: .12em; text-transform: uppercase; color: rgba(232,234,240,.48); margin-bottom: 7px; padding-left: 2px; }

.vd-grade-band { border-radius: 12px; padding: 12px 14px; margin-bottom: 8px; border-left: 4px solid; }
.g1 { background: rgba(16,185,129,.07); border-color: #10b981; }
.g2 { background: rgba(59,130,246,.07); border-color: #3b82f6; }
.g3 { background: rgba(245,158,11,.07); border-color: #f59e0b; }
.g4 { background: rgba(239,68,68,.07); border-color: #ef4444; }

.vd-q-card { background: rgba(255,255,255,.03); border: 1px solid rgba(255,255,255,.09); border-radius: 10px; padding: 11px 13px; margin-bottom: 6px; }
.vd-q-number { display: inline-flex; align-items: center; justify-content: center; width: 25px; height: 25px; background: rgba(245,200,66,.15); border-radius: 50%; font-size: .75rem; font-weight: 700; color: #f5c842; margin-right: 9px; flex-shrink: 0; }

.vd-rubric-cell { background: rgba(255,255,255,.04); border-radius: 7px; padding: 7px 9px; font-size: .79rem; }
.vd-rubric-exc { background: rgba(16,185,129,.12) !important; }
.vd-rubric-gd  { background: rgba(59,130,246,.10) !important; }
.vd-rubric-sat { background: rgba(245,158,11,.10) !important; }
.vd-rubric-ni  { background: rgba(239,68,68,.10) !important; }

.vd-progress-outer { background: rgba(255,255,255,.08); border-radius: 99px; height: 7px; margin-top: 4px; overflow: hidden; }
.vd-progress-inner { height: 100%; border-radius: 99px; background: linear-gradient(90deg, #f5c842, #e8a21a); transition: width .4s ease; }
.vd-topic-pill { display: inline-flex; align-items: center; gap: 4px; padding: 3px 9px; border-radius: 7px; font-size: .76rem; font-weight: 500; margin: 2px; }
.pill-done    { background: rgba(16,185,129,.15); color: #10b981; border: 1px solid rgba(16,185,129,.25); }
.pill-pending { background: rgba(239,68,68,.10);  color: rgba(239,68,68,.85); border: 1px solid rgba(239,68,68,.2); }
.pill-active  { background: rgba(245,200,66,.15); color: #f5c842; border: 1px solid rgba(245,200,66,.35); }

.vd-student-card { background: rgba(255,255,255,.03); border: 1px solid rgba(255,255,255,.09); border-radius: 13px; padding: 11px 13px; display: flex; align-items: center; gap: 10px; cursor: pointer; transition: all .15s; }
.vd-student-card:hover { border-color: rgba(245,200,66,.25); background: rgba(245,200,66,.04); }
.vd-highlight-item { display: flex; gap: 8px; align-items: flex-start; margin-bottom: 5px; font-size: .86rem; }
.vd-dot-green { width: 7px; height: 7px; border-radius: 50%; background: #10b981; margin-top: 5px; flex-shrink: 0; }
.vd-dot-amber { width: 7px; height: 7px; border-radius: 50%; background: #f59e0b; margin-top: 5px; flex-shrink: 0; }
.vd-dot-blue  { width: 7px; height: 7px; border-radius: 50%; background: #3b82f6; margin-top: 5px; flex-shrink: 0; }

.mg-time-label { background: rgba(245,200,66,.1); border-radius: 9px; padding: 10px 6px; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 90px; }
.mg-teacher-bar { background: rgba(245,200,66,.05); border: 1px solid rgba(245,200,66,.12); border-radius: 9px; padding: 8px 14px; font-size: .81rem; margin-top: 5px; margin-bottom: 10px; }
.mg-subject-chip { display: inline-flex; align-items: center; gap: 5px; padding: 4px 12px; border-radius: 8px; font-size: .80rem; font-weight: 600; background: rgba(245,200,66,.1); border: 1px solid rgba(245,200,66,.25); color: #f5c842; }

.topic-covered { background: rgba(16,185,129,.12); border: 1px solid rgba(16,185,129,.3); border-radius: 8px; padding: 5px 9px; margin-bottom: 3px; font-size: .81rem; display: flex; justify-content: space-between; align-items: center; }
.topic-pending { background: rgba(239,68,68,.07); border: 1px solid rgba(239,68,68,.2); border-radius: 8px; padding: 5px 9px; margin-bottom: 3px; font-size: .81rem; display: flex; justify-content: space-between; align-items: center; }
.coverage-wrap { background: rgba(255,255,255,.04); border-radius: 12px; padding: 12px 14px; margin-bottom: 8px; border: 1px solid rgba(255,255,255,.08); }

/* Sidebar step labels */
.sb-step { font-size: .72rem; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; color: #f5c842; margin-top: 12px; margin-bottom: 4px; opacity: .85; }
.sb-grade-topic { font-size: .76rem; font-weight: 700; margin-top: 5px; margin-bottom: 1px; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────
# CONSTANTS & HELPERS
# ─────────────────────────────────────────────────────────────
GRADE_COLORS = {"Class 1": "#10b981", "Class 2": "#3b82f6", "Class 3": "#f59e0b", "Class 4": "#ef4444"}
GRADE_CSS    = {"Class 1": "g1", "Class 2": "g2", "Class 3": "g3", "Class 4": "g4"}
ALL_GRADES   = ["Class 1", "Class 2", "Class 3", "Class 4"]

def hex_to_rgb(h):
    h = h.lstrip('#')
    return f"{int(h[0:2],16)},{int(h[2:4],16)},{int(h[4:6],16)}"

def badge(label, color="#f5c842", bg_alpha=0.15):
    rgb = hex_to_rgb(color)
    return (f'<span class="vd-badge" style="background:rgba({rgb},{bg_alpha});'
            f'color:{color};border:1px solid rgba({rgb},.3)">{html.escape(str(label))}</span>')

def kpi(label, value, sub=""):
    sub_html = f'<div class="vd-kpi-sub">{html.escape(str(sub))}</div>' if sub else ""
    return (f'<div class="vd-kpi"><div class="vd-kpi-label">{html.escape(str(label))}</div>'
            f'<div class="vd-kpi-value">{html.escape(str(value))}</div>{sub_html}</div>')

def slabel(text):
    st.markdown(f'<div class="vd-section-label">{html.escape(text)}</div>', unsafe_allow_html=True)

def pbar(pct, color="#f5c842"):
    return (f'<div class="vd-progress-outer"><div class="vd-progress-inner" '
            f'style="width:{pct}%;background:{color}"></div></div>')

def grade_badges_html(grades):
    return " ".join(badge(g, GRADE_COLORS.get(g, "#aaa")) for g in grades)

def _find_coverage(coverage, subject):
    for key in coverage:
        if subject.lower() in key.lower() or key.lower() in subject.lower():
            return coverage[key]
    return None

def _split_time(total, n):
    base, rem = divmod(total, n)
    slots = [base] * n
    for i in range(rem):
        slots[i] += 1
    return slots

def _slot_content(plan, slot_idx, topic):
    timeline = plan.get("timeline", [])
    if slot_idx < len(timeline):
        sl  = timeline[slot_idx]
        stu = sl.get("student_task", f"Work on {topic}")
        mat = ", ".join(plan.get("materials", ["Worksheet"])[:2])
        return {"student": stu[:90] + ("…" if len(stu) > 90 else ""), "materials": mat}
    return {"student": f"Continue {topic}", "materials": "Textbook, worksheet"}

def _teacher_roles(selected_grades, slot_names):
    n = len(selected_grades)
    roles = []
    for si, slot in enumerate(slot_names):
        if "Warm" in slot:
            roles.append("Lead whole-class warm-up — same subject, differentiated questions per grade cluster")
        elif "Direct" in slot:
            focus  = selected_grades[si % n]
            others = [g for g in selected_grades if g != focus]
            oth    = " & ".join(others) if others else "—"
            roles.append(f"Direct instruction with **{focus}** · {oth}: self-directed instruction cards")
        elif "Guided" in slot:
            roles.append(f"Rotate between clusters every ~{max(3, 8 // max(n, 1))} min · Table Monitors manage materials")
        elif "Independent" in slot or "Peer" in slot:
            roles.append("Circulate & observe · Target 1-on-1 support to students flagged in guided practice")
        else:
            roles.append("Collect exit tickets from all clusters · Grade-specific verbal feedback · Preview next topic")
    return roles


# ─────────────────────────────────────────────────────────────
# SIDEBAR
# New flow: (1) select grades → (2) one shared subject → (3) per-grade topic
# ─────────────────────────────────────────────────────────────
def render_sidebar():
    with st.sidebar:
        st.markdown(
            '<div class="sidebar-logo">🪔 Vidyalaya AI'
            '<span>Multigrade Teaching Assistant</span></div>',
            unsafe_allow_html=True
        )
        slabel("Navigation")
        page = st.radio("nav", [
            "🏠  Dashboard",
            "📅  Course Planner",
            "📝  Worksheet Generator",
            "📊  Assessment Generator",
            "🎨  Visual Aids",
            "🤝  Peer Activities",
            "📈  Progress Tracker",
            "📚  NCERT Explorer",
        ], label_visibility="collapsed")

        st.divider()

        # ── STEP 1 ─ Select grades ────────────────────────────
        st.markdown('<div class="sb-step">Step 1 — Select Grades</div>', unsafe_allow_html=True)
        selected_grades = st.multiselect(
            "grades", ALL_GRADES,
            default=["Class 1", "Class 2"],
            label_visibility="collapsed",
            help="All selected grades are taught at the same time."
        )
        if not selected_grades:
            st.warning("Please select at least one grade.")
            selected_grades = ["Class 1"]

        # Grade count pill
        n = len(selected_grades)
        grade_pill_html = " ".join(
            f'<span style="font-size:.72rem;padding:2px 8px;border-radius:6px;'
            f'background:rgba({hex_to_rgb(GRADE_COLORS.get(g,"#aaa"))},.15);'
            f'color:{GRADE_COLORS.get(g,"#aaa")};font-weight:700">{g.split()[-1]}</span>'
            for g in selected_grades
        )
        st.markdown(f'<div style="margin-top:3px">{grade_pill_html}</div>', unsafe_allow_html=True)

        # ── STEP 2 ─ One shared subject ───────────────────────
        st.markdown('<div class="sb-step">Step 2 — Shared Subject</div>', unsafe_allow_html=True)
        subject_sets    = [set(NCERT_CURRICULUM.get(g, {}).keys()) for g in selected_grades]
        common_subjects = sorted(set.intersection(*subject_sets)) if subject_sets else ["Mathematics"]
        if not common_subjects:
            common_subjects = list(NCERT_CURRICULUM.get(selected_grades[0], {}).keys())

        shared_subject = st.selectbox(
            "subject", common_subjects,
            label_visibility="collapsed",
            help="One subject taught to all grades simultaneously — each at their own level."
        )
        st.caption("Same subject · differentiated difficulty per grade")

        # ── STEP 3 ─ Per-grade topic within shared subject ────
        st.markdown('<div class="sb-step">Step 3 — Topic per Grade</div>', unsafe_allow_html=True)
        grade_topics = {}
        for g in selected_grades:
            c      = GRADE_COLORS.get(g, "#aaa")
            topics = NCERT_CURRICULUM.get(g, {}).get(shared_subject, {}).get("topics", ["Select topic"])
            st.markdown(
                f'<div class="sb-grade-topic" style="color:{c}">{g}</div>',
                unsafe_allow_html=True
            )
            grade_topics[g] = st.selectbox(
                f"topic_{g}", topics,
                key=f"topic_{g}",
                label_visibility="collapsed"
            )

        st.divider()
        st.markdown('<div class="sb-step">Session Settings</div>', unsafe_allow_html=True)
        class_size = st.slider("Total Class Size", 8, 60, 28)
        duration   = st.slider("Duration (min)",   20, 90, 45)

        st.divider()
        st.caption(f"📆 {datetime.now().strftime('%A, %d %b %Y')}")
        st.caption(f"🏫 {n} grade{'s' if n > 1 else ''} · {shared_subject}")

    return page.strip(), selected_grades, shared_subject, grade_topics, class_size, duration


# ─────────────────────────────────────────────────────────────
# DASHBOARD
# ─────────────────────────────────────────────────────────────
def page_dashboard(selected_grades, shared_subject, grade_topics):
    st.markdown("## 🏠 Teacher Dashboard")

    logs     = STUDENT_DATA["lesson_logs"]
    students = STUDENT_DATA["students"]
    coverage = STUDENT_DATA["curriculum_coverage"]

    # Active session banner
    topics_str = " · ".join(
        f'<b style="color:{GRADE_COLORS.get(g,"#aaa")}">{g.split()[-1]}:</b> {grade_topics[g]}'
        for g in selected_grades
    )
    st.markdown(
        f'<div style="padding:10px 16px;background:rgba(245,200,66,.06);border:1px solid '
        f'rgba(245,200,66,.15);border-radius:10px;margin-bottom:16px;font-size:.88rem">'
        f'<span class="mg-subject-chip">📚 {shared_subject}</span>'
        f'&nbsp;&nbsp;{grade_badges_html(selected_grades)}'
        f'&nbsp;&nbsp;<span style="color:rgba(232,234,240,.6)">{topics_str}</span></div>',
        unsafe_allow_html=True
    )

    c1, c2, c3, c4 = st.columns(4)
    active_stu = sum(1 for s in students if s["class"] in selected_grades)
    c1.metric("📚 Lessons This Month", len(logs),       "+3 vs last month")
    c2.metric("👩‍🎓 Active Students",  active_stu,      f"{len(selected_grades)} grade(s)")
    c3.metric("✅ Avg Completion",      "91%",           "+4% this week")
    # c4.metric("🌟 Top Performer",       "Meera Gupta",   "Class 4 · 98%")

    st.divider()
    left, right = st.columns([3, 2], gap="large")

    with left:
        st.markdown("### 📅 Recent Lesson Logs")
        slabel("Last 7 sessions")
        sc = {"Mathematics":"#3b82f6","English":"#10b981","EVS":"#f59e0b","Science":"#8b5cf6","Hindi":"#ec4899"}
        for log in logs[-7:]:
            cc = sc.get(log["subject"], "#6b7280")
            gs = grade_badges_html(log["grades"])
            co = "#10b981" if log["completion"]==100 else ("#f59e0b" if log["completion"]>=80 else "#ef4444")
            st.markdown(f"""
<div style="display:grid;grid-template-columns:72px 88px 1fr auto;align-items:center;
gap:10px;padding:8px 12px;border-radius:9px;background:rgba(255,255,255,.025);
border:1px solid rgba(255,255,255,.07);margin-bottom:4px;font-size:.85rem">
  <span style="font-family:'DM Mono',monospace;color:rgba(232,234,240,.45);font-size:.76rem">{log['date'][5:]}</span>
  <span style="color:{cc};font-weight:600;font-size:.82rem">{log['subject']}</span>
  <span style="color:rgba(232,234,240,.72)">{log['topic']} &nbsp;{gs}</span>
  <span style="color:{co};font-weight:700">{log['completion']}%</span>
</div>""", unsafe_allow_html=True)

    with right:
        st.markdown(f"### 📊 {shared_subject} Coverage")
        slabel("Selected grades — current topic progress")
        cov_subj = _find_coverage(coverage, shared_subject)
        for g in selected_grades:
            cov_g   = cov_subj.get(g, {}) if cov_subj else {}
            pct     = cov_g.get("percent", 0)
            c       = GRADE_COLORS.get(g, "#aaa")
            topic   = grade_topics.get(g, "")
            covered = topic in cov_g.get("covered", [])
            pc      = "pill-done" if covered else "pill-active"
            ic      = "✅" if covered else "▶"
            st.markdown(
                f'{badge(g,c)} '
                f'<span class="vd-topic-pill {pc}">{ic} {topic}</span>'
                f'<span style="font-size:.74rem;color:rgba(232,234,240,.45);margin-left:4px">{pct}%</span>'
                + pbar(pct, c),
                unsafe_allow_html=True
            )
            st.markdown("")

    st.divider()
    st.markdown("### 📋 Weekly Summary")
    ws   = WEEKLY_SUMMARY
    ca, cb, cc = st.columns(3)
    for col, dot, key, items in [
        (ca, "vd-dot-green", "✅ Highlights",       ws["highlights"]),
        (cb, "vd-dot-amber", "⚠️ Needs Attention",  ws["areas_for_improvement"]),
        (cc, "vd-dot-blue",  "📅 Next Week",         ws["next_week_focus"]),
    ]:
        with col:
            slabel(key)
            for h in items:
                st.markdown(
                    f'<div class="vd-highlight-item"><div class="{dot}"></div><span>{h}</span></div>',
                    unsafe_allow_html=True
                )


# ─────────────────────────────────────────────────────────────
# COURSE PLANNER  — integrated multigrade timeline, same subject
# ─────────────────────────────────────────────────────────────
def page_course_planner(selected_grades, shared_subject, grade_topics, class_size, duration):
    st.markdown("## 📅 Multigrade Course Planner")

    n = len(selected_grades)
    col1, col2 = st.columns([3, 2], gap="large")
    with col1:
        st.markdown(
            f'<div style="margin-bottom:10px"><span class="mg-subject-chip">📚 {shared_subject}</span>'
            f'&nbsp; <span style="font-size:.88rem">taught across <b>{n} grade{"s" if n>1 else ""}</b> simultaneously</span></div>',
            unsafe_allow_html=True
        )
        for g in selected_grades:
            c = GRADE_COLORS.get(g, "#aaa")
            st.markdown(
                f'{badge(g,c)} <span style="font-size:.88rem"><b>{shared_subject}</b> — {grade_topics[g]}</span>',
                unsafe_allow_html=True
            )
        st.text_area(
            "Custom notes for today (optional)",
            placeholder="e.g. Class 1 needs extra manipulative time; emphasise real-life word problems",
            height=68
        )
    with col2:
        per = class_size // max(n, 1)
        st.info(
            f"**Subject:** {shared_subject}\n\n"
            f"**Grades:** {', '.join(selected_grades)}\n\n"
            f"**Duration:** {duration} min · **Class:** {class_size} students\n\n"
            f"**~{per} students per grade cluster**"
        )

    if st.button("🚀 Generate Lesson Plan", type="primary", key="gen_plan"):
        with st.spinner("Building integrated lesson plan…"):
            import time; time.sleep(0.7)
        st.success(f"✅ Lesson plan ready — {n} grade{'s' if n>1 else ''}, {shared_subject}!")

    _render_plan_tabs(selected_grades, shared_subject, grade_topics, duration, class_size)


def _render_plan_tabs(selected_grades, shared_subject, grade_topics, duration, class_size):
    n     = len(selected_grades)
    plans = {g: get_course_plan(g, shared_subject, grade_topics[g]) for g in selected_grades}

    gb     = grade_badges_html(selected_grades)
    tot_s  = sum(1 for s in STUDENT_DATA["students"] if s["class"] in selected_grades)
    k_html = "".join([
        kpi("Subject",  shared_subject),
        kpi("Grades",   str(n)),
        kpi("Duration", f"{duration} min"),
        kpi("Students", str(tot_s), f"~{class_size//max(n,1)} per cluster"),
        kpi("Slots",    "5"),
    ])
    st.markdown(f"""
<div class="vd-hero">
  <div class="vd-hero-title">📅 {html.escape(shared_subject)} — Integrated Lesson</div>
  <div class="vd-hero-sub">{gb}</div>
  <div class="vd-kpis">{k_html}</div>
</div>""", unsafe_allow_html=True)

    tabs = st.tabs(["⏱️ Integrated Timeline", "🎯 Objectives & Materials",
                    "📊 Assessment Plan", "🔀 Differentiation & HW", "📋 Teacher Checklist"])

    # ── TAB 1  TIMELINE ──────────────────────────────────────
    with tabs[0]:
        slabel("Minute-by-minute — what every grade is doing at the same time")

        slot_names = ["Warm-up / Review", "Direct Instruction",
                      "Guided Practice", "Peer / Independent Work", "Exit & Wrap-up"]
        slot_mins  = _split_time(duration, 5)
        t_roles    = _teacher_roles(selected_grades, slot_names)

        elapsed = 0
        for si, (sname, smin) in enumerate(zip(slot_names, slot_mins)):
            time_lbl = f"{elapsed}–{elapsed+smin} min"
            elapsed += smin

            # Column headers on first row
            if si == 0:
                hcols = st.columns([1] + [2] * n)
                hcols[0].markdown(
                    '<div style="font-size:.64rem;font-weight:700;text-transform:uppercase;'
                    'letter-spacing:.1em;color:rgba(232,234,240,.3);padding:2px 0">TIME</div>',
                    unsafe_allow_html=True
                )
                for hi, g in enumerate(selected_grades):
                    c = GRADE_COLORS.get(g, "#aaa")
                    hcols[hi+1].markdown(
                        f'<div style="font-size:.74rem;font-weight:700;text-transform:uppercase;'
                        f'letter-spacing:.06em;color:{c};padding:2px 0">{g}</div>',
                        unsafe_allow_html=True
                    )

            rcols = st.columns([1] + [2] * n)
            with rcols[0]:
                st.markdown(f"""
<div class="mg-time-label">
  <div style="font-family:'DM Mono',monospace;color:#f5c842;font-size:.72rem;font-weight:700">{time_lbl}</div>
  <div style="font-size:.62rem;color:rgba(232,234,240,.35);margin-top:2px">{smin} min</div>
</div>""", unsafe_allow_html=True)

            for gi, g in enumerate(selected_grades):
                with rcols[gi+1]:
                    plan = plans[g]
                    c    = GRADE_COLORS.get(g, "#aaa")
                    css  = GRADE_CSS.get(g, "g1")
                    sc   = _slot_content(plan, si, grade_topics[g])
                    st.markdown(f"""
<div class="vd-grade-band {css}" style="min-height:88px;margin-bottom:0">
  <div style="font-size:.72rem;font-weight:700;color:{c};margin-bottom:4px">{sname}</div>
  <div style="font-size:.78rem;color:rgba(232,234,240,.85);line-height:1.45;margin-bottom:3px">
    🧑‍🎓 {html.escape(sc['student'])}
  </div>
  <div style="font-size:.71rem;color:rgba(232,234,240,.45)">
    📦 {html.escape(sc['materials'])}
  </div>
</div>""", unsafe_allow_html=True)

            st.markdown(
                f'<div class="mg-teacher-bar">👩‍🏫 <b style="color:#f5c842">Teacher</b>'
                f'&nbsp;→&nbsp;<span style="color:rgba(232,234,240,.80)">{t_roles[si]}</span></div>',
                unsafe_allow_html=True
            )

        # Classroom signals
        st.divider()
        slabel("Transition signals")
        sc_ = st.columns(4)
        for col, (sig, desc) in zip(sc_, [
            ("🔔 3 Claps",      "Whole class — freeze & look at teacher"),
            ("🔔 Bell Ring",    "Pencils down, 30-sec stretch"),
            ("🔄 2 Bell Rings", "Rotate to next activity / station"),
            ("✋ Hand Raise",   "Quiet signal — spreads across room"),
        ]):
            with col:
                st.markdown(f'<div class="vd-card"><div class="vd-card-title">{sig}</div>'
                             f'<div class="vd-card-meta">{desc}</div></div>', unsafe_allow_html=True)

    # ── TAB 2  OBJECTIVES ────────────────────────────────────
    with tabs[1]:
        slabel(f"Learning objectives and materials — {shared_subject}, each grade at their level")
        for g in selected_grades:
            plan      = plans[g]
            c         = GRADE_COLORS.get(g, "#aaa")
            css       = GRADE_CSS.get(g, "g1")
            stu_count = sum(1 for s in STUDENT_DATA["students"] if s["class"] == g)
            with st.expander(f"**{g}** — {shared_subject}: {grade_topics[g]}", expanded=True):
                ca, cb = st.columns(2)
                with ca:
                    st.markdown(f"""
<div class="vd-grade-band {css}">
  {badge(g, c)}
  <div style="font-size:.85rem;line-height:1.65;margin-top:8px"><b>Objectives:</b><br>{html.escape(plan['objectives'])}</div>
  <div style="margin-top:5px;font-size:.77rem;color:rgba(232,234,240,.45)">👩‍🎓 {stu_count} students</div>
</div>""", unsafe_allow_html=True)
                with cb:
                    st.markdown("**Materials needed:**")
                    for m in plan.get("materials", []):
                        st.markdown(f'<div style="font-size:.83rem;padding:2px 0">📦 {m}</div>', unsafe_allow_html=True)

        st.divider()
        slabel("Combined prep checklist")
        seen_mats = set()
        mat_cols  = st.columns(2)
        idx = 0
        for g in selected_grades:
            for m in plans[g].get("materials", []):
                key = f"[{g}] {m}"
                if key not in seen_mats:
                    seen_mats.add(key)
                    with mat_cols[idx % 2]:
                        st.checkbox(key, key=f"matck_{key[:28]}")
                    idx += 1

    # ── TAB 3  ASSESSMENT ────────────────────────────────────
    with tabs[2]:
        slabel(f"Grade-differentiated assessment — {shared_subject}")
        for g in selected_grades:
            plan  = plans[g]
            asmnt = get_assessment(g, shared_subject, grade_topics[g])
            c     = GRADE_COLORS.get(g, "#aaa")
            css   = GRADE_CSS.get(g, "g1")
            with st.expander(f"**{g}** — {grade_topics[g]}", expanded=False):
                ca, cb = st.columns(2)
                with ca:
                    slabel("Exit assessment")
                    st.markdown(
                        f'<div style="padding:10px 12px;background:rgba(245,200,66,.06);border-radius:9px;'
                        f'border:1px solid rgba(245,200,66,.15);font-size:.85rem;line-height:1.6">'
                        f'{html.escape(plan.get("assessment","See plan"))}</div>', unsafe_allow_html=True
                    )
                    slabel("Oral questions")
                    for i, oq in enumerate(asmnt.get("oral_questions", [])[:3], 1):
                        st.markdown(
                            f'<div class="vd-q-card"><span class="vd-q-number">{i}</span>'
                            f'<span style="font-size:.85rem">{html.escape(oq)}</span></div>',
                            unsafe_allow_html=True
                        )
                with cb:
                    slabel("Rubric")
                    rubric = asmnt.get("rubric", {})
                    for lvl, key, cls in [
                        ("⭐ Excellent",    "excellent",        "vd-rubric-exc"),
                        ("👍 Good",         "good",             "vd-rubric-gd"),
                        ("📝 Satisfactory", "satisfactory",     "vd-rubric-sat"),
                        ("⚠️ Needs Help",   "needs_improvement","vd-rubric-ni"),
                    ]:
                        desc = rubric.get(key, "See teacher guide")
                        st.markdown(
                            f'<div class="vd-rubric-cell {cls}" style="padding:9px 12px;margin-bottom:4px;border-radius:9px">'
                            f'<b>{lvl}:</b><br><span style="font-size:.78rem;font-weight:400">{html.escape(desc)}</span></div>',
                            unsafe_allow_html=True
                        )

        st.divider()
        slabel("Shared formative checks — run for all grades simultaneously")
        fc_cols = st.columns(3)
        for fc, (t, d) in zip(fc_cols, [
            ("🔁 Opening",    "Thumbs up/sideways/down — whole-class confidence check"),
            ("📝 Mid-lesson", "Sticky-note prompt: grade-appropriate card at each cluster"),
            ("📁 Portfolio",  "Student picks best work; teacher adds one written comment"),
        ]):
            with fc:
                st.markdown(f'<div class="vd-card"><div class="vd-card-title">{t}</div>'
                             f'<div class="vd-card-meta">{d}</div></div>', unsafe_allow_html=True)

    # ── TAB 4  DIFFERENTIATION ───────────────────────────────
    with tabs[3]:
        slabel("Support and extension — same subject, different levels")
        for g in selected_grades:
            plan = plans[g]
            css  = GRADE_CSS.get(g, "g1")
            with st.expander(f"**{g}** — {grade_topics[g]}", expanded=False):
                ca, cb, cc = st.columns(3)
                with ca:
                    st.markdown(
                        f'<div class="vd-rubric-cell vd-rubric-ni" style="border-radius:10px;padding:10px;height:100%">'
                        f'🤝 <b>Support</b><br><span style="font-size:.80rem;font-weight:400">'
                        f'{html.escape(plan["differentiation"]["support"])}</span></div>',
                        unsafe_allow_html=True
                    )
                with cb:
                    st.markdown(
                        f'<div class="vd-rubric-cell vd-rubric-exc" style="border-radius:10px;padding:10px;height:100%">'
                        f'🚀 <b>Advanced</b><br><span style="font-size:.80rem;font-weight:400">'
                        f'{html.escape(plan["differentiation"]["advanced"])}</span></div>',
                        unsafe_allow_html=True
                    )
                with cc:
                    st.markdown(
                        f'<div style="background:rgba(59,130,246,.07);border:1px solid rgba(59,130,246,.2);'
                        f'border-radius:10px;padding:10px;height:100%">'
                        f'📋 <b>Homework</b><br><span style="font-size:.80rem;font-weight:400">'
                        f'{html.escape(plan["homework"])}</span></div>',
                        unsafe_allow_html=True
                    )

        if n > 1:
            st.divider()
            slabel("Cross-grade management tips")
            tips = [
                ("🔄 Stagger tasks",    "Have extension cards ready so fast finishers don't disrupt other clusters."),
                ("👥 Peer mentoring",   "Pair advanced students with support students within the same grade first."),
                ("📌 Self-check cards", "Place answer keys face-down at each cluster for independent self-checking."),
                ("⏱️ Visible timer",    "A shared countdown visible to all grades reduces off-task behaviour."),
            ]
            tip_cols = st.columns(2)
            for i, (title, desc) in enumerate(tips):
                with tip_cols[i % 2]:
                    st.markdown(f'<div class="vd-card"><div class="vd-card-title">{title}</div>'
                                 f'<div class="vd-card-meta">{desc}</div></div>', unsafe_allow_html=True)

    # ── TAB 5  CHECKLIST ─────────────────────────────────────
    with tabs[4]:
        ca, cb = st.columns(2)
        with ca:
            slabel("Materials to prepare")
            seen = set()
            for g in selected_grades:
                for m in plans[g].get("materials", []):
                    key = f"[{g}] {m}"
                    if key not in seen:
                        seen.add(key)
                        st.checkbox(key, key=f"chk_{key[:28]}")
        with cb:
            slabel("Pre-lesson actions")
            for a in [
                "Arrange desks in colour-coded grade clusters",
                "Write each grade's objective on the board / mini-whiteboard",
                "Place materials tray at each cluster",
                "Brief Table Monitors — distribute & collect",
                "Prepare grade-differentiated instruction cards for independent slot",
                "Prepare extension cards for fast finishers",
                "Set visible countdown timer",
                "Place Help Needed signal cards (red/green) at each desk",
            ]:
                st.checkbox(a, key=f"pre_{a[:26]}")

        st.divider()
        lc, _ = st.columns([2, 3])
        with lc:
            if st.button("💾 Log Lesson as Taught", key="log_plan"):
                st.success(f"✅ Logged for {', '.join(selected_grades)} — {shared_subject}!")


# ─────────────────────────────────────────────────────────────
# WORKSHEET GENERATOR
# ─────────────────────────────────────────────────────────────
def page_worksheet_generator(selected_grades, shared_subject, grade_topics):
    st.markdown("## 📝 Multigrade Worksheet Generator")

    n = len(selected_grades)
    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown(f'<span class="mg-subject-chip">📚 {shared_subject}</span><br><br>',
                    unsafe_allow_html=True)
        st.markdown("**One worksheet per grade — same subject, levelled difficulty:**")
        for g in selected_grades:
            c = GRADE_COLORS.get(g, "#aaa")
            st.markdown(f'{badge(g,c)} <span style="font-size:.87rem">{grade_topics[g]}</span>',
                        unsafe_allow_html=True)
        include_ans = st.checkbox("Include Answer Key", value=False)
    with col2:
        st.info(
            f"**{n} worksheet{'s' if n > 1 else ''}** will be generated.\n\n"
            f"Each worksheet is tailored to its grade's topic within **{shared_subject}**.\n\n"
            f"Print and distribute one per grade cluster."
        )

    if st.button("📝 Generate All Worksheets", type="primary", key="gen_ws"):
        with st.spinner("Creating differentiated worksheets…"):
            import time; time.sleep(0.6)
        st.success(f"✅ {n} worksheet{'s' if n > 1 else ''} ready!")

    total_qs = sum(
        len(get_worksheet(g, shared_subject, grade_topics[g]).get("questions", []))
        for g in selected_grades
    )
    k_html = "".join([
        kpi("Subject",    shared_subject),
        kpi("Worksheets", str(n)),
        kpi("Total Qs",   str(total_qs)),
    ])
    st.markdown(f"""
<div class="vd-hero" style="padding:16px 22px;margin-bottom:14px">
  <div class="vd-hero-sub" style="margin-bottom:10px">{grade_badges_html(selected_grades)}</div>
  <div class="vd-kpis">{k_html}</div>
</div>""", unsafe_allow_html=True)

    if n == 1:
        _ws_single(selected_grades[0], shared_subject, grade_topics[selected_grades[0]], include_ans)
    else:
        grade_tabs = st.tabs([f"{g} — {grade_topics[g][:20]}" for g in selected_grades])
        for i, g in enumerate(selected_grades):
            with grade_tabs[i]:
                _ws_single(g, shared_subject, grade_topics[g], include_ans)


def _ws_single(g, subject, topic, include_ans):
    ws   = get_worksheet(g, subject, topic)
    c    = GRADE_COLORS.get(g, "#aaa")
    css  = GRADE_CSS.get(g, "g1")
    icons = {"fill_blank":"✏️","drawing":"🖼️","mcq":"🔘","short_answer":"✍️",
             "matching":"🔗","identification":"🔍"}

    k_html = "".join([
        kpi("Grade",     g),
        kpi("Topic",     topic[:18]+("…" if len(topic)>18 else "")),
        kpi("Questions", str(len(ws.get("questions", [])))),
    ])
    st.markdown(f"""
<div class="vd-grade-band {css}" style="margin-bottom:14px">
  {badge(g, c)} <span style="font-size:1rem;font-weight:700">{html.escape(ws['title'])}</span>
  <div class="vd-kpis" style="margin-top:10px">{k_html}</div>
</div>""", unsafe_allow_html=True)

    ws_tabs = st.tabs(["📋 Questions", "🔑 Answer Key"]) if include_ans else st.tabs(["📋 Questions"])
    with ws_tabs[0]:
        if ws.get("passage"):
            slabel("Reading Passage")
            st.markdown(
                f'<div style="padding:13px 15px;background:rgba(59,130,246,.06);border-radius:11px;'
                f'border:1px solid rgba(59,130,246,.15);font-size:.88rem;line-height:1.75;margin-bottom:14px">'
                f'{html.escape(ws["passage"])}</div>', unsafe_allow_html=True
            )
        for q in ws.get("questions", []):
            qtype = q.get("question_type", q.get("type", "short_answer"))
            icon  = icons.get(qtype, "❓")
            opts  = ""
            if q.get("options"):
                opts = '<div style="margin-top:5px;display:flex;flex-wrap:wrap;gap:4px">' + \
                       "".join(f'<span style="padding:2px 9px;border-radius:5px;background:rgba(255,255,255,.05);'
                               f'font-size:.76rem">{o}</span>' for o in q["options"]) + '</div>'
            st.markdown(f"""
<div class="vd-q-card">
  <div style="display:flex;align-items:flex-start">
    <span class="vd-q-number">{q['no']}</span>
    <div style="flex:1">
      <div style="font-size:.87rem;font-weight:600;margin-bottom:4px">{html.escape(q['q'])}</div>
      <span style="font-size:.71rem;padding:2px 7px;border-radius:5px;background:rgba(255,255,255,.06);
color:rgba(232,234,240,.55)">{icon} {qtype.replace('_',' ').title()}</span>
      {opts}
    </div>
  </div>
</div>""", unsafe_allow_html=True)

    if include_ans and len(ws_tabs) > 1:
        with ws_tabs[1]:
            slabel("Answer Key — Teacher Reference")
            for q in ws.get("questions", []):
                ans = q.get("answer", "See teacher guide")
                ac  = "#10b981" if str(ans) not in ["Varies","varies"] else "#f5c842"
                st.markdown(
                    f'<div style="padding:5px 0;font-size:.85rem;border-bottom:1px solid rgba(255,255,255,.05)">'
                    f'<b style="color:{ac}">Q{q["no"]}:</b> {html.escape(str(ans))}</div>',
                    unsafe_allow_html=True
                )

    if st.button("🖨️ Export", key=f"ws_exp_{g}_{topic[:8]}"):
        st.success(f"✅ {g} worksheet exported!")


# ─────────────────────────────────────────────────────────────
# ASSESSMENT GENERATOR
# ─────────────────────────────────────────────────────────────
def page_assessment_generator(selected_grades, shared_subject, grade_topics):
    st.markdown("## 📊 Multigrade Assessment Generator")

    n = len(selected_grades)
    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown(f'<span class="mg-subject-chip">📚 {shared_subject}</span><br><br>',
                    unsafe_allow_html=True)
        for g in selected_grades:
            c = GRADE_COLORS.get(g, "#aaa")
            st.markdown(f'{badge(g,c)} <span style="font-size:.87rem">{grade_topics[g]}</span>',
                        unsafe_allow_html=True)
        atype = st.selectbox("Assessment Type",
            ["Formative (in-class check)", "Summative (end of topic)", "Diagnostic (prior knowledge)"])
    with col2:
        st.info(
            f"Generates assessments for all **{n} grade{'s' if n>1 else ''}**.\n\n"
            f"Same subject (**{shared_subject}**), each grade assessed on their own topic and level."
        )

    if st.button("📊 Generate Assessment Plan", type="primary", key="gen_asmnt"):
        with st.spinner("Designing assessments…"):
            import time; time.sleep(0.6)
        st.success("✅ Assessment plan ready!")

    k_html = "".join([
        kpi("Subject", shared_subject),
        kpi("Grades",  str(n)),
        kpi("Type",    atype.split("(")[0].strip()),
    ])
    st.markdown(f"""
<div class="vd-hero">
  <div class="vd-hero-title">📊 {html.escape(shared_subject)} — Assessment Plan</div>
  <div class="vd-hero-sub">{grade_badges_html(selected_grades)} · {html.escape(atype)}</div>
  <div class="vd-kpis">{k_html}</div>
</div>""", unsafe_allow_html=True)

    if n == 1:
        _asmnt_single(selected_grades[0], shared_subject, grade_topics[selected_grades[0]], atype)
    else:
        grade_tabs = st.tabs([f"{g} — {grade_topics[g][:20]}" for g in selected_grades])
        for i, g in enumerate(selected_grades):
            with grade_tabs[i]:
                _asmnt_single(g, shared_subject, grade_topics[g], atype)

    st.divider()
    slabel("Shared formative checks — run for all grades simultaneously")
    fc_cols = st.columns(3)
    for fc, (t, d) in zip(fc_cols, [
        ("🔁 Opening",    "Thumbs up/sideways/down — whole-class confidence check"),
        ("📝 Mid-lesson", "Sticky-note exit: grade-appropriate prompt card per cluster"),
        ("📁 Portfolio",  "Student picks best work; teacher writes one positive + one growth comment"),
    ]):
        with fc:
            st.markdown(f'<div class="vd-card"><div class="vd-card-title">{t}</div>'
                         f'<div class="vd-card-meta">{d}</div></div>', unsafe_allow_html=True)


def _asmnt_single(g, subject, topic, atype):
    asmnt = get_assessment(g, subject, topic)
    c     = GRADE_COLORS.get(g, "#aaa")
    css   = GRADE_CSS.get(g, "g1")
    st.markdown(
        f'<div class="vd-grade-band {css}">{badge(g,c)}'
        f'<span style="font-weight:600;margin-left:8px">{subject} — {topic}</span></div>',
        unsafe_allow_html=True
    )
    a_tabs = st.tabs(["🗣️ Oral", "✍️ Written", "👁️ Observation", "📊 Rubric"])
    with a_tabs[0]:
        for i, q in enumerate(asmnt.get("oral_questions", [f"Explain {topic} in your own words."]) or [], 1):
            st.markdown(f'<div class="vd-q-card"><span class="vd-q-number">{i}</span>'
                        f'<span style="font-size:.87rem">{html.escape(q)}</span></div>',
                        unsafe_allow_html=True)
    with a_tabs[1]:
        wqs = asmnt.get("written_questions", [])
        if wqs:
            for i, q in enumerate(wqs, 1):
                st.markdown(f'<div class="vd-q-card"><span class="vd-q-number">{i}</span>'
                            f'<span style="font-size:.87rem">{html.escape(q)}</span></div>',
                            unsafe_allow_html=True)
        else:
            st.info("Use the Worksheet Generator for written questions on this topic.")
    with a_tabs[2]:
        for item in asmnt.get("observation_points", []):
            st.checkbox(item, key=f"obs_{g}_{topic[:8]}_{item[:14]}")
        st.divider()
        st.markdown('<div style="padding:10px 12px;background:rgba(255,255,255,.03);border-radius:9px;'
                    'border:1px solid rgba(255,255,255,.08);font-size:.85rem;font-style:italic">'
                    '🪞 "What was easy? What was hard? What do I still want to understand?"</div>',
                    unsafe_allow_html=True)
    with a_tabs[3]:
        rubric = asmnt.get("rubric", {})
        for lvl, key, cls in [
            ("⭐ Excellent",    "excellent",        "vd-rubric-exc"),
            ("👍 Good",         "good",             "vd-rubric-gd"),
            ("📝 Satisfactory", "satisfactory",     "vd-rubric-sat"),
            ("⚠️ Needs Help",   "needs_improvement","vd-rubric-ni"),
        ]:
            desc = rubric.get(key, "See teacher guide")
            st.markdown(
                f'<div class="vd-rubric-cell {cls}" style="padding:9px 13px;margin-bottom:4px;border-radius:9px">'
                f'<b>{lvl}:</b><br><span style="font-size:.79rem;font-weight:400">{html.escape(desc)}</span></div>',
                unsafe_allow_html=True
            )


# ─────────────────────────────────────────────────────────────
# VISUAL AIDS
# ─────────────────────────────────────────────────────────────
def page_visual_aids(selected_grades, shared_subject, grade_topics):
    st.markdown("## 🎨 Visual Aids Generator")
    col1, col2 = st.columns([3, 2])
    with col1:
        default_topic = " & ".join([grade_topics[g] for g in selected_grades[:2]])
        aid_topic = st.text_input("Visual Aid Topic", value=f"{shared_subject} — {default_topic}")
        aid_type  = st.selectbox("Aid Type", ["Interactive Wall Display","Poster","Chart","Diagram","Flashcards"])
    with col2:
        st.markdown(f'<div style="padding:12px 14px;background:rgba(255,255,255,.03);border-radius:10px;'
                    f'border:1px solid rgba(255,255,255,.08)">'
                    f'<b>Grades:</b> {grade_badges_html(selected_grades)}<br>'
                    f'<b>Subject:</b> {shared_subject}</div>', unsafe_allow_html=True)

    if st.button("🎨 Generate Visual Aid", type="primary", key="gen_va"):
        with st.spinner("Designing…"): import time; time.sleep(0.5)
        st.success("✅ Ready!")

    va    = HARDCODED_VISUAL_AIDS["default"]
    k_html = "".join([kpi("Type",aid_type), kpi("Grades",str(len(selected_grades))),
                      kpi("Materials",len(va["materials_needed"]))])
    st.markdown(f"""
<div class="vd-hero">
  <div class="vd-hero-title">🎨 {html.escape(aid_topic)}</div>
  <div class="vd-hero-sub">{grade_badges_html(selected_grades)}</div>
  <div class="vd-kpis">{k_html}</div>
</div>""", unsafe_allow_html=True)

    tabs = st.tabs(["🖼️ Design","👥 Grade Zones","📖 Usage","💻 Digital"])
    with tabs[0]:
        ca, cb = st.columns([3,2])
        d = va["content_description"]
        with ca:
            slabel("Main visual")
            st.markdown(f'<div style="font-size:.88rem;line-height:1.7;padding:11px;background:rgba(255,255,255,.03);'
                        f'border-radius:10px;border:1px solid rgba(255,255,255,.08)">'
                        f'{html.escape(d["main_visual"])}</div>', unsafe_allow_html=True)
        with cb:
            slabel("Materials")
            for m in va["materials_needed"]:
                st.markdown(f'<div style="font-size:.82rem;padding:2px 0">📦 {m}</div>', unsafe_allow_html=True)
    with tabs[1]:
        for ge in va["grade_specific_elements"]:
            grade = ge["grade"]
            if grade not in selected_grades: continue
            cg  = GRADE_COLORS.get(grade, "#aaa")
            css = GRADE_CSS.get(grade, "g1")
            with st.expander(f"**{grade}** Zone — {grade_topics.get(grade,'')}", expanded=True):
                st.markdown(f"""
<div class="vd-grade-band {css}">
  {badge(grade, cg)}
  <div style="margin-top:7px;font-size:.86rem"><b>Focus:</b> {html.escape(ge['visual_focus'])}</div>
  <div style="font-size:.86rem"><b>Interaction:</b> {html.escape(ge['interaction_method'])}</div>
</div>""", unsafe_allow_html=True)
    with tabs[2]:
        u = va["usage_instructions"]
        slabel("Setup")
        st.markdown(f'<div style="font-size:.88rem;line-height:1.65">{html.escape(u["setup"])}</div>', unsafe_allow_html=True)
        slabel("Intro script")
        st.markdown(f'<div style="padding:11px 13px;background:rgba(245,200,66,.06);border-radius:10px;'
                    f'border:1px solid rgba(245,200,66,.15);font-size:.87rem;font-style:italic">'
                    f'💬 "{html.escape(u["introduction_script"])}"</div>', unsafe_allow_html=True)
    with tabs[3]:
        for d2 in va["digital_alternatives"]:
            with st.expander(f"💻 {d2['platform']}"):
                st.markdown(d2["description"])
                for f2 in d2["accessibility_features"]:
                    st.markdown(f'<div style="font-size:.82rem">♿ {f2}</div>', unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
# PEER ACTIVITIES
# ─────────────────────────────────────────────────────────────
def page_peer_activities(selected_grades, shared_subject, grade_topics, class_size):
    st.markdown("## 🤝 Peer Activity Generator")
    col1, col2 = st.columns([3, 2])
    with col1:
        default_t = " & ".join([grade_topics[g] for g in selected_grades[:2]])
        collab_topic = st.text_input("Collaboration Topic", value=f"Cross-Grade {shared_subject} — {default_t}")
        collab_type  = st.selectbox("Type", ["Mixed Groups with Role Rotation","Buddy System","Mentoring Pairs"])
    with col2:
        st.markdown(f'<div style="padding:12px 14px;background:rgba(255,255,255,.03);border-radius:10px;'
                    f'border:1px solid rgba(255,255,255,.08)">'
                    f'<b>Grades:</b> {grade_badges_html(selected_grades)}<br>'
                    f'<b>Class size:</b> {class_size}</div>', unsafe_allow_html=True)

    if st.button("🤝 Generate Activity", type="primary", key="gen_pa"):
        with st.spinner("…"): import time; time.sleep(0.5)
        st.success("✅ Ready!")

    pa = HARDCODED_PEER_ACTIVITIES["default"]
    gs = pa["grouping_strategy"]
    k_html = "".join([kpi("Grades",str(len(selected_grades))),kpi("Duration",f"{pa['duration']} min"),
                      kpi("Stations",len(pa["activity_stations"]))])
    st.markdown(f"""
<div class="vd-hero">
  <div class="vd-hero-title">🤝 {html.escape(collab_topic)}</div>
  <div class="vd-hero-sub">{grade_badges_html(selected_grades)}</div>
  <div class="vd-kpis">{k_html}</div>
</div>""", unsafe_allow_html=True)

    tabs = st.tabs(["👥 Groups","🏫 Stations","🪞 Assessment","🌈 Differentiation"])
    with tabs[0]:
        ca, cb = st.columns(2)
        with ca:
            slabel("Grouping")
            for k2, v in gs.items():
                if k2 != "pairing_criteria":
                    st.markdown(f'<div style="font-size:.86rem;padding:3px 0">• <b>{k2.replace("_"," ").title()}:</b> {v}</div>', unsafe_allow_html=True)
        with cb:
            slabel("Roles for selected grades")
            for role in pa["role_definitions"]:
                relevant = [g for g in role["suitable_grades"] if g in selected_grades]
                if not relevant: continue
                with st.expander(f"**{role['role_name']}**"):
                    st.markdown(grade_badges_html(relevant), unsafe_allow_html=True)
                    ra, rb = st.columns(2)
                    with ra:
                        st.markdown("**Responsibilities**")
                        for r in role["responsibilities"]:
                            st.markdown(f'<div style="font-size:.81rem">• {r}</div>', unsafe_allow_html=True)
                    with rb:
                        st.markdown("**Skills Built**")
                        for s in role["skills_developed"]:
                            st.markdown(f'<div style="font-size:.81rem">🌱 {s}</div>', unsafe_allow_html=True)
    with tabs[1]:
        for stn in pa["activity_stations"]:
            with st.expander(f"**{stn['station_name']}** — {stn['time_allocation']} min"):
                ra, rb = st.columns(2)
                i2 = stn["instructions"]
                with ra:
                    st.markdown(f'<div style="padding:8px 11px;background:rgba(245,200,66,.06);border-radius:9px;'
                                f'border:1px solid rgba(245,200,66,.15);font-size:.83rem">'
                                f'<b style="color:#f5c842">👩‍🏫 Mentor:</b><br>{html.escape(i2["mentor_guide"])}</div>',
                                unsafe_allow_html=True)
                with rb:
                    st.markdown(f'<div style="padding:8px 11px;background:rgba(59,130,246,.06);border-radius:9px;'
                                f'border:1px solid rgba(59,130,246,.15);font-size:.83rem">'
                                f'<b style="color:#3b82f6">📝 Learners:</b><br>{html.escape(i2["learner_tasks"])}</div>',
                                unsafe_allow_html=True)
    with tabs[2]:
        ass = pa["assessment_strategies"]
        ra, rb, rc = st.columns(3)
        with ra:
            slabel("Peer Feedback")
            for pf in ass["peer_feedback_forms"]:
                st.text_area("", placeholder=pf, height=68, key=f"pf_{pf[:12]}", label_visibility="collapsed")
        with rb:
            slabel("Self Reflection")
            for sr in ass["self_reflection_prompts"]:
                st.markdown(f'<div style="font-size:.81rem;padding:3px 0">🪞 {sr}</div>', unsafe_allow_html=True)
        with rc:
            slabel("Teacher Observation")
            for obs in ass["teacher_observation_points"]:
                st.checkbox(obs[:48]+("…" if len(obs)>48 else ""), key=f"to_{obs[:12]}")
    with tabs[3]:
        diff = pa["differentiation"]
        ra, rb, rc = st.columns(3)
        with ra:
            slabel("Support")
            for s in diff["support_strategies"]:
                st.markdown(f'<div style="font-size:.83rem;padding:2px 0">🤝 {s}</div>', unsafe_allow_html=True)
        with rb:
            slabel("Challenge")
            for s in diff["challenge_extensions"]:
                st.markdown(f'<div style="font-size:.83rem;padding:2px 0">🚀 {s}</div>', unsafe_allow_html=True)
        with rc:
            slabel("Inclusion")
            for s in diff["inclusion_accommodations"]:
                st.markdown(f'<div style="font-size:.83rem;padding:2px 0">♿ {s}</div>', unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
# PROGRESS TRACKER
# ─────────────────────────────────────────────────────────────
def page_progress_tracker(selected_grades, shared_subject, grade_topics):
    st.markdown("## 📈 Progress Tracker")
    students   = STUDENT_DATA["students"]
    scores     = STUDENT_DATA["progress_scores"]
    topic_prog = STUDENT_DATA["topic_progress"]
    coverage   = STUDENT_DATA["curriculum_coverage"]
    logs       = STUDENT_DATA["lesson_logs"]

    tabs = st.tabs(["🗺️ Topic Coverage", "👩‍🎓 Students", "📊 Class Overview", "📅 Lesson Logs"])

    # ── TOPIC COVERAGE ────────────────────────────────────────
    with tabs[0]:
        st.markdown(f"### 🗺️ {shared_subject} — Topic Coverage by Grade")
        cov_subj = _find_coverage(coverage, shared_subject)

        for g in selected_grades:
            c       = GRADE_COLORS.get(g, "#aaa")
            cov_g   = cov_subj.get(g, {}) if cov_subj else {}
            pct     = cov_g.get("percent", 0)
            covered = cov_g.get("covered", [])
            pending = cov_g.get("pending", [])
            current = grade_topics.get(g, "")

            st.markdown(f"""
<div class="coverage-wrap">
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">
    <div>{badge(g,c)} <span style="font-weight:700">{shared_subject}</span></div>
    <div style="font-size:1.35rem;font-weight:800;color:{c}">{pct}%</div>
  </div>
  {pbar(pct, c)}
  <div style="display:flex;gap:14px;margin-top:6px;font-size:.76rem;color:rgba(232,234,240,.5)">
    <span>✅ {len(covered)} covered</span>
    <span>⏳ {len(pending)} pending</span>
    <span>▶ Current: <b style="color:{c}">{current}</b></span>
  </div>
</div>""", unsafe_allow_html=True)

            ca, cb = st.columns(2)
            stu_g  = [s for s in students if s["class"] == g]
            with ca:
                slabel("✅ Covered")
                for t in covered:
                    is_cur   = (t == current)
                    border   = f"border:2px solid {c};" if is_cur else ""
                    mastered = sum(1 for s in stu_g
                                   if topic_prog.get(s["id"],{}).get(shared_subject,{}).get(t, False))
                    st.markdown(
                        f'<div class="topic-covered" style="{border}">✅ {t}'
                        f'{"  👈 current" if is_cur else ""}'
                        f'<span style="font-size:.73rem;color:#10b981;font-weight:600">'
                        f'{mastered}/{len(stu_g)}</span></div>',
                        unsafe_allow_html=True
                    )
            with cb:
                slabel("⏳ Pending")
                for t in pending:
                    is_cur  = (t == current)
                    border  = f"border:2px solid {c};" if is_cur else ""
                    started = sum(1 for s in stu_g
                                  if topic_prog.get(s["id"],{}).get(shared_subject,{}).get(t, False))
                    st.markdown(
                        f'<div class="topic-pending" style="{border}">⏳ {t}'
                        f'{"  👈 current" if is_cur else ""}'
                        f'<span style="font-size:.73rem;color:rgba(239,68,68,.85);font-weight:600">'
                        f'{started}/{len(stu_g)} started</span></div>',
                        unsafe_allow_html=True
                    )

            all_t = covered + pending
            mc1, mc2 = st.columns([3, 1])
            with mc1:
                mk = st.selectbox(f"Mark as taught ({g})", all_t,
                                  index=all_t.index(current) if current in all_t else 0,
                                  key=f"mk_{g}")
            with mc2:
                st.markdown('<div style="height:27px"></div>', unsafe_allow_html=True)
                if st.button("✅ Mark", key=f"mk_btn_{g}"):
                    st.success(f"✅ '{mk}' marked for {g}!")
            st.markdown("")

    # ── STUDENTS ──────────────────────────────────────────────
    with tabs[1]:
        gf       = st.selectbox("Filter", ["All Selected Grades"] + selected_grades, key="stu_filter")
        filtered = ([s for s in students if s["class"] in selected_grades]
                    if gf == "All Selected Grades"
                    else [s for s in students if s["class"] == gf])

        cols3 = st.columns(3)
        for i, stu in enumerate(filtered):
            with cols3[i % 3]:
                ss    = scores.get(stu["id"], {})
                avgs  = [v[-1] for v in ss.values() if v]
                avg   = round(sum(avgs)/len(avgs)) if avgs else 0
                tc    = "#10b981" if avg >= 70 else ("#f59e0b" if avg >= 55 else "#ef4444")
                gc    = GRADE_COLORS.get(stu["class"], "#aaa")
                st.markdown(f"""
<div class="vd-student-card">
  <div style="font-size:1.75rem">{stu['avatar']}</div>
  <div style="flex:1">
    <div style="font-weight:600;font-size:.91rem">{html.escape(stu['name'])}</div>
    <div style="font-size:.77rem;color:rgba(232,234,240,.52)">{badge(stu['class'],gc)} Roll {stu['roll']}</div>
  </div>
  <div style="text-align:right">
    <div style="font-size:1.1rem;font-weight:700;color:{tc}">{avg}%</div>
    <div style="font-size:.80rem;color:{tc}">{"↑" if avg>=70 else ("→" if avg>=55 else "↓")}</div>
  </div>
</div>""", unsafe_allow_html=True)
                with st.expander(f"📊 {stu['name'].split()[0]}"):
                    for subj, s_sc in ss.items():
                        last = s_sc[-1]
                        pc   = "#10b981" if last>=70 else ("#f59e0b" if last>=55 else "#ef4444")
                        sc1, sc2 = st.columns([3,1])
                        with sc1:
                            st.markdown(f'<div style="font-size:.78rem;margin-bottom:1px">{subj}</div>', unsafe_allow_html=True)
                            st.markdown(pbar(last, pc), unsafe_allow_html=True)
                        with sc2:
                            st.markdown(f'<div style="font-size:.83rem;font-weight:700;color:{pc};text-align:right;margin-top:2px">{last}%</div>', unsafe_allow_html=True)
                    tp = topic_prog.get(stu["id"],{}).get(shared_subject,{})
                    if tp:
                        st.markdown('<div style="margin-top:6px"></div>', unsafe_allow_html=True)
                        slabel(f"{shared_subject} topics")
                        done  = sum(1 for v in tp.values() if v)
                        total = len(tp)
                        st.markdown(
                            f'<span style="font-size:.78rem;color:rgba(232,234,240,.5)">{done}/{total}</span>'
                            + pbar(round(done/total*100) if total else 0, GRADE_COLORS.get(stu["class"],"#aaa")),
                            unsafe_allow_html=True
                        )

    # ── CLASS OVERVIEW ────────────────────────────────────────
    with tabs[2]:
        slabel("Performance across selected grades")
        ca, cb = st.columns(2)
        with ca:
            slabel("Average score by grade")
            for g in selected_grades:
                g_ids  = [s["id"] for s in students if s["class"] == g]
                all_sc = [v for sid in g_ids for sv in scores.get(sid,{}).values() for v in sv]
                avg    = round(sum(all_sc)/len(all_sc)) if all_sc else 0
                c      = GRADE_COLORS.get(g,"#aaa")
                st.markdown(f'{badge(g,c)} <span style="font-size:.78rem;color:rgba(232,234,240,.55)">{avg}%</span>'
                            + pbar(avg, c), unsafe_allow_html=True)
                st.markdown("")
        with cb:
            slabel("Top performers")
            avgs_l = []
            for s in students:
                if s["class"] not in selected_grades: continue
                vals = [v[-1] for v in scores.get(s["id"],{}).values() if v]
                avgs_l.append((s, round(sum(vals)/len(vals)) if vals else 0))
            avgs_l.sort(key=lambda x:x[1], reverse=True)
            for i, (s, av) in enumerate(avgs_l[:3]):
                c = GRADE_COLORS.get(s["class"],"#aaa")
                st.markdown(f"""
<div class="vd-card" style="display:flex;align-items:center;gap:10px;padding:9px 13px;margin-bottom:5px">
  <span style="font-size:1.35rem">{"🥇🥈🥉"[i]}</span>
  <span style="font-size:1.1rem">{s['avatar']}</span>
  <div><div style="font-weight:600;font-size:.90rem">{s['name']}</div><div>{badge(s['class'],c)}</div></div>
  <div style="margin-left:auto;font-size:1.05rem;font-weight:700;color:#f5c842">{av}%</div>
</div>""", unsafe_allow_html=True)

    # ── LESSON LOGS ───────────────────────────────────────────
    with tabs[3]:
        lf1 = st.selectbox("Subject filter", ["All","Mathematics","English","EVS","Science","Hindi"], key="lf1")
        lf2 = st.selectbox("Grade filter",   ["All Selected"] + selected_grades, key="lf2")

        fl = [l for l in logs if (lf1 == "All" or l["subject"] == lf1)]
        fl = [l for l in fl if (lf2 == "All Selected" and any(g in l["grades"] for g in selected_grades))
              or (lf2 != "All Selected" and lf2 in l["grades"])]

        sc2 = {"Mathematics":"#3b82f6","English":"#10b981","EVS":"#f59e0b","Science":"#8b5cf6","Hindi":"#ec4899"}
        for log in reversed(fl):
            cc2 = sc2.get(log["subject"],"#6b7280")
            gh  = grade_badges_html(log["grades"])
            co  = "#10b981" if log["completion"]==100 else ("#f59e0b" if log["completion"]>=80 else "#ef4444")
            with st.expander(f"**{log['date']}** — {log['subject']} · {log['topic']}"):
                ca2, cb2 = st.columns([2,1])
                with ca2:
                    st.markdown(f"**Topic:** {log['topic']}")
                    st.markdown(f"**Grades:** {gh}", unsafe_allow_html=True)
                    st.markdown(f"**Duration:** {log['duration']} min")
                    st.markdown(f"**Notes:** _{log['notes']}_")
                with cb2:
                    st.metric("Completion", f"{log['completion']}%")

        if st.button("➕ Add New Log", type="primary", key="add_log"):
            st.success("✅ New log added!")


# ─────────────────────────────────────────────────────────────
# NCERT EXPLORER
# ─────────────────────────────────────────────────────────────
def page_ncert_explorer(selected_grades, shared_subject, grade_topics):
    st.markdown("## 📚 NCERT Curriculum Explorer")
    st.markdown("Browse all curriculum content. Active grades & topics are highlighted.")

    class_sel  = st.selectbox(
        "Class", list(NCERT_CURRICULUM.keys()),
        index=list(NCERT_CURRICULUM.keys()).index(selected_grades[0]) if selected_grades else 0
    )
    class_data = NCERT_CURRICULUM[class_sel]
    subj_tabs  = st.tabs(list(class_data.keys()))

    for i, (subj, subj_data) in enumerate(class_data.items()):
        with subj_tabs[i]:
            is_active    = class_sel in selected_grades and subj == shared_subject
            active_topic = grade_topics.get(class_sel, "") if is_active else None
            c = GRADE_COLORS.get(class_sel, "#aaa")

            active_pill = (
                f'&nbsp;<span style="font-size:.74rem;padding:3px 9px;'
                f'background:rgba(245,200,66,.15);border-radius:6px;color:#f5c842">▶ Active</span>'
            ) if is_active else ""

            k_html = "".join([
                kpi("Chapters", len(subj_data["chapters"])),
                kpi("Topics",   len(subj_data["topics"])),
                kpi("Concepts", len(subj_data["key_concepts"])),
            ])
            st.markdown(f"""
<div class="vd-hero">
  <div class="vd-hero-title">{html.escape(class_sel)} — {html.escape(subj)} {active_pill}</div>
  <div class="vd-hero-sub">NCERT curriculum reference</div>
  <div class="vd-kpis">{k_html}</div>
</div>""", unsafe_allow_html=True)

            cov_subj2 = _find_coverage(STUDENT_DATA["curriculum_coverage"], subj)
            covered_t = cov_subj2.get(class_sel,{}).get("covered",[]) if cov_subj2 else []

            ca, cb, cc = st.columns(3)
            with ca:
                slabel("Chapters")
                for ch in subj_data["chapters"]:
                    st.markdown(f'<div style="font-size:.83rem;padding:4px 0;border-bottom:1px solid rgba(255,255,255,.05)">📖 {ch}</div>',
                                unsafe_allow_html=True)
            with cb:
                slabel("Topics")
                for t in subj_data["topics"]:
                    is_cov = t in covered_t
                    is_cur = t == active_topic
                    pc = "pill-done" if is_cov else ("pill-active" if is_cur else "pill-pending")
                    ic = "✅" if is_cov else ("▶" if is_cur else "⏳")
                    st.markdown(f'<span class="vd-topic-pill {pc}" style="display:inline-flex;margin-bottom:3px">'
                                f'{ic} {t}</span>', unsafe_allow_html=True)
            with cc:
                slabel("Key Concepts")
                for k in subj_data["key_concepts"]:
                    st.markdown(f'<div style="font-size:.82rem;padding:2px 0">💡 {k}</div>', unsafe_allow_html=True)

            st.divider()
            if st.button(f"🚀 Use {class_sel} {subj} in Planner", key=f"use_{class_sel}_{subj}"):
                st.success(f"Set sidebar to {class_sel} + {subj}, then go to Course Planner!")


# ─────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────
def main():
    inject_css()
    page, selected_grades, shared_subject, grade_topics, class_size, duration = render_sidebar()
    pk = page.split("  ", 1)[-1].strip().lower()

    if   "dashboard"  in pk: page_dashboard(selected_grades, shared_subject, grade_topics)
    elif "course"     in pk: page_course_planner(selected_grades, shared_subject, grade_topics, class_size, duration)
    elif "worksheet"  in pk: page_worksheet_generator(selected_grades, shared_subject, grade_topics)
    elif "assessment" in pk: page_assessment_generator(selected_grades, shared_subject, grade_topics)
    elif "visual"     in pk: page_visual_aids(selected_grades, shared_subject, grade_topics)
    elif "peer"       in pk: page_peer_activities(selected_grades, shared_subject, grade_topics, class_size)
    elif "progress"   in pk: page_progress_tracker(selected_grades, shared_subject, grade_topics)
    elif "ncert"      in pk: page_ncert_explorer(selected_grades, shared_subject, grade_topics)
    else:                    page_dashboard(selected_grades, shared_subject, grade_topics)


if __name__ == "__main__":
    main()