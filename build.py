# Edit the data below, then run:  python3 build.py
from pathlib import Path

NAME = "Piero Christian Ronaldo"
EMAIL = "pierochristian10@gmail.com"
WA = "6287820060810"
WA_TXT = "+62 878-2006-0810"
IG = "https://www.instagram.com/piewuo/"
GH = "https://github.com/P1caro"
LINKEDIN = "https://www.linkedin.com/in/piero-christian-ronaldo-728194326/"
LOCATION = "Tangerang, Banten, Indonesia"
TAGLINE = "Computer Science Student at BINUS Alam Sutera | AI Track | Aspiring AI &amp; Software Engineer"

BINUS_MAP = (
    "https://www.google.com/maps/search/?api=1&query=BINUS+University+Alam+Sutera"
)
PJA_MAP = "https://maps.app.goo.gl/ybY52k2vxXVAtdRU6"
COURSES_VISIBLE = 12  # how many course pills show before "See more"

ABOUT = (
    "I'm a Computer Science student at BINUS University with a strong focus on "
    "<em>front-end development</em>. I love bringing ideas to life in the browser and creating "
    "seamless digital experiences. Recently, I've been focused on building dynamic web applications "
    "and continuously refining my UI/UX skills. I'm always eager to tackle new design challenges, and "
    "I'm even practicing conversational Mandarin on the side to broaden my communication skills."
)
ABOUT_COLS = [
    "Front-end development is where I spend most of my time. I care about interfaces that feel fast, "
    "readable, and considered down to the spacing, and I enjoy the part of the work where a rough idea "
    "turns into something people can actually click through.",
    "UI/UX design sits right next to that for me: wireframing, iterating on layouts, and testing whether "
    "a flow makes sense before a line of code is written. And when a project needs backend work, APIs, "
    "data handling, or model integration, I'm glad to step in and help get it done.",
]

# Logos: drop your own files at these paths.
EDUCATION = dict(
    school="BINUS University",
    sub="Undergraduate Student",
    logo="image/binus.png",
    date="Aug 2024 - Present",
    field="Computer Science | AI Streaming",
    place="BINUS Alam Sutera",
    map=BINUS_MAP,
    courses=[
        "Python",
        "C++",
        "Java",
        "JavaScript",
        "SQL",
        "Machine Learning",
        "Deep Learning",
        "Computer Vision",
        "Artificial Intelligence (AI)",
        "Data Structures",
        "React.js",
        "Web Development",
        "Algorithm and Programming",
        "Algorithm Design and Analysis",
        "Basic Statistics",
        "Discrete Mathematics",
        "Linear Algebra",
        "Calculus",
        "Program Design Method",
        "Creativity and Innovation",
        "Human and Computer Interaction",
        "Scientific Computing",
        "Computational Physics",
        "Computer Networking",
        "Database Technology",
        "Object-Oriented Programming (OOP)",
        "Cisco Routers",
        "Anaconda",
        "Computational Biology",
        "Natural Language Processing (NLP)",
        "Research Methods",
        "Software Systems Engineering",
        "BLAST",
        "Random Forest",
        "YOLO",
        "CNN",
        "Compilation Techniques",
        "Operating Systems",
        "Speech Recognition",
        "Venture Creation",
        "Programming",
        "Front-End Design",
        "Front-end Coding",
        "Back-End Web Development",
        "Laravel",
        "Linux",
        "HTML",
    ],
)

EXPERIENCE = dict(
    role="Assistant",
    company="PT Piero Jaya Abadi",
    logo="image/pja.jpeg",
    date="June 2024 - Present",
    place="PT Piero Jaya Abadi",
    map=PJA_MAP,
    jd=[
        "Executed monthly payroll processing and managed financial administration accurately within the finance department.",
        "Recorded and evaluated sample bag dimensions to facilitate the design and development of new product lines.",
    ],
    learn=[
        "Accounting",
        "Bookkeeping",
        "Cross-functional Collaborations",
        "Data Accuracy &amp; Attention to Detail",
        "Data Recording &amp; Evaluation",
        "Financial Management",
        "Payroll Management",
        "Product Development",
        "Quality Control &amp; Measurement",
        "Specification Analysis",
    ],
)

