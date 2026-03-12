
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
#MainMenu, footer { visibility: hidden; }
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
    clean_ws_text = lambda s: str(s).replace("</div>", "").strip()

    k_html = "".join([
        kpi("Grade",     g),
        kpi("Topic",     topic[:18]+("…" if len(topic)>18 else "")),
        kpi("Questions", str(len(ws.get("questions", [])))),
    ])
    st.markdown(f"""
<div class="vd-grade-band {css}" style="margin-bottom:14px">
  {badge(g, c)} <span style="font-size:1rem;font-weight:700">{html.escape(clean_ws_text(ws['title']))}</span>
  <div class="vd-kpis" style="margin-top:10px">{k_html}</div>
</div>""", unsafe_allow_html=True)

    ws_tabs = st.tabs(["📋 Questions", "🔑 Answer Key"]) if include_ans else st.tabs(["📋 Questions"])
    with ws_tabs[0]:
        if ws.get("passage"):
            slabel("Reading Passage")
            st.markdown(
                f'<div style="padding:13px 15px;background:rgba(59,130,246,.06);border-radius:11px;'
                f'border:1px solid rgba(59,130,246,.15);font-size:.88rem;line-height:1.75;margin-bottom:14px">'
                f'{html.escape(clean_ws_text(ws["passage"]))}</div>', unsafe_allow_html=True
            )
        for q in ws.get("questions", []):
            qtype = q.get("question_type", q.get("type", "short_answer"))
            icon  = icons.get(qtype, "❓")
            opts  = ""
            if q.get("options"):
                opts = '<div style="margin-top:5px;display:flex;flex-wrap:wrap;gap:4px">' + \
                       "".join(f'<span style="padding:2px 9px;border-radius:5px;background:rgba(255,255,255,.05);'
                               f'font-size:.76rem">{clean_ws_text(o)}</span>' for o in q["options"]) + '</div>'
            st.markdown(f"""
<div class="vd-q-card">
  <div style="display:flex;align-items:flex-start">
    <span class="vd-q-number">{q['no']}</span>
    <div style="flex:1">
      <div style="font-size:.87rem;font-weight:600;margin-bottom:4px">{html.escape(clean_ws_text(q['q']))}</div>
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
                    f'<b style="color:{ac}">Q{q["no"]}:</b> {html.escape(clean_ws_text(ans))}</div>',
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
