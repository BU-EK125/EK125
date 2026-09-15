# Handoff: EK125 → executable notebooks + Colab launch buttons

## Goal

`EK125` (the course site at `/Users/briandepasquale/Documents/GitHub/EK125`) is a
JupyterBook / Sphinx-book-theme site. Its pages are currently *plain* Markdown
(`Week*.md`), not real notebooks, so there's nothing executable behind them and
no "Open in Colab" button.

The plan: convert readings into real `.ipynb` notebooks so JupyterBook can
actually execute the code at build time (catching broken code automatically)
and so a `launch_buttons` / Colab config can let students open and run any
page live.

This work is happening in a **separate repo** (`EK125-notebooks`) so the main
course repo isn't touched during the pilot.

## Decisions made (via user Q&A this session)

- **Scope**: pilot **one file first** (`Week10A.md`) end-to-end before touching
  the other ~24 `Week*.md` files. Prove the pipeline works, then decide whether
  to roll out further.
- **Format**: real **`.ipynb`** files (not MyST-Markdown-notebook / Jupytext
  paired `.md`). User explicitly chose `.ipynb` over the diff-friendlier MyST
  option.
- **Execution**: JupyterBook should **execute notebooks at build time**
  (`execute_notebooks: force` in `_config.yml`), not just embed static
  pasted-in output.
- **Repo**: work happens in a **new repo**, `EK125-notebooks`, containing a
  **full copy** of the current EK125 site (not a minimal skeleton).
- **Hosting**: **local repo only** — do NOT create a GitHub remote or push.
  The user will create the GitHub repo and push it themselves.

## What's been done so far

1. Created `/Users/briandepasquale/Documents/GitHub/EK125-notebooks`, a fresh
   local git repo (`git init`, no remote configured).
2. Copied all git-tracked files from `EK125` into it. Two files needed manual
   fixing because `rsync --files-from=-` silently dropped them:
   - `intro.md` (root doc referenced by `_toc.yml`'s `root:` — build fails
     without it)
   - `images/Class1B/*.png` (5 files)
   Both were copied manually and committed.
3. Commits so far, in order:
   - `Initial copy of EK125 course content`
   - `Add tracked image files`
   - `Add missing intro.md`
4. Set up a Python venv at `EK125-notebooks/.venv` and installed:
   - **`jupyter-book<2`** (resolved to `1.0.4.post1`) — **important**: plain
     `pip install jupyter-book` installs JupyterBook **v2**, which is a full
     MyST-based rewrite with an incompatible config format (`myst.yml`
     instead of `_config.yml`/`_toc.yml`, different CLI). This repo's
     `_config.yml`/`_toc.yml` are the **classic v0.x/v1.x Sphinx-based**
     format (sphinx-book-theme, `execute.execute_notebooks`), so the
     dependency must stay pinned below v2.
   - `nbformat`, `jupytext`, `ipykernel`, `matplotlib`, `numpy`, `pandas`
5. Ran a **baseline build** (`./.venv/bin/jupyter-book build .`) on the
   as-copied site — **succeeded** (123 non-fatal warnings, mostly
   non-consecutive-header-level MyST warnings). Confirms the copy is a valid
   starting point before any notebook conversion.
6. Did **not yet** add a `.gitignore` — `.venv/` and `_build/` are currently
   untracked-but-present and should be excluded before the next commit (the
   baseline build also copied a bunch of `.venv/.../a11y_pygments/*.png`
   theme assets into `_build/html/_images/`, which is harmless but noisy).

## Detailed analysis of Week10A.md (not yet converted)

