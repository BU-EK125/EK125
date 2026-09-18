## For instructors: How to modify this jupyter book

This site is student-facing and permanent -- it stays up and publicly accessible indefinitely, not just for the current semester. Only add readings, lecture notes, GPPs (Group Practice Problems), and GPP solutions here. Do not add quizzes, tests/exams, homework, or IPPs (Individual Practice Problems) -- that material belongs on Blackboard or wherever your course keeps assessment content, not in this public repository. Even a page left out of `_toc.yml` still gets built to a public, directly-reachable URL, so "not linked from the sidebar" is not a safe way to keep something private -- if it shouldn't be public, don't add it here at all.

Most class pages are plain markdown files (`ClassN.md`); a few (like Classes 1 and 5) are executable Jupyter notebooks (`ClassN.ipynb`) with real, runnable code. The site executes every notebook fresh every time it builds (`execute_notebooks: force` in `_config.yml`) -- you never need to run a notebook yourself or save it with outputs baked in. Whatever your code actually produces when it runs is exactly what gets published. This also means a notebook whose code no longer runs will fail the build outright, which is exactly what the `pr-check` below catches before a broken notebook can reach `main`.

**Want the 🚀 "open in Colab" rocket icon on a page?** It only appears on pages that are actual Jupyter notebooks (`.ipynb`) -- a plain markdown page (`.md`) never gets it, no matter what's in it. To make a reading or GPP Colab-openable:
1. Author it as a `.ipynb` file, not `.md` (see Class 1 or Class 5's reading for the pattern -- explanatory text in markdown cells, real code in code cells).
2. Merge it to `main` at the exact path referenced in `_toc.yml`. The rocket button links straight to that file on GitHub's `main` branch, so it won't work from a branch that's still only in an open PR -- it 404s until merged.
3. No extra config needed beyond that -- `launch_buttons`/`repository` are already set up in `_config.yml` for the whole book, so any `.ipynb` page automatically gets the rocket icon once it's live on `main`.

Note that Colab runs the notebook live on Google's servers when a student clicks through and experiments with it -- that's a separate execution from the one that happens when the site itself builds, which is what non-Colab visitors see.

**To add or modify a reading:**

1. Create or edit the file at the top level of this repository, named `ClassN.md` (or `ClassN.ipynb` for an interactive version). For a notebook, just write real, working code -- there's nothing extra to do before saving; the site runs it for you at build time.
   - **Want a cell to intentionally raise an error** (e.g. demonstrating a bug or an exception on purpose)? Tag that cell `raises-exception`, or the build will treat the error as broken code and fail. In Jupyter/JupyterLab: View → Cell Toolbar → Tags, then type `raises-exception` into the tag box for that cell. See Class 1's `del x; print(x)` cell for a working example.
2. If you're adding a new page, add it to `_toc.yml`, following the pattern already there. A Group Practice Problem page goes in `gpps/` and is nested under its reading with a `sections:` entry, e.g.:
   ```yaml
   - file: Class5
     sections:
       - file: gpps/Class5_GPP
   ```
3. Open a pull request with your change rather than pushing directly to `main`. A GitHub Actions check (`pr-check`) runs automatically on every PR and builds the whole book -- since that build executes every notebook, any notebook whose code doesn't run cleanly will fail the check. Fix anything it flags before merging.
4. Once the PR is merged, GitHub Actions rebuilds and republishes the live site automatically -- no manual steps needed.

## https://BU-EK125.github.io/EK125/intro.html