SKILLS = [
    (
        "Front-End",
        "M3 3v18h18M7 14l3-3 3 3 5-5",
        [
            "React.js",
            "HTML",
            "CSS",
            "JavaScript",
            "Laravel",
            "Front-End Design",
            "Responsive UI",
        ],
    ),
    (
        "Design",
        "M12 2 2 7l10 5 10-5-10-5ZM2 17l10 5 10-5M2 12l10 5 10-5",
        ["UI / UX Design", "Figma", "Prototyping"],
    ),
    (
        "AI &amp; Data",
        "M12 2a5 5 0 0 1 5 5v1a4 4 0 0 1 0 8v1a5 5 0 0 1-10 0v-1a4 4 0 0 1 0-8V7a5 5 0 0 1 5-5Z",
        ["Machine Learning", "Computer Vision", "NLP", "YOLO", "CNN", "Bioinformatics"],
    ),
    (
        "Engineering",
        "m8 6-6 6 6 6m8-12 6 6-6 6",
        ["Python", "C++", "SQL", "Git &amp; GitHub", "Linux"],
    ),
    (
        "Soft Skills",
        "M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2M9 3a4 4 0 1 1 0 8 4 4 0 0 1 0-8Zm13 18v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75",
        [
            "Communicative",
            "Multitasking",
            "Teamwork",
            "Problem Solving",
            "Creativity",
            "Finance",
        ],
    ),
]

# name, note, percent, light hex, dark hex  (palette validated for both surfaces)
LANGUAGES = [
    ("Indonesian", "Native, everyday language", 100, "#2a78d6", "#3987e5"),
    ("Chinese", "HSK 4, upper intermediate", 70, "#eb6834", "#d95926"),
    ("English", "Intermediate, working proficiency", 60, "#1baf7a", "#199e70"),
]

