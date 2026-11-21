#!/usr/bin/env python3
"""
GitHub Profile README Generator for ashishkumar0724
Creates the complete directory structure and files for the Git-Koi + Bonsai + Stats profile.
Idempotent: Safe to run multiple times. Will warn before overwriting existing files.
"""

import pathlib
import sys

# --- CONFIGURATION ---
GITHUB_USERNAME = "ashishkumar0724"

# --- FILE DEFINITIONS ---
FILES = {
    ".github/workflows/koi.yml": f"""name: Koi
on:
  schedule:
    - cron: "20 0 * * *" # Runs just after midnight UTC
  workflow_dispatch:
  push:
    paths: [.github/workflows/koi.yml]

permissions:
  contents: write

concurrency: koi

jobs:
  koi:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: yalongwastaken/git-koi@v1
        with:
          body: white # Options: white, black, asagi, tea, gold, platinum
          output-dir: koi
      - name: Commit the koi if it changed
        shell: bash
        run: |
          git add koi/koi.gif
          if git diff --cached --quiet; then
            echo "The koi is unchanged; nothing to commit."
            exit 0
          fi
          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git commit --quiet --message "koi: draw the day's koi"
          git push --quiet
""",

    ".github/workflows/cards.yml": f"""name: Cards
on:
  schedule:
    - cron: "40 0 * * *" # Staggered 20 mins after koi to prevent git push race conditions
  workflow_dispatch:
  push:
    paths: [.github/workflows/cards.yml]

permissions:
  contents: write

concurrency: cards

jobs:
  cards:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Draw the stats card, light
        uses: stats-organization/github-readme-stats-action@v2.1.0
        with:
          card: stats
          options: username={GITHUB_USERNAME}&hide_border=true&disable_animations=true&bg_color=00000000&title_color=4a32a6&text_color=1f2328&icon_color=1257ab&card_width=400&show_icons=true&rank_icon=github&ring_color=4a32a6
          path: cards/stats-light.svg
          fail_on_error: "true"

      - name: Draw the stats card, dark
        uses: stats-organization/github-readme-stats-action@v2.1.0
        with:
          card: stats
          options: username={GITHUB_USERNAME}&hide_border=true&disable_animations=true&bg_color=00000000&title_color=a98ff7&text_color=c9d1d9&icon_color=7ccdf2&card_width=400&show_icons=true&rank_icon=github&ring_color=a98ff7
          path: cards/stats-dark.svg
          fail_on_error: "true"

      - name: Draw the languages card, light
        uses: stats-organization/github-readme-stats-action@v2.1.0
        with:
          card: top-langs
          options: username={GITHUB_USERNAME}&hide_border=true&disable_animations=true&bg_color=00000000&title_color=4a32a6&text_color=1f2328&icon_color=1257ab&card_width=400&layout=compact&size_weight=0&count_weight=1&langs_count=6
          path: cards/languages-light.svg
          fail_on_error: "true"

      - name: Draw the languages card, dark
        uses: stats-organization/github-readme-stats-action@v2.1.0
        with:
          card: top-langs
          options: username={GITHUB_USERNAME}&hide_border=true&disable_animations=true&bg_color=00000000&title_color=a98ff7&text_color=c9d1d9&icon_color=7ccdf2&card_width=400&layout=compact&size_weight=0&count_weight=1&langs_count=6
          path: cards/languages-dark.svg
          fail_on_error: "true"

      - name: Commit the cards if they changed
        shell: bash
        run: |
          git add cards/
          if git diff --cached --quiet; then
            echo "The cards are unchanged; nothing to commit."
            exit 0
          fi
          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git commit --quiet --message "cards: draw the day's cards"
          git push --quiet
""",

    ".github/workflows/bonsai.yml": """name: Bonsai
on:
  schedule:
    - cron: "0 3 * * *" # Runs at 3 AM UTC
  workflow_dispatch:
  push:
    paths: [.github/workflows/bonsai.yml]

permissions:
  contents: write

concurrency: bonsai

jobs:
  grow:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: egorthinks/git-bonsai@bec04c39f62731fdb28c3b82322ef21cbf3bdfac
        with:
          commit: 'false' # We handle the commit manually to check for changes
      - name: Commit the bonsai if it changed
        shell: bash
        run: |
          git add output/
          if git diff --cached --quiet; then
            echo "Bonsai unchanged — nothing to commit"
            exit 0
          fi
          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git commit --quiet --message "chore: tend the bonsai 🌳"
          git push --quiet
""",

    "README.md": f"""<!-- Top Section: Koi and Bonsai -->
<a href="https://github.com/yalongwastaken/git-koi">
  <img src="koi/koi.gif" align="right" width="45%" alt="My koi, redrawn every night from the day's activity">
</a>

<a href="https://egorthinks.github.io/git-bonsai/?u={GITHUB_USERNAME}">
  <img src="output/bonsai.gif" align="left" width="45%" alt="My GitHub bonsai swaying in the wind">
</a>
<br clear="all">

<!-- Bottom Section: Stats Cards (Light/Dark Mode Aware) -->
<a href="https://github.com/{GITHUB_USERNAME}#year-list-container">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="cards/stats-dark.svg">
    <img src="cards/stats-light.svg" align="left" width="45%" alt="GitHub stats">
  </picture>
</a>

<a href="https://github.com/{GITHUB_USERNAME}?tab=repositories">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="cards/languages-dark.svg">
    <img src="cards/languages-light.svg" align="right" width="45%" alt="Languages by repo count">
  </picture>
</a>
<br clear="all">

### Hi there, I'm Ashish Kumar 👋

I'm a developer passionate about building practical, technology-driven solutions. My recent work focuses on **Python**, **Machine Learning**, and **RAG (Retrieval-Augmented Generation)** systems, alongside interactive web experiences.

- 🔭 I’m currently working on: RAG-based chat applications and AI-powered database interfaces (like [`askmydb-mysql`](https://github.com/ashishkumar0724/askmydb-mysql)).
- 🌱 I’m currently learning: Advanced MLOps pipelines, drift detection, and scalable AI deployment.
- 💬 Ask me about: Python, Streamlit, LLM integrations, and building developer-friendly tools.
- 📫 How to reach me: [Add your email or LinkedIn here]

---
""",

    ".gitignore": """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Environment variables (best practice, even for profile repos)
.env
.env.local
""",

    "scripts/recolor.py": """#!/usr/bin/env python3
\"\"\"
Placeholder for custom bonsai recoloring script.
The default workflow works without this, but if you want to apply 
a custom palette (e.g., 'comet-night'), you can implement the 
image processing logic here using Pillow or similar.
\"\"\"
import sys

def main():
    print("Recolor script executed (placeholder). No changes made.")
    # Example: sys.argv[1] would be the 'output' directory

if __name__ == "__main__":
    main()
"""
}

def main():
    print("🚀 Starting GitHub Profile README setup for ashishkumar0724...")
    
    dirs_to_create = [
        ".github/workflows",
        "cards",
        "koi",
        "output",
        "scripts"
    ]
    
    for dir_path in dirs_to_create:
        path = pathlib.Path(dir_path)
        path.mkdir(parents=True, exist_ok=True)
        print(f"✅ Created directory: {dir_path}/")
        
        gitkeep = path / ".gitkeep"
        if not gitkeep.exists():
            gitkeep.touch()
            print(f"   └─ Added .gitkeep")

    for file_path, content in FILES.items():
        path = pathlib.Path(file_path)
        if path.exists():
            print(f"⚠️  File already exists, skipping: {file_path}")
            continue
        
        path.write_text(content, encoding="utf-8")
        print(f"✅ Created file: {file_path}")

    print("\n🎉 Setup complete!")
    print("👉 See the 'MANUAL CHANGES REQUIRED' section below before pushing to GitHub.")

if __name__ == "__main__":
    main()