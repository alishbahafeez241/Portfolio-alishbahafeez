# Alishba Hafeez — Portfolio (Streamlit + 3D)

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```
Then open the local URL Streamlit prints (usually http://localhost:8501).

## Deploy for free (so you can share a link, like your AI Investment Advisory app)
1. Push this folder to a new GitHub repo.
2. Go to https://share.streamlit.io, sign in with GitHub.
3. Click "New app", pick the repo, set main file to `app.py`, click Deploy.

## What's inside
- `app.py` — the whole portfolio (single file).
- The hero section uses **Three.js** (loaded from a CDN) rendered inside the page via
  `streamlit.components.v1.html`, giving you real animated 3D graphics (a rotating
  wireframe icosahedron "shield" + a floating particle field) while the rest of the
  site is pure Python/Streamlit.
- Sections: Hero, About, Skills, Experience, Projects (including your AI Investment
  Advisory System with a live-demo link), Certifications, Contact.

## Customize
- Swap colors: edit the `#29ffc6` (accent teal) and `#0d1b2a` (background navy) hex codes near the top CSS block.
- Add/edit projects: edit the `projects` list about halfway down `app.py`.
- Replace the mailto/LinkedIn/phone links in the "Contact" section at the bottom.