PROJECTS = [
    dict(
        t="Digimart",
        cat="Frontend Website",
        role="Frontend Developer",
        year="2025",
        url="https://github.com/P1caro/Digimart",
        sum="E-Commerce Web App.",
        desc="As the UI Designer and Frontend Developer, I built the responsive interface for Digimart, "
        "a tech e-commerce web app, using React and Tailwind CSS. I designed a clean and consistent "
        "shopping experience from product listings to checkout, which deepened my skills in creating "
        "reusable components, maintaining a design system, and collaborating with backend teams.",
        caps=["Home Page", "Shopping Cart Page", "Admin Page"],
    ),
    dict(
        t="VSTravel",
        cat="Frontend Website",
        role="Full-Stack Developer",
        year="2025",
        url="https://github.com/P1caro/VSTravel",
        sum="Travel Booking Web App",
        desc="To modernize traditional travel marketing, I built VSTravel, a responsive catalog and booking "
        "platform for Indonesian destinations using pure HTML, CSS, and JavaScript. Created as my "
        "individual HCI project, it features dynamic filtering and interactive form validation, "
        "deepening my skills in frontend development and proving that a well-structured interface "
        "builds user trust.",
        caps=["Destination Page", "Contact Us Page", "About Us Page"],
    ),
    dict(
        t="GeneMix",
        cat="Bioinformatics Website",
        role="Full-Stack Developer",
        year="2026",
        url="https://github.com/P1caro/GeneMix",
        sum="Genetics Simulation Platform",
        desc="To replace tedious manual Punnett squares, I independently developed GeneMix, a full-stack "
        "Mendelian inheritance simulator. Built with a Node.js and Express backend alongside a vanilla "
        "HTML/CSS/JS frontend using Chart.js, the app calculates and visualizes the probabilities of a "
        "child inheriting specific blood types and genetic conditions. This project sharpened my ability "
        "to translate complex biological rules into testable code and present data clearly to everyday users.",
        caps=["Simulation Page", "Result Page", "Instruction Page"],
    ),
    dict(
        t="Malaria Detection App",
        cat="Computer Vision Website",
        role="Frontend Developer &amp; UI/UX Designer",
        year="2026",
        url="https://github.com/DffaFyyz/malaria-detection-app",
        sum="Malaria Cell Classification Website",
        desc="As part of a team project, I took the Frontend Developer and UI/UX Designer role on this "
        "malaria cell classification platform. I designed and built the interface that lets a user upload "
        "a thin blood smear image, pick between Random Forest and Logistic Regression, and read back the "
        "predicted class, the confidence score, and the features the model extracted. My focus was making "
        "a research tool feel approachable: a clear upload flow, result cards that are easy to scan, and an "
        "honest presentation of what the model can and cannot tell you, since the app is built for academic "
        "use rather than clinical diagnosis.",
        caps=["Predict Page", "Feature Extraction Page", "Result Model Page"],
    ),
    dict(
        t="Piflix",
        cat="Machine Learning Website",
        role="Frontend Developer &amp; UI/UX Designer",
        year="2026",
        url="https://github.com/Arthurchrst/Piflix",
        sum="Contrast Taste Film Rating System",
        desc="Piflix is a film rating platform driven by a machine learning recommendation model, where I "
        "worked as the Frontend Developer and UI/UX Designer. Its twist is contrast: alongside films that "
        "match your taste, it surfaces what viewers with the opposite taste enjoy. I designed the flow and "
        "built the interface that turns the model output into something people actually want to browse, "
        "translating raw similarity scores into film cards, taste comparisons, and a layout that makes the "
        "two opposing recommendation feeds easy to read side by side.",
        caps=["Home Page", "Same Taste Page", "Opposite Taste Page"],
    ),
    dict(
        t="Portfolio",
        cat="Portfolio Website",
        role="Frontend Developer",
        year="2026",
        url="https://github.com/P1caro/Portfolio",
        sum="Personal Portfolio Website",
        desc="I designed and built this portfolio to bring my experience, skills, and project work together "
        "in one place. Built with HTML, CSS, and JavaScript, it features responsive layouts, individual "
        "project case studies, and a light/dark theme that remembers the visitor's choice. I also created "
        "a Python build script to generate the pages from shared project data, keeping the site consistent "
        "and straightforward to update.",
        caps=["Project Page", "Footer", "Dark Mode"],
    ),
]
for i, p in enumerate(PROJECTS, 1):
    p["n"] = i
    p["f"] = f"project{i}.html"

FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;0,9..144,700;1,9..144,400'
    "&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,500;0,8..60,600;0,8..60,700;1,8..60,400&family=Mr+Dafoe"
    '&family=Newsreader:ital,opsz,wght@0,6..72,400;1,6..72,400&display=swap" rel="stylesheet">'
)
THEME = (
    '<script>try{var t=localStorage.getItem("theme")||(matchMedia("(prefers-color-scheme:dark)").matches?"dark":"light");'
    "document.documentElement.dataset.theme=t}catch(e){}</script>"
)


def ic(b, s=22, cls=""):
    c = f' class="{cls}"' if cls else ""
    return (
        f'<svg{c} viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" '
        f'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{b}</svg>'
    )