`Week10A.md` is 911 lines with ~40 ` ```python ` fenced code blocks. It's a
*reading*, not a script meant to run top-to-bottom — some blocks are
self-contained, some deliberately show broken/anti-pattern code, and some
read files that are never created anywhere in the document. Naively turning
every fence into a live cell and forcing execution would crash the build.

Plan worked out (not yet implemented):

- **Safe cells** (convert directly, no changes needed): pure string/path
  assignments, `os.getcwd()`, and any self-contained `"w"`/`"a"` mode file
  write (these don't require a pre-existing file).
- **Hidden setup cells needed** before the *first* real "good" read of a file
  that's never written earlier in the doc: `data.txt`, `data/readings.txt`,
  `story.txt`, `names.txt`, `grades.txt`, `numbers.txt`, `contacts.txt`.
  Plan: insert a tiny cell immediately before each first read that writes
  placeholder content, tagged `remove-cell` so it's hidden from the built
  HTML page (keeps the reading's visual flow identical to today) but still
  present and functional when a student opens the raw `.ipynb` in Colab
  (Colab doesn't understand `remove-cell`, so it needs the real setup to run
  standalone).
- **`raises-exception` tag needed** on a few genuine, *uncaught* error-demo
  cells so nbclient permits the exception and still renders the real
  traceback instead of failing the whole build:
  - the "Avoid: absolute path" example (path won't exist on any machine)
  - "WRONG: Opening a binary file in text mode" (`photo.jpg` never exists)
  - the bare `missing.txt` open in Appendix B (not wrapped in try/except)
  Most of the other error-adjacent examples (`missing.txt`, `protected.txt`,
  multiple-exception-types demo) are already wrapped in their own
  `try/except` in the source text, so they're self-handling and don't need
  a tag.
- **Do NOT execute as code** — one block is pure pseudocode with undefined
  placeholder functions:
  ```python
  try:
      risky_operation()
  except SomeError:
      handle_the_error()
  ```
  `risky_operation`/`handle_the_error`/`SomeError` are never defined; running
  this raises `NameError`. Keep it as an inert fenced block inside a markdown
  cell, not a live code cell.
- **Flagged but not fixed**: a pre-existing accuracy issue in the source
  content itself (unrelated to the notebook conversion, worth a decision from
  the user). The "WRONG: not stripping whitespace" example in section 12
  claims `int(line)` "will fail due to newline character" — but Python's
  `int()` strips surrounding whitespace/newlines automatically
  (`int("10\n") == 10`), so a normal numeric line with a trailing newline
  will *not* actually raise. Only a genuinely blank/non-numeric line would.
  Under real execution this "WRONG" demo won't demonstrate a failure unless
  the sample file is deliberately given a bad line. Not yet resolved — worth
  asking the user whether to leave as a (harmless, `raises-exception`-tagged)
  cell that just happens not to raise, or to tweak the sample data so it
  actually reproduces the claimed failure.

## Not yet done

- Actually build `Week10A.ipynb` from the plan above (nbformat script was
  about to be written when the pivot to this new repo/handoff happened).
- Execute the notebook and iterate until it runs clean end to end.
- Delete the old `Week10A.md` (JupyterBook resolves `_toc.yml`'s
  `file: Week10A` entry to whichever extension exists — can't have both).
- Update `_config.yml`:
  - `execute.execute_notebooks: force`
  - add `launch_buttons.colab_url: "https://colab.research.google.com"`
  - add `repository.url` / `repository.branch` — **note**: this should
    eventually point at wherever `EK125-notebooks` gets pushed on GitHub
    (not the original `EK125` remote, `https://github.com/depasquale-lab/EK125.git`),
    since Colab links are built from that repository URL. Needs the actual
    new repo URL once the user creates/pushes it.
- Add a `.gitignore` for `.venv/` and `_build/`.
- Rebuild the full site and manually verify: the launch/Colab button appears
  on the Week10A page, the notebook's outputs render as real executed output
  (not static text), and no other pages regressed.
- Decide, based on how the pilot goes, whether/how to roll the same treatment
  out to the other ~24 `Week*.md` files (this was intentionally deferred
  until the pilot proves out).

## Key facts / paths

- Original course repo: `/Users/briandepasquale/Documents/GitHub/EK125`
  (remote: `https://github.com/depasquale-lab/EK125.git`) — untouched by this
  work.
- New pilot repo: `/Users/briandepasquale/Documents/GitHub/EK125-notebooks`
  — local git repo, **no remote configured yet**, 3 commits so far.
- Venv: `EK125-notebooks/.venv` (not committed — should be gitignored),
  `jupyter-book` pinned to `<2`.
