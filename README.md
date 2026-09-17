## For instructors: How to modify this jupyter book

This site is student-facing and permanent -- it stays up and publicly accessible indefinitely, not just for the current semester. Only add readings, lecture notes, GPPs (Group Practice Problems), and GPP solutions here. Do not add quizzes, tests/exams, homework, or IPPs (Individual Practice Problems) -- that material belongs on Blackboard or wherever your course keeps assessment content, not in this public repository. Even a page left out of `_toc.yml` still gets built to a public, directly-reachable URL, so "not linked from the sidebar" is not a safe way to keep something private -- if it shouldn't be public, don't add it here at all.

Most class pages are plain markdown files (`ClassN.md`); a few (like Class 5) are executable Jupyter notebooks (`ClassN.ipynb`) with real, runnable code and their output already baked in.

**To add or modify a reading:**

1. Create or edit the file at the top level of this repository, named `ClassN.md` (or `ClassN.ipynb` for an interactive version). This repo does not execute notebooks when it builds (`execute_notebooks: "off"` in `_config.yml`), so if you're editing a notebook, run it yourself first and save it with the outputs you want shown -- whatever's baked in is exactly what students will see.
2. If you're adding a new page, add it to `_toc.yml`, following the pattern already there. A Group Practice Problem page goes in `gpps/` and is nested under its reading with a `sections:` entry, e.g.:
   ```yaml
   - file: Class5
     sections:
       - file: gpps/Class5_GPP
   ```
3. Open a pull request with your change rather than pushing directly to `main`. A GitHub Actions check (`pr-check`) runs automatically on every PR: it builds the whole book, and for any changed notebook, verifies it actually executes end to end. Fix anything it flags before merging.
4. Once the PR is merged, GitHub Actions rebuilds and republishes the live site automatically -- no manual steps needed.

## https://BU-EK125.github.io/EK125/intro.html