LOGO = (
    '<svg class="logo" viewBox="0 0 64 64" aria-hidden="true">'
    '<path d="M15 57c4-19 8-35 11-43 1-4 4-6 7-6 6 0 10 5 9 11-1 8-9 14-19 15 4 1 8 1 11 0"/></svg>'
)
WAI = ic(
    '<path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/><path d="M9 9.5c0 3 2.5 5.5 5.5 5.5l1.2-1.3-2-1-.8.7c-.9-.4-1.7-1.2-2.1-2.1l.7-.8-1-2z"/>'
)
MAI = ic('<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>')
GHP = '<path d="M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.4 5.4 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4"/><path d="M9 18c-4.51 2-5-2-7-2"/>'
GHI = ic(GHP)
INI = ic(
    '<path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/>'
)
IGI = ic(
    '<rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><path d="M17.5 6.5h.01"/>'
)
MOON = ic('<path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"/>', 20, "moon")
SUN = ic(
    '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2m-7.07-2.93 1.41-1.41m11.32-11.32 1.41-1.41M2 12h2m16 0h2M4.93 4.93l1.41 1.41m11.32 11.32 1.41 1.41"/>',
    20,
    "sun",
)
PIN = ic(
    '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>',
    24,
)
CAL = ic(
    '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M16 3v4M8 3v4M3 11h18"/>',
    15,
)
ARROW = ic('<path d="M7 17 17 7M9 7h8v8"/>', 17)
ARROW_BACK = ic('<path d="M17 17 7 7M15 7H7v8"/>', 17)
NAV_NEXT = ic('<path d="M5 12h14M13 6l6 6-6 6"/>', 21)
NAV_BACK = ic('<path d="M19 12H5M11 6l-6 6 6 6"/>', 21)
CHEV = ic('<path d="m6 9 6 6 6-6"/>', 15)


def ph(f, alt, cls=""):
    return f'<div class="ph {cls}" data-file="{f}"><img src="{f}" alt="{alt}" onerror="this.remove()"></div>'


def image_path(name):
    for ext in ("jpg", "jpeg", "png", "webp"):
        candidate = Path("image") / f"{name}.{ext}"
        if candidate.exists():
            return candidate.as_posix()
    return f"/{name}.png"


def crest(f, alt):
    return f'<div class="crest" data-file="{f}"><img src="{f}" alt="{alt}" onerror="this.remove()"></div>'


def loc(url, place):
    return (
        f'<a class="loc" href="{url}" target="_blank" rel="noopener">'
        f'<span class="pin">{PIN}</span><span><small>Location</small><b>{place}</b></span></a>'
    )


def datechip(text):
    return f'<span class="chip date">{CAL}{text}<i class="now"></i></span>'


def spread_letters(text):
    return "".join("<span>%s</span>" % (c if c != " " else "&nbsp;") for c in text)


