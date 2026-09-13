import os
import html
import requests
import streamlit as st
import google.generativeai as genai
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title="Vimarsh Jaiswal | AI/ML & Full-Stack Developer",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -----------------------------
# Theme / global styling
# -----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap');

:root {
  --bg:#06111d;
  --panel:#0b1a2a;
  --panel2:#0e2236;
  --line:#1e3a54;
  --text:#f5f8fc;
  --muted:#aab8c8;
  --blue:#2997ff;
  --blue2:#6db8ff;
  --green:#35d49a;
  --purple:#9c7cff;
}
html { scroll-behavior:smooth; }
.stApp { background: radial-gradient(circle at 80% 5%, rgba(41,151,255,.13), transparent 25%), var(--bg); color:var(--text); }
[data-testid="stHeader"] { background:rgba(6,17,29,.72); backdrop-filter:blur(14px); }
.block-container { max-width:1180px; padding-top:1.2rem; padding-bottom:4rem; }
section[data-testid="stSidebar"] { display:none; }

/* Hide Streamlit chrome */
#MainMenu, footer { visibility:hidden; }

.navbar { position:sticky; top:0; z-index:20; display:flex; align-items:center; justify-content:space-between; padding:14px 20px; margin-bottom:30px; border:1px solid rgba(125,180,230,.14); border-radius:18px; background:rgba(7,20,33,.82); backdrop-filter:blur(18px); box-shadow:0 12px 40px rgba(0,0,0,.22); }
.brand { font-family:'Space Grotesk'; font-weight:800; font-size:25px; color:#fff; letter-spacing:-1px; }
.navlinks a { color:#b9c8d8; text-decoration:none; margin-left:22px; font-size:14px; font-weight:600; }
.navlinks a:hover { color:#fff; }

.hero { min-height:490px; display:flex; align-items:center; padding:42px 10px 24px; }
.eyebrow { color:var(--blue2); font-weight:700; font-size:16px; margin-bottom:8px; }
h1 { font-family:'Space Grotesk'; font-size:clamp(42px,6vw,76px)!important; line-height:.98!important; letter-spacing:-3px; margin:0 0 16px!important; }
.gradient { background:linear-gradient(100deg,#fff 15%,#2997ff 70%,#83c7ff); -webkit-background-clip:text; background-clip:text; color:transparent; }
.hero-sub { font-size:21px; color:#dce8f4; font-weight:600; margin-bottom:16px; }
.hero-copy { color:var(--muted); font-size:16px; line-height:1.75; max-width:650px; }
.pill { display:inline-block; border:1px solid #2a4a68; background:rgba(25,58,86,.5); border-radius:999px; padding:8px 13px; margin:5px 5px 0 0; color:#d9e7f4; font-size:12px; }

.profile-wrap { display:flex; justify-content:center; align-items:center; min-height:390px; }
.profile-ring { width:350px; height:350px; border-radius:50%; display:flex; align-items:center; justify-content:center; background:radial-gradient(circle,#177de4 0%,#0e4f99 38%,transparent 69%); box-shadow:0 0 100px rgba(41,151,255,.24); }
.profile-placeholder { width:250px; height:300px; border-radius:38% 38% 45% 45%; background:linear-gradient(160deg,#172d43,#07101a); border:1px solid #335b7c; display:flex; align-items:center; justify-content:center; color:#74bfff; font-family:'Space Grotesk'; font-size:76px; font-weight:800; }

.cta { display:inline-block; padding:13px 20px; border-radius:12px; text-decoration:none!important; font-weight:700; margin:18px 8px 0 0; border:1px solid #2f78b9; }
.cta-primary { background:#218ff0; color:#fff!important; box-shadow:0 10px 25px rgba(33,143,240,.22); }
.cta-secondary { background:transparent; color:#eaf4ff!important; }
.socials { margin-top:18px; }
.socials a { display:inline-flex; width:38px; height:38px; align-items:center; justify-content:center; border:1px solid #27445e; border-radius:10px; color:#dcecff; text-decoration:none; margin-right:8px; background:rgba(11,31,49,.75); }

.stats { display:grid; grid-template-columns:repeat(4,1fr); gap:0; border:1px solid var(--line); border-radius:18px; background:rgba(10,27,43,.72); margin:4px 0 50px; overflow:hidden; }
.stat { padding:22px 15px; text-align:center; border-right:1px solid var(--line); }
.stat:last-child { border-right:0; }
.stat-num { font-family:'Space Grotesk'; font-size:28px; font-weight:800; }
.stat-label { color:var(--muted); font-size:13px; }

.section { padding:30px 0 18px; scroll-margin-top:100px; }
.section-kicker { color:var(--blue2); font-size:12px; font-weight:800; letter-spacing:2px; text-transform:uppercase; }
.section-title { font-family:'Space Grotesk'; font-size:32px; font-weight:800; margin:3px 0 24px; }
.card { background:linear-gradient(145deg,rgba(15,36,57,.96),rgba(7,22,35,.96)); border:1px solid var(--line); border-radius:17px; padding:22px; box-shadow:0 12px 30px rgba(0,0,0,.16); }
.muted { color:var(--muted); }

.info-grid { display:grid; grid-template-columns:1.35fr .9fr; gap:22px; }
.info-list { display:grid; grid-template-columns:110px 1fr; gap:13px 12px; font-size:14px; }
.info-list strong { color:#dce8f4; }

.timeline { position:relative; padding-left:28px; }
.timeline:before { content:''; position:absolute; left:7px; top:7px; bottom:7px; width:1px; background:#2a5678; }
.exp { position:relative; margin-bottom:22px; }
.exp:before { content:''; position:absolute; left:-26px; top:7px; width:10px; height:10px; border-radius:50%; background:#2997ff; box-shadow:0 0 0 5px rgba(41,151,255,.12); }
.exp-date { color:#70b9ff; font-size:12px; font-weight:700; }
.exp-title { font-size:18px; font-weight:800; margin-top:5px; }
.exp-company { color:#d5e4f2; margin:3px 0; font-size:14px; }

.projects { display:grid; grid-template-columns:repeat(3,1fr); gap:18px; }
.project-card { padding:0; overflow:hidden; transition:.25s ease; }
.project-card:hover { transform:translateY(-5px); border-color:#3976a8; box-shadow:0 18px 40px rgba(0,0,0,.28); }
.project-image { height:150px; display:flex; align-items:center; justify-content:center; background:linear-gradient(135deg,#102d48,#081521); color:#66b6ff; font-size:38px; font-weight:800; }
.project-body { padding:19px; }
.project-title { font-family:'Space Grotesk'; font-size:19px; font-weight:800; }
.tags { margin:11px 0; }
.tag { display:inline-block; padding:5px 8px; margin:3px; background:#162e45; border:1px solid #294660; border-radius:7px; color:#c9dbeb; font-size:11px; }
.project-links a { color:#8bcaff; text-decoration:none; font-size:13px; font-weight:700; margin-right:15px; }

.skills { display:grid; grid-template-columns:repeat(4,1fr); gap:16px; }
.skill-card h4 { margin:0 0 14px; font-family:'Space Grotesk'; }
.skill-card p { margin:0; line-height:2; }

.achievements { display:grid; grid-template-columns:repeat(4,1fr); gap:16px; }
.achievement-icon { font-size:27px; margin-bottom:8px; }
.achievement-title { font-weight:800; }

.contact { display:grid; grid-template-columns:1fr .85fr; gap:25px; }
.contact-art { min-height:300px; display:flex; align-items:center; justify-content:center; font-size:90px; background:radial-gradient(circle at 50% 50%,rgba(41,151,255,.22),transparent 58%); }
.footer { border-top:1px solid #1d3449; margin-top:45px; padding-top:22px; display:flex; justify-content:space-between; color:#8498ab; font-size:12px; }

/* Streamlit inputs */
.stTextInput input, .stTextArea textarea { background:#091b2c!important; color:#fff!important; border:1px solid #27455f!important; border-radius:11px!important; }
.stButton button, .stDownloadButton button { border-radius:10px!important; border:1px solid #2d6fa5!important; background:#168af0!important; color:white!important; font-weight:700!important; }

@media(max-width:850px){
 .navlinks{display:none}.hero{padding-top:20px}.profile-wrap{min-height:300px}.profile-ring{width:260px;height:260px}.profile-placeholder{width:185px;height:220px;font-size:55px}.stats{grid-template-columns:repeat(2,1fr)}.stat:nth-child(2){border-right:0}.stat:nth-child(-n+2){border-bottom:1px solid var(--line)}.info-grid,.contact{grid-template-columns:1fr}.projects{grid-template-columns:1fr}.skills{grid-template-columns:1fr 1fr}.achievements{grid-template-columns:1fr 1fr}h1{letter-spacing:-2px!important}
}
@media(max-width:520px){.skills,.achievements{grid-template-columns:1fr}.navbar{padding:12px 15px}.block-container{padding-left:18px;padding-right:18px}.footer{display:block}.footer div{margin-top:8px}}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Data from existing portfolio
# -----------------------------
experiences = [
    ("May 2023 – Jul 2023", "AI-ML Virtual Internship", "AICTE NEAT", "Amazon Web Services (AWS) · Machine Learning · Artificial Intelligence"),
    ("Aug 2023 – Present", "Graphic Design Lead", "CodeChef ABESEC Chapter", "Leading the graphics team and creating engaging creatives using Figma, Canva and Premiere Pro."),
    ("Sep 2022 – Nov 2023", "Coordinator", "Ardema", "Worked on graphics and technical activities and supported events."),
]
projects = [
    ("FileSpeak", "AI-powered PDF assistant for uploading documents, creating chats and interacting with an AI assistant.", ["Python","Gemini","PDF","AI"], "📄", "https://github.com/vimarsh11"),
    ("Ink & Quill", "MERN-stack content platform focused on a responsive, interactive and scalable web experience.", ["MongoDB","Express","React","Node.js"], "✒️", "https://github.com/vimarsh11"),
    ("PPT Tracking Controller", "Gesture-based PowerPoint controller using hand-shape detection and computer vision.", ["Python","OpenCV","MediaPipe","NumPy"], "📊", "https://github.com/vimarsh11"),
]

# -----------------------------
# Helpers
# -----------------------------
def lottie(url):
    try:
        r = requests.get(url, timeout=6)
        return r.json() if r.ok else None
    except Exception:
        return None


def safe_link(url, label):
    return f'<a href="{html.escape(url)}" target="_blank">{html.escape(label)}</a>'

# -----------------------------
# Navbar
# -----------------------------
st.markdown('''
<div class="navbar">
  <div class="brand">VJ</div>
  <div class="navlinks">
    <a href="#home">Home</a><a href="#about">About</a><a href="#experience">Experience</a><a href="#projects">Projects</a><a href="#skills">Skills</a><a href="#achievements">Achievements</a><a href="#contact">Contact</a>
  </div>
</div>
''', unsafe_allow_html=True)

# -----------------------------
# Hero
# -----------------------------
st.markdown('<div id="home" class="hero">', unsafe_allow_html=True)
left, right = st.columns([1.18, .82], gap="large")
with left:
    st.markdown('<div class="eyebrow">HELLO, I\'M</div>', unsafe_allow_html=True)
    st.markdown('<h1>Vimarsh <span class="gradient">Jaiswal</span></h1>', unsafe_allow_html=True)
    st.markdown('<div class="hero-sub">AI/ML Enthusiast · Full-Stack Developer · Creative Technologist</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-copy">Computer Science & Engineering student at ABES Engineering College, Ghaziabad, specializing in AI & ML. I enjoy building intelligent, user-focused applications at the intersection of AI, web development and design.</div>', unsafe_allow_html=True)
    st.markdown('<span class="pill">Artificial Intelligence</span><span class="pill">Machine Learning</span><span class="pill">Web Development</span><span class="pill">Graphic Design</span>', unsafe_allow_html=True)
    st.markdown('<a class="cta cta-primary" href="#projects">View Projects →</a><a class="cta cta-secondary" href="#contact">Let\'s Connect ↗</a>', unsafe_allow_html=True)
    st.markdown('<div class="socials">'+safe_link('https://www.linkedin.com/in/vimarshjaiswal','in')+safe_link('https://github.com/vimarsh11','GH')+safe_link('https://twitter.com/jaiswal_vimarsh','𝕏')+safe_link('mailto:jaiswaldesh16@gmail.com','✉')+'</div>', unsafe_allow_html=True)
with right:
    st.markdown('<div class="profile-wrap"><div class="profile-ring"><div class="profile-placeholder">VJ</div></div></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('''
<div class="stats">
 <div class="stat"><div class="stat-num">5+</div><div class="stat-label">Projects</div></div>
 <div class="stat"><div class="stat-num">147+</div><div class="stat-label">LeetCode</div></div>
 <div class="stat"><div class="stat-num">125+</div><div class="stat-label">GFG</div></div>
 <div class="stat"><div class="stat-num">5+</div><div class="stat-label">Hackathons</div></div>
</div>
''', unsafe_allow_html=True)

# -----------------------------
# About
# -----------------------------
st.markdown('<div id="about" class="section"><div class="section-kicker">01 · About</div><div class="section-title">A little about me</div>', unsafe_allow_html=True)
a,b=st.columns([1.25,.9],gap='large')
with a:
    st.markdown('<div class="card"><p class="muted" style="line-height:1.8;margin:0">I\'m a Computer Science & Engineering student at ABES Engineering College, Ghaziabad, specializing in AI & ML. I\'m well-versed in C/C++, Python and web development, with a keen interest in graphic design. I enjoy exploring new technologies, building projects and continuously learning to make a positive impact in the tech industry.</p></div>', unsafe_allow_html=True)
with b:
    st.markdown('''<div class="card"><div class="info-list"><strong>Name</strong><span>Vimarsh Jaiswal</span><strong>Education</strong><span>B.Tech CSE (AI & ML), ABES EC</span><strong>Location</strong><span>Lucknow, Uttar Pradesh</span><strong>Email</strong><span>jaiswaldesh16@gmail.com</span></div></div>''', unsafe_allow_html=True)
st.markdown('</div>',unsafe_allow_html=True)

# -----------------------------
# Experience
# -----------------------------
st.markdown('<div id="experience" class="section"><div class="section-kicker">02 · Experience</div><div class="section-title">Where I\'ve worked & learned</div><div class="card"><div class="timeline">', unsafe_allow_html=True)
for date,title,company,desc in experiences:
    st.markdown(f'<div class="exp"><div class="exp-date">{date}</div><div class="exp-title">{title}</div><div class="exp-company">{company}</div><div class="muted">{desc}</div></div>',unsafe_allow_html=True)
st.markdown('</div></div></div>',unsafe_allow_html=True)

# -----------------------------
# Projects
# -----------------------------
st.markdown('<div id="projects" class="section"><div class="section-kicker">03 · Featured Work</div><div class="section-title">Projects I\'m proud of</div><div class="projects">',unsafe_allow_html=True)
for title,desc,tags,icon,link in projects:
    tag_html=''.join(f'<span class="tag">{html.escape(t)}</span>' for t in tags)
    st.markdown(f'''<div class="card project-card"><div class="project-image">{icon}</div><div class="project-body"><div class="project-title">{html.escape(title)}</div><p class="muted">{html.escape(desc)}</p><div class="tags">{tag_html}</div><div class="project-links">{safe_link(link,'GitHub ↗')}</div></div></div>''',unsafe_allow_html=True)
st.markdown('</div></div>',unsafe_allow_html=True)

# -----------------------------
# Skills
# -----------------------------
st.markdown('<div id="skills" class="section"><div class="section-kicker">04 · Skills</div><div class="section-title">Tools & technologies</div><div class="skills">',unsafe_allow_html=True)
for title,icon,items in [
    ('Programming','⌘',['C/C++','Python','JavaScript']),
    ('Web Development','◉',['HTML','CSS','React','Bootstrap','Tailwind']),
    ('AI / ML','◈',['Artificial Intelligence','Machine Learning','Computer Vision']),
    ('Tools & Design','⚒',['GitHub','Figma','Canva','Premiere Pro']),
]:
    chips=''.join(f'<span class="tag">{html.escape(x)}</span>' for x in items)
    st.markdown(f'<div class="card skill-card"><h4>{icon} &nbsp;{title}</h4><p>{chips}</p></div>',unsafe_allow_html=True)
st.markdown('</div></div>',unsafe_allow_html=True)

# -----------------------------
# Achievements
# -----------------------------
st.markdown('<div id="achievements" class="section"><div class="section-kicker">05 · Achievements</div><div class="section-title">A few things I\'ve accomplished</div><div class="achievements">',unsafe_allow_html=True)
for icon,title,desc in [
    ('🏆','Coding','147+ LeetCode · 125+ GFG'),
    ('🥇','Open Source','Contributed to frontend and DSA projects · Top 10 in SWOC'),
    ('🚀','Hackathons','Participated in the 5th Technovation Hackathon'),
    ('🎨','Leadership','Graphic Design Lead at CodeChef ABESEC Chapter'),
]:
    st.markdown(f'<div class="card"><div class="achievement-icon">{icon}</div><div class="achievement-title">{title}</div><div class="muted" style="margin-top:6px">{desc}</div></div>',unsafe_allow_html=True)
st.markdown('</div></div>',unsafe_allow_html=True)

# -----------------------------
# VimAI
# -----------------------------
st.markdown('<div class="section"><div class="section-kicker">06 · VimAI</div><div class="section-title">Ask my AI assistant</div></div>',unsafe_allow_html=True)

persona = '''You are VimAI, the portfolio assistant for Vimarsh Jaiswal. Answer in first person as Vimarsh. Do not answer in second or third person. Use only the following verified portfolio information:\n\nVimarsh Jaiswal is a student at ABES Engineering College pursuing B.Tech in Computer Science & Engineering (AI & ML). He is well-versed in C/C++, Python, JavaScript, HTML, CSS, React and web development, with an interest in graphic design and AI/ML. He has worked with AWS, OpenCV, MediaPipe, NumPy, Figma, Canva and Premiere Pro. His projects include FileSpeak, Ink & Quill and PPT Tracking Controller. He has 147+ LeetCode problems and 125+ GeeksforGeeks questions, contributed to open-source projects, achieved a top 10 SWOC rank, and participated in the 5th Technovation Hackathon. Email: jaiswaldesh16@gmail.com. LinkedIn: https://www.linkedin.com/in/vimarshjaiswal. GitHub: https://github.com/vimarsh11. Twitter: https://twitter.com/jaiswal_vimarsh.'''

qcol, acol = st.columns([1,.9],gap='large')
with qcol:
    question = st.text_input('Ask something about my projects, skills, experience or resume', placeholder='e.g. What projects have I built?')
    ask = st.button('Ask VimAI →', use_container_width=False)
    if ask and question.strip():
        try:
            api_key = st.secrets.get('GOOGLE_API_KEY') or os.getenv('GOOGLE_API_KEY')
            if not api_key:
                st.warning('Add GOOGLE_API_KEY to Streamlit secrets or your environment to enable VimAI.')
            else:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('gemini-1.5-flash')
                with st.spinner('Thinking...'):
                    response = model.generate_content(persona + '\n\nUser question: ' + question)
                st.markdown(f'<div class="card"><strong>🤖 VimAI</strong><p class="muted" style="line-height:1.7">{html.escape(response.text)}</p></div>',unsafe_allow_html=True)
        except Exception as e:
            st.error(f'VimAI could not respond: {e}')
with acol:
    st.markdown('<div class="card contact-art">🤖</div>',unsafe_allow_html=True)

# -----------------------------
# Resume + Contact
# -----------------------------
st.markdown('<div id="contact" class="section"><div class="section-kicker">07 · Contact</div><div class="section-title">Let\'s work together</div>',unsafe_allow_html=True)
left,right=st.columns([1,.75],gap='large')
with left:
    st.markdown('<div class="card"><p class="muted">Have a project, opportunity, or just want to say hello? I\'d love to hear from you.</p></div>',unsafe_allow_html=True)
    with st.form('contact_form'):
        name=st.text_input('Your Name')
        email=st.text_input('Your Email')
        message=st.text_area('Your Message',height=130)
        submitted=st.form_submit_button('Send Message →')
        if submitted:
            if name and email and message:
                st.success('Thanks! Your message is ready to be sent. For production, connect this form to FormSubmit or your preferred email service.')
            else:
                st.warning('Please fill in all fields.')
with right:
    st.markdown('<div class="card"><h3>Resume</h3><p class="muted">Download the latest resume and explore my experience in more detail.</p></div>',unsafe_allow_html=True)
    resume_path='WD Resume.pdf'
    if os.path.exists(resume_path):
        with open(resume_path,'rb') as f:
            st.download_button('Download Resume',f,file_name='Vimarsh_Jaiswal_Resume.pdf',mime='application/pdf',use_container_width=True)
    else:
        st.info('Place your resume as "WD Resume.pdf" beside app.py to enable the download button.')

st.markdown('</div>',unsafe_allow_html=True)

st.markdown('''<div class="footer"><div>© 2026 Vimarsh Jaiswal · Built with Python & Streamlit</div><div>AI · Web · Design</div></div>''',unsafe_allow_html=True)
