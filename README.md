# Piero's Portfolio

Personal portfolio website for Piero Christian Ronaldo, a Computer Science student at BINUS University on the AI track. The site brings together his background, experience, skills, and project case studies.

GitHub: [P1caro/Portfolio](https://github.com/P1caro/Portfolio)

## Features

- Responsive home page with profile, education, experience, skills, and projects
- Project carousel and dedicated case-study pages
- Light and dark themes with the selected theme saved in the browser
- Python build script that generates the static HTML pages from shared project data

## Built With

- HTML
- CSS
- JavaScript
- Python 3 (static page generator)

## Run Locally

From the project root, regenerate the HTML pages:

```bash
python build.py
```

Then start a local web server:

```bash
python -m http.server 8000
```

Open [http://localhost:8000](http://localhost:8000) in your browser.

## Updating Content

Edit `build.py` to update the portfolio content. Project entries are in the `PROJECTS` list; running `python build.py` regenerates the home page, project listing, and individual project pages. Shared layout and styles are in `css/style.css`, and interactive behavior is in `js/main.js`.

Place site images in the `image/` folder. Project images follow a four-image sequence: each project uses one cover image and up to three work-gallery images. For example, Portfolio uses `img21.jpeg` as its cover and `img22.jpeg` through `img24.jpeg` in its gallery. See `fonts/README.txt` for optional local font setup.