def page(title, body, on, spy=False):
    links = [
        ("Home", "index.html", "#top"),
        ("About", "index.html#about", "#about"),
        ("Projects", "projects.html", "#work"),
    ]
    nav = ""
    for k, h, sel in links:
        if spy:
            href = sel if k != "Projects" else "projects.html"
            attr = f' data-spy="{sel}"' if k != "Projects" else ""
            nav += f'<li><a href="{href}"{attr} class="{"on" if k == "Home" else ""}">{k}</a></li>'
        else:
            nav += f'<li><a href="{h}" class="{"on" if k == on else ""}">{k}</a></li>'
    cta = (
        ("index.html", "Back to home")
        if title == "Projects"
        else ("projects.html", "Explore my projects")
    )
    fcards = (
        f'<a class="fc" href="https://wa.me/{WA}" target="_blank" rel="noopener">{WAI}<div><small>WhatsApp</small><span>{WA_TXT}</span></div></a>'
        f'<a class="fc" href="mailto:{EMAIL}">{MAI}<div><small>Email</small><span>{EMAIL}</span></div></a>'
        f'<a class="fc" href="{GH}" target="_blank" rel="noopener">{GHI}<div><small>GitHub</small><span>P1caro</span></div></a>'
        f'<a class="fc" href="{LINKEDIN}" target="_blank" rel="noopener">{INI}<div><small>LinkedIn</small><span>Piero Christian Ronaldo</span></div></a>'
        f'<a class="fc" href="{IG}" target="_blank" rel="noopener">{IGI}<div><small>Instagram</small><span>@piewuo</span></div></a>'
    )
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | {NAME}</title><meta name="description" content="{TAGLINE}">{THEME}{FONTS}<link rel="stylesheet" href="css/style.css"></head><body id="top">
<header class="top"><div class="wrap"><nav>
<a class="brand" href="index.html">{LOGO}<span>{NAME}<small>{LOCATION}</small></span></a>
<div class="navr"><ul>{nav}</ul><button class="tog" id="tog" aria-label="Toggle dark and light mode">{MOON}{SUN}</button></div>
</nav></div></header>
<main class="wrap">{body}</main>
<footer><div class="wrap">
<div class="ftop"><div><p class="spread-wide">{spread_letters("THANKS FOR STOPPING BY")}</p>
<h2>Take a look at what I&rsquo;ve built.</h2>
<a class="btn" href="{cta[0]}">{cta[1]} &rarr;</a></div>
<div class="fnav"><strong>Navigate</strong><a href="index.html">Home</a><a href="index.html#about">About</a>
<a href="index.html#background">Education &amp; Experience</a><a href="projects.html">My Project</a></div></div>
<div class="fcards">{fcards}</div>
<div class="foot"><span>&copy; 2026 {NAME}</span><span>{LOCATION}</span><span>Built with HTML, CSS &amp; JavaScript</span></div>
</div></footer><script src="js/main.js"></script></body></html>"""


def facts(p):
    return (
        f'<div class="facts"><div><small>Role</small><b>{p["role"]}</b></div>'
        f'<div><small>Year</small><b>{p["year"]}</b></div></div>'
    )


def hero_img(p):
    return image_path("img%d" % ((p["n"] - 1) * 4 + 1))


def card(p):
    img = ph(hero_img(p), p["t"])
    return (
        f'<a class="card rv" href="{p["f"]}">{img}<div class="cbody">'
        f'<span class="badge">0{p["n"]}</span><h3 class="pname">{p["t"]}</h3>'
        f'<p class="pcat">{p["cat"]}</p>{facts(p)}</div></a>'
    )


spread = "".join(
    '<b style="animation-delay:%.2fs">%s</b>' % (0.06 * i, c)
    for i, c in enumerate("PORTFOLIO")
)

skills = ""
for _n, _d, _items in SKILLS:
    _icon = ic('<path d="%s"/>' % _d, 19)
    _pills = "".join("<span>%s</span>" % s for s in _items)
    skills += f'<div class="sk rv"><h4>{_icon}{_n}</h4><div class="pills">{_pills}</div></div>'

langs = "".join(
    f'<div class="lang rv"><b>{n}<i>{note}</i></b><div class="bar">'
    f'<span style="--w:{pct}%;background:{lt}"></span></div></div>'
    for n, note, pct, lt, dk in LANGUAGES
)

# concentric proficiency rings — one arc per language, each measured against 100%
import math

rings = ""
legend = ""
for i, (n, note, pct, lt, dk) in enumerate(LANGUAGES):
    r = 72 - i * 21
    circ = 2 * math.pi * r
    rings += (
        f'<circle class="track" cx="100" cy="100" r="{r}"></circle>'
        f'<circle class="arc" cx="100" cy="100" r="{r}" stroke="var(--l{i+1})" '
        f'stroke-dasharray="{circ:.1f}" stroke-dashoffset="{circ:.1f}" '
        f'data-off="{circ * (1 - pct / 100):.1f}" transform="rotate(-90 100 100)"></circle>'
    )
    legend += f'<div><i style="background:var(--l{i+1})"></i>{n}<b>{pct}%</b></div>'
lvars = ";".join(f"--l{i+1}:{lt}" for i, (n, no, p, lt, dk) in enumerate(LANGUAGES))
dvars = ";".join(f"--l{i+1}:{dk}" for i, (n, no, p, lt, dk) in enumerate(LANGUAGES))
ring_style = (
    f"<style>.ring{{{lvars}}}:root[data-theme=dark] .ring{{{dvars}}}"
    f"@media(prefers-color-scheme:dark){{:root:not([data-theme=light]) .ring{{{dvars}}}}}</style>"
)
ring = (
    f'{ring_style}<div class="ring rv"><svg viewBox="0 0 200 200" role="img" '
    f'aria-label="Language proficiency: Indonesian 100 percent, Chinese 70 percent, English 60 percent">'
    f'{rings}</svg><div class="rlegend">{legend}</div></div>'
)

slides = ""
for p in PROJECTS:
    _img = ph(hero_img(p), p["t"])
    slides += (
        f'<a class="slide" href="{p["f"]}">{_img}'
        f'<div class="sbody"><span class="badge">0{p["n"]}</span>'
        f'<h3 class="pname">{p["t"]}</h3><p class="pcat">{p["cat"]}</p>{facts(p)}'
        f'<span class="go">View case study{ARROW}</span></div></a>'
    )
dots = "".join(
    f'<button aria-label="Show project {p["n"]}"></button>' for p in PROJECTS
)

E = EDUCATION
_head = "".join("<span>%s</span>" % c for c in E["courses"][:COURSES_VISIBLE])
_rest = "".join(
    '<span class="more">%s</span>' % c for c in E["courses"][COURSES_VISIBLE:]
)
_hidden = len(E["courses"]) - COURSES_VISIBLE
edu = f"""<div class="block rv"><div class="bhead">{crest(E["logo"], E["school"] + " logo")}
<div class="who"><h3>{E["school"]}</h3><p class="sub">{E["sub"]}</p><div class="bmeta">
{datechip(E["date"])}<span class="chip">{E["field"]}</span></div></div>
{loc(E["map"], E["place"])}</div>
<div class="rulel"></div>
<p class="subh">WHAT I LEARN THERE</p>
<div class="pills small" id="courses">{_head}{_rest}</div>
<button class="showmore" type="button" data-target="courses" aria-expanded="false"
data-less="Show fewer" data-more="See all {len(E["courses"])} subjects"><span>See all {len(E["courses"])} subjects</span>{CHEV}</button></div>"""

X = EXPERIENCE
jd = "".join(f"<li>{d}</li>" for d in X["jd"])
learn = "".join(f"<span>{item}</span>" for item in X["learn"])
exp = f"""<div class="block rv"><div class="bhead">{crest(X["logo"], X["company"] + " logo")}
<div class="who"><h3>{X["company"]}</h3><p class="sub">{X["role"]}</p><div class="bmeta">
{datechip(X["date"])}</div></div>
{loc(X["map"], X["place"])}</div>
<div class="rulel"></div>
<p class="subh">What I do there</p><ul class="jd">{jd}</ul>
<p class="subh">WHAT I LEARN THERE</p><div class="pills small">{learn}</div></div>"""

home = f"""<div class="hero"><div><p class="spread">{spread}</p>
<h1 class="sig" aria-label="{NAME}"><span class="a">Piero</span> <span class="b">Christian Ronaldo</span></h1>
<p class="role fu d2">Computer Science Student at BINUS Alam Sutera <i>|</i> AI Track <i>|</i> Aspiring AI &amp; Software Engineer</p>
<div class="status fu d3"><span class="beacon"><i></i></span><div class="txt">
<span class="tagline">Available now</span>
<b>Open to internships and collaborations</b>
<small>Currently a Computer Science student at BINUS University</small></div></div></div>
<div class="fu d4">{ph(image_path("profile"), NAME, "tall portrait")}<p class="cap">{LOCATION}</p></div></div>

