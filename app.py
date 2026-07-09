import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Alishba Hafeez | Cybersecurity & Full-Stack Developer",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ----------------------------------------------------------------------------
# PROJECT LINKS — fill this in once you deploy the coffee shop site
# (see DEPLOY_INSTRUCTIONS.md in the coffee-beans-site.zip for a 60-second guide)
# ----------------------------------------------------------------------------
COFFEE_SHOP_LIVE_URL = ""  # <-- paste your deployed Netlify / GitHub Pages URL here

ASSETS_DIR = Path(__file__).parent / "assets"

# ----------------------------------------------------------------------------
# GLOBAL STYLE

# ----------------------------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

html, body, [class*="css"]  { font-family: 'Space Grotesk', sans-serif; }

#MainMenu, footer, header {visibility: hidden;}
.block-container { padding-top: 0rem; padding-bottom: 0rem; max-width: 1200px; }

.stApp {
    background: radial-gradient(circle at 20% 10%, #0d1b2a 0%, #060a12 45%, #030509 100%);
    color: #e8eef5;
}

::selection { background: #29ffc6; color: #04121a; }

.section-wrap { padding: 70px 6% 10px 6%; scroll-margin-top: 30px; }

html { scroll-behavior: smooth; }

.navpill {
    font-family: 'JetBrains Mono', monospace; font-size:0.8rem; color:#c9d6e3;
    border:1px solid rgba(255,255,255,0.14); padding:8px 18px; border-radius:20px;
    text-decoration:none; transition: all .2s ease; background: rgba(255,255,255,0.02);
}
.navpill:hover {
    color:#04121a; background:#29ffc6; border-color:#29ffc6;
    box-shadow: 0 0 18px rgba(41,255,198,0.4); transform: translateY(-2px);
}

.section-title {
    font-size: 2.1rem;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 28px;
    border-left: 4px solid #29ffc6;
    padding-left: 14px;
}

.card {
    background: linear-gradient(145deg, rgba(255,255,255,0.045), rgba(255,255,255,0.015));
    border: 1px solid rgba(41,255,198,0.15);
    border-radius: 16px;
    padding: 22px 24px;
    margin-bottom: 18px;
    transition: transform .25s ease, border-color .25s ease, box-shadow .25s ease;
}
.card:hover {
    transform: translateY(-4px);
    border-color: rgba(41,255,198,0.55);
    box-shadow: 0 10px 30px rgba(41,255,198,0.08);
}

.card h4 { margin: 0 0 6px 0; color: #ffffff; font-size: 1.12rem; }
.card p { margin: 0; color: #b7c4d3; font-size: 0.93rem; line-height: 1.5; }
.card .tag {
    display:inline-block; font-family:'JetBrains Mono', monospace; font-size:0.68rem;
    color:#29ffc6; border:1px solid rgba(41,255,198,0.4); border-radius:20px;
    padding:2px 10px; margin: 10px 6px 0 0;
}
.card a { color:#29ffc6; text-decoration:none; font-family:'JetBrains Mono', monospace; font-size:0.8rem; }
.card a:hover { text-decoration: underline; }

.skill-pill {
    display:inline-block; background: rgba(41,255,198,0.08);
    border: 1px solid rgba(41,255,198,0.3); color:#dff7ee;
    padding: 7px 16px; border-radius: 30px; margin: 5px 6px 5px 0;
    font-size: 0.85rem; font-family:'JetBrains Mono', monospace;
}

.timeline-item {
    border-left: 2px solid rgba(41,255,198,0.35);
    padding: 2px 0 22px 24px; position: relative; margin-left: 6px;
}
.timeline-item::before {
    content:''; position:absolute; left:-7px; top:4px; width:12px; height:12px;
    background:#29ffc6; border-radius:50%; box-shadow: 0 0 12px #29ffc6;
}
.timeline-item h4 { color:#fff; margin:0 0 2px 0; }
.timeline-item .meta { color:#29ffc6; font-family:'JetBrains Mono', monospace; font-size:0.78rem; margin-bottom:6px; }
.timeline-item p { color:#b7c4d3; margin:0; font-size:0.92rem; }

.footer-cta {
    text-align:center; padding: 60px 6% 50px 6%;
}
.footer-cta a.btn {
    display:inline-block; background:#29ffc6; color:#04121a; font-weight:600;
    padding: 12px 30px; border-radius: 30px; text-decoration:none; margin: 6px 8px;
    font-family:'JetBrains Mono', monospace; font-size:0.85rem;
    transition: transform .2s ease;
}
.footer-cta a.btn:hover { transform: scale(1.05); }
.footer-cta a.btn.outline {
    background: transparent; color:#29ffc6; border:1px solid #29ffc6;
}
hr.div { border: none; border-top: 1px solid rgba(255,255,255,0.08); margin: 10px 6% 0 6%; }
</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# HERO with three.js 3D animation
# ----------------------------------------------------------------------------
hero_html = """
<div id="hero-wrap" style="position:relative; width:100%; height:480px; border-radius:20px; overflow:hidden;
     background: radial-gradient(circle at 30% 20%, #0e2436 0%, #060b12 70%); font-family:'Space Grotesk', sans-serif;">
  <canvas id="c" style="position:absolute; inset:0; width:100%; height:100%;"></canvas>
  <div style="position:absolute; inset:0; display:flex; flex-direction:column; justify-content:center;
       padding: 0 6%; z-index:2; pointer-events:none;">
    <div style="font-family:'JetBrains Mono', monospace; color:#29ffc6; letter-spacing:3px; font-size:0.85rem;">
      HELLO, I'M
    </div>
    <div style="font-size: clamp(2.2rem, 5vw, 3.6rem); font-weight:700; color:#ffffff; margin:6px 0 4px 0; text-shadow: 0 0 30px rgba(41,255,198,0.25);">
      Alishba Hafeez
    </div>
    <div style="font-size: 1.2rem; color:#c9d6e3; margin-bottom:18px;">
      Cybersecurity Student &amp; Full-Stack Developer
    </div>
    <div style="color:#8fa3b8; max-width:520px; font-size:0.95rem; line-height:1.6;">
      Building secure, intelligent, and scalable digital solutions — from network
      defense to full-stack web apps and machine learning.
    </div>
  </div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
(function(){
  const wrap = document.getElementById('hero-wrap');
  const canvas = document.getElementById('c');
  const renderer = new THREE.WebGLRenderer({canvas: canvas, antialias:true, alpha:true});
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(60, wrap.clientWidth/wrap.clientHeight, 0.1, 1000);
  camera.position.set(0,0,32);

  function resize(){
    renderer.setSize(wrap.clientWidth, wrap.clientHeight, false);
    camera.aspect = wrap.clientWidth/wrap.clientHeight;
    camera.updateProjectionMatrix();
  }
  resize();
  window.addEventListener('resize', resize);

  // Icosahedron wireframe "shield core"
  const geo = new THREE.IcosahedronGeometry(9, 1);
  const mat = new THREE.MeshBasicMaterial({color: 0x29ffc6, wireframe:true, transparent:true, opacity:0.55});
  const core = new THREE.Mesh(geo, mat);
  core.position.set(9, 1, 0);
  scene.add(core);

  const innerGeo = new THREE.IcosahedronGeometry(5.4, 0);
  const innerMat = new THREE.MeshBasicMaterial({color: 0x6ce9ff, wireframe:true, transparent:true, opacity:0.35});
  const inner = new THREE.Mesh(innerGeo, innerMat);
  inner.position.copy(core.position);
  scene.add(inner);

  // Particle field (network / data nodes)
  const particleCount = 260;
  const positions = new Float32Array(particleCount * 3);
  for (let i=0; i<particleCount; i++){
    positions[i*3]   = (Math.random()-0.5) * 70;
    positions[i*3+1] = (Math.random()-0.5) * 40;
    positions[i*3+2] = (Math.random()-0.5) * 40;
  }
  const pGeo = new THREE.BufferGeometry();
  pGeo.setAttribute('position', new THREE.BufferAttribute(positions, 3));
  const pMat = new THREE.PointsMaterial({color:0x29ffc6, size:0.5, transparent:true, opacity:0.65});
  const points = new THREE.Points(pGeo, pMat);
  scene.add(points);

  let mouseX = 0, mouseY = 0;
  wrap.addEventListener('mousemove', (e) => {
    const r = wrap.getBoundingClientRect();
    mouseX = ((e.clientX - r.left) / r.width - 0.5);
    mouseY = ((e.clientY - r.top) / r.height - 0.5);
  });

  function animate(){
    requestAnimationFrame(animate);
    core.rotation.y += 0.0025;
    core.rotation.x += 0.0012;
    inner.rotation.y -= 0.0035;
    inner.rotation.x += 0.0018;
    points.rotation.y += 0.0006;

    camera.position.x += (mouseX*8 - camera.position.x) * 0.02;
    camera.position.y += (-mouseY*6 - camera.position.y) * 0.02;
    camera.lookAt(scene.position);

    renderer.render(scene, camera);
  }
  animate();
})();
</script>
"""
components.html(hero_html, height=490)

# ----------------------------------------------------------------------------
# NAV-ish quick links row
# ----------------------------------------------------------------------------
nav_items = [
    ("About", "about"), ("Skills", "skills"), ("Experience", "experience"),
    ("Projects", "projects"), ("Certifications", "certifications"), ("Contact", "contact"),
]
st.markdown("""
<div style="display:flex; justify-content:center; gap:10px; flex-wrap:wrap; margin: 18px 0 0 0;">
""" + "".join([
    f'<a class="navpill" href="#{anchor}">{label}</a>' for label, anchor in nav_items
]) + "</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# ABOUT
# ----------------------------------------------------------------------------
st.markdown('<div class="section-wrap" id="about">', unsafe_allow_html=True)
st.markdown('<div class="section-title">About Me</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1.4, 1])
with col1:
    st.markdown("""
    <p style="color:#c9d6e3; font-size:1.02rem; line-height:1.85;">
    Highly motivated Computer Science student specializing in <b style="color:#29ffc6;">Cybersecurity</b>,
    currently in the 6th semester of a BSCS program at Capital University of Science and Technology,
    with additional hands-on experience as a <b style="color:#29ffc6;">Full-Stack Web Developer</b>.
    I combine strong development skills in C++, Python, HTML, CSS, Bootstrap and JavaScript with
    practical, security-focused coursework and internships. Proficient in Kali Linux for security
    testing and Cisco Packet Tracer for network architecture, I'm dedicated to building secure,
    intelligent, and scalable digital solutions that bridge robust software engineering with
    proactive cyber defense.
    </p>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="card">
      <h4>🎓 Education</h4>
      <p><b>BS Computer Science — Cybersecurity</b><br>
      Capital University of Science and Technology, Islamabad<br>
      2023 – 2027 · 6th Semester · CGPA 3.73</p>
    </div>
    <div class="card">
      <h4>📍 Location</h4>
      <p>Kallar Syedan, Rawalpindi, Punjab, Pakistan</p>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<hr class="div">', unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# SKILLS
# ----------------------------------------------------------------------------
st.markdown('<div class="section-wrap" id="skills">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Technical Skills</div>', unsafe_allow_html=True)

skill_groups = {
    "🛡️ Cybersecurity": ["Kali Linux", "Wireshark", "Network Security Fundamentals", "Cisco Packet Tracer"],
    "💻 Programming": ["C", "C++", "Python", "C#", "HTML", "JavaScript", "CSS", "Bootstrap", "JSON"],
    "🧩 Frameworks & Backend": ["ASP.NET (DB Backend)", "Angular", "React (Basics)"],
    "📊 Data & ML": ["Excel", "Python", "Matplotlib", "Predictive Modeling"],
    "🗄️ Database": ["MySQL", "ASP.NET DB Backends"],
    "🌐 Networking": ["Linux", "Wireshark", "Cisco"],
    "🧰 Tools": ["MS Word", "PowerPoint", "Excel"],
}
cols = st.columns(2)
for i, (group, skills) in enumerate(skill_groups.items()):
    with cols[i % 2]:
        pills = "".join([f'<span class="skill-pill">{s}</span>' for s in skills])
        st.markdown(f"""
        <div class="card">
          <h4>{group}</h4>
          <div>{pills}</div>
        </div>
        """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<hr class="div">', unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# EXPERIENCE
# ----------------------------------------------------------------------------
st.markdown('<div class="section-wrap" id="experience">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Professional Experience</div>', unsafe_allow_html=True)

st.markdown("""
<div class="timeline-item">
  <h4>Remote Cybersecurity Intern — Arch Technologies</h4>
  <div class="meta">Started 01 April 2026 · Completed</div>
  <p>Applied security fundamentals and hands-on tooling (Kali Linux, Wireshark) in a remote, real-world environment.</p>
</div>
<div class="timeline-item">
  <h4>Remote Full-Stack Intern — Developer Hub Corporation</h4>
  <div class="meta">Started 27 April 2026 · Completed</div>
  <p>Built and maintained full-stack web applications, working across frontend and backend.</p>
</div>
<div class="timeline-item">
  <h4>Teaching Experience</h4>
  <div class="meta">Tutor</div>
  <p>Tutored students in Computer Science and Mathematics.</p>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<hr class="div">', unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# PROJECTS
# ----------------------------------------------------------------------------
st.markdown('<div class="section-wrap" id="projects">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Featured Projects</div>', unsafe_allow_html=True)

projects = [
    {
        "title": "🤖 AI Investment Advisory System",
        "desc": "An ML-powered web app that analyzes financial data and generates data-driven investment "
                "recommendations. Deployed live on Streamlit Cloud.",
        "tags": ["Python", "Machine Learning", "Streamlit"],
        "link": "https://ai-investment-advisory-system-wjyfskujcuxpfuwzisplfp.streamlit.app/",
        "link_text": "🔗 Live Demo",
    },
    {
        "title": "☕ Coffee Beans Shop",
        "desc": "A 9-page full-stack coffee shop site — home, menu, cart, reviews, contact, login/signup — "
                "built with HTML, Bootstrap, AngularJS and jQuery.",
        "tags": ["HTML/CSS", "Bootstrap", "AngularJS", "jQuery"],
        **({"link": "https://alishbahafeez241.github.io/Coffee-Shop-Website/", "link_text": "🔗 Live Demo"} if COFFEE_SHOP_LIVE_URL else {}),
        "preview": "coffee",
    },
    {
        "title": "💬 Basic Chatbot (AI/NLP)",
        "desc": "A rule-based chatbot built in Python with a self-created dataset, integrating HTML/CSS for an interactive frontend.",
        "tags": ["Python", "NLP", "HTML/CSS"],
    },
    {
        "title": "👗 Full-Stack Wardrobe Management System",
        "desc": "A full-stack application for organizing and managing a digital wardrobe.",
        "tags": ["Full-Stack", "MySQL"],
    },
    {
        "title": "🛒 E-Commerce Frontend Interface",
        "desc": "A responsive e-commerce frontend interface built with modern web technologies.",
        "tags": ["HTML", "CSS", "JavaScript"],
    },
    {
        "title": "🍽️ Restaurant & Dining Frontend Design",
        "desc": "A clean, user-friendly frontend design for a restaurant and dining experience.",
        "tags": ["UI/UX", "Frontend"],
    },
]

cols = st.columns(2)
for i, p in enumerate(projects):
    with cols[i % 2]:
        tags_html = "".join([f'<span class="tag">{t}</span>' for t in p["tags"]])
        link_html = f'<div style="margin-top:10px;"><a href="{p["link"]}" target="_blank">{p["link_text"]} →</a></div>' if "link" in p else ""
        st.markdown(f"""
        <div class="card">
          <h4>{p['title']}</h4>
          <p>{p['desc']}</p>
          <div>{tags_html}</div>
          {link_html}
        </div>
        """, unsafe_allow_html=True)

        if p.get("preview") == "coffee":
            if not COFFEE_SHOP_LIVE_URL:
                st.caption("No live URL set yet — showing an embedded preview of the home page below.")
            with st.expander("👀 Open embedded live preview"):
                preview_file = ASSETS_DIR / "coffee_index_preview.html"
                if preview_file.exists():
                    components.html(preview_file.read_text(encoding="utf-8"), height=650, scrolling=True)
                    st.caption(
                        "This is the actual home page rendering live. It's a 9-page site "
                        "(menu, cart, reviews, login, signup...) — deploy the full site for free "
                        "to unlock navigation between pages; see DEPLOY_INSTRUCTIONS.md."
                    )
                else:
                    st.info("Preview file not found — make sure the `assets/` folder ships next to app.py.")
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<hr class="div">', unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# CERTIFICATIONS
# ----------------------------------------------------------------------------
st.markdown('<div class="section-wrap" id="certifications">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Certifications</div>', unsafe_allow_html=True)

certifications = [
    ("🛡️", "Cybersecurity Internship Completion", "Arch Technologies"),
    ("💻", "Full-Stack Development Internship Completion", "Developer Hub Corporation"),
    ("🏅", "Introduction to Cybersecurity", "Cisco Networking Academy"),
    ("🖥️", "Operating Systems Basics", "Certificate of Completion"),
    ("🏆", "ICPC Participation Certificate", "Capital University of Science and Technology"),
    ("🎓", "Dean's Honor Roll", "Capital University of Science and Technology"),
]
cols = st.columns(2)
for i, (icon, title, org) in enumerate(certifications):
    with cols[i % 2]:
        st.markdown(f"""
        <div class="card">
          <h4>{icon} {title}</h4>
          <p>{org}</p>
        </div>
        """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# CONTACT / FOOTER
# ----------------------------------------------------------------------------
st.markdown("""
<div class="footer-cta" id="contact">
  <div class="section-title" style="border:none; text-align:center; padding-left:0;">Let's Connect</div>
  <p style="color:#8fa3b8; max-width:520px; margin:0 auto 20px auto;">
    Open to cybersecurity, full-stack, and machine learning opportunities, internships, and collaborations.
  </p>
  <a class="btn" href="mailto:alishbahafeez241@gmail.com">✉ Email Me</a>
  <a class="btn outline" href="https://linkedin.com/in/alishba-hafeez-289b7139b" target="_blank">🔗 LinkedIn</a>
  <a class="btn outline" href="tel:+923277983117">📞 +92-327-7983117</a>
  <p style="color:#4d5c6e; font-size:0.78rem; margin-top:30px; font-family:'JetBrains Mono', monospace;">
    © 2026 Alishba Hafeez · Built with Streamlit &amp; Three.js
  </p>
</div>
""", unsafe_allow_html=True)