<section id="about"><p class="label rv">About</p>
<div class="about"><div class="frame rv">{ph("image/about.jpg", NAME)}<span class="shine"></span></div>
<div class="abouttext"><p class="statement rv">{ABOUT}</p>
<div class="cols rv d1" style="margin-top:28px"><p>{ABOUT_COLS[0]}</p><p>{ABOUT_COLS[1]}</p></div></div></div></section>

<section id="background"><p class="label rv">Background</p>
<h2 class="rv" style="font-size:clamp(26px,3vw,34px);margin-top:18px">Education</h2>{edu}
<h2 class="rv" style="font-size:clamp(26px,3vw,34px);margin-top:56px">Experience</h2>{exp}</section>

<section><p class="label rv">Capabilities</p>
<h2 class="rv" style="font-size:clamp(24px,2.6vw,30px);margin-top:18px">Skill</h2>
<div class="skills">{skills}</div>
<h2 class="rv" style="font-size:clamp(24px,2.6vw,30px);margin-top:64px">Languages</h2>
<div class="langwrap block"><div class="langs">{langs}</div>{ring}</div></section>

<section id="work"><p class="label rv">Projects</p>
<h2 class="rv" style="margin-top:16px">My Project</h2>
<div class="slider rv">{slides}</div><div class="sctl">{dots}</div>
<div class="cta-row"><a class="btn" href="projects.html">View all projects &rarr;</a>
<a class="btn ghost" href="{GH}" target="_blank" rel="noopener">{GHI}GitHub</a></div></section>"""

open("index.html", "w").write(page("Home", home, "Home", spy=True))
open("projects.html", "w").write(
    page(
        "Projects",
        f'<section style="border:0"><p class="label">Projects</p>'
        f'<h1 style="font-size:clamp(40px,6vw,72px);margin-top:16px">My Project</h1>'
        f'<div class="grid">{"".join(card(p) for p in PROJECTS)}</div></section>',
        "Projects",
    )
)

for p in PROJECTS:
    n = p["n"]
    nx = PROJECTS[n % len(PROJECTS)]
    pv = PROJECTS[n - 2]
    b = (n - 1) * 4

    def g(k, c, cls=""):
        box = ph(image_path("img%d" % (b + k)), "%s %d" % (p["t"], k))
        return f'<figure class="rv {cls}">{box}<small>{c}</small></figure>'

    hero = ph(hero_img(p), p["t"] + " hero")
    gallery = "".join(
        g(k + 2, caption, "wide" if i == 0 else "")
        for i, (k, caption) in enumerate(zip(range(len(p["caps"])), p["caps"]))
    )
    work = (
        f'<section><h2 class="rv">The work</h2><div class="gal">{gallery}</div></section>'
        if gallery
        else ""
    )
    body = f"""<div class="phead"><div class="lead"><p class="label fu">Project 0{n} / {len(PROJECTS):02d}</p>
<h1 class="pname fu d1" style="font-size:clamp(44px,6.4vw,80px);margin:16px 0 18px">{p["t"]}</h1>
<p class="pcat fu d1">{p["cat"]}</p>
<p class="fu d2" style="max-width:620px;color:var(--mute);margin-top:18px">{p["sum"]}</p></div>
<div class="act fu d3"><a class="btn" href="{p["url"]}" target="_blank" rel="noopener">{GHI}View on GitHub</a></div></div>
<div class="rv" style="margin-top:48px">{hero}</div>
<div class="meta"><div><b>Role</b>{p["role"]}</div><div><b>Year accomplished</b>{p["year"]}</div>
<div><b>Link</b><a href="{p["url"]}" target="_blank" rel="noopener">{p["url"].replace("https://", "")}</a></div></div>
<h2 class="rv desch">Project Description</h2>
<p class="rv descp">{p["desc"]}</p>
{work}
<section class="nextwrap"><div class="pnav">
<a class="pnavbtn back" href="{pv["f"]}">{NAV_BACK}<span><small>Back</small><b>{pv["t"]}</b></span></a>
<a class="pnavbtn" href="{nx["f"]}"><span><small>Next</small><b>{nx["t"]}</b></span>{NAV_NEXT}</a>
</div></section>"""
    open(p["f"], "w").write(page(p["t"], body, "Projects"))

print("built:", ", ".join(["index.html", "projects.html"] + [p["f"] for p in PROJECTS]))
