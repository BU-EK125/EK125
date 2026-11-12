# Cross-repo context for EK125

This file exists to carry over knowledge from work done across the wider
EK125 repo ecosystem that isn't written down in this repo's own README.md
or CONVENTIONS.md (both of which are authoritative for this repo's own
porting patterns, cross-reference/common-mistake auditing standards, and
the GPP-solutions porting pattern -- read those first, don't duplicate them
here).

## The repo map (BU-EK125 org, unless noted)

- **EK125** (this repo) -- the main, public, permanent jupyter-book site.
  Student-facing. Canonical source for reading content, GPP problem
  statements, and (Fall 2026 on) homework problem statements and GPP
  solutions for Act 1 (Classes 1-7), plus Classes 9-14 (added
  2026-10-02, 2026-10-05, and 2026-10-16 by explicit instructor request --
  see README.md for the authoritative scope statement; this is not a
  general Act 2
  reopening).
- **EK125-notebooks** (private) -- the instructor-side staging/source repo
  most content here gets ported *from*. Itself built as a second,
  internal-only jupyter-book site (has its own `_config.yml`/`_toc.yml`).
  Not always trustworthy as-is -- files there have repeatedly turned out
  stale or polluted (worked answers baked into what should be blank GPP
  scaffolds, old grading rubrics, joke placeholder names). Always
  cross-check against what students are actually currently given before
  trusting it as source. It also has two gitignored folders, `/HWs/` and
  `/ipp/`, holding real homework and IPP solutions -- never referenced by
  its own `_toc.yml`, never to be copied anywhere public.
- **EK125-C1-DePasquale-Slides** (public) -- marimo slide decks: one
  lecture-through-the-reading deck per class from Class 6 on, with
  built-in GPP-sourced quick-checks. Classes 2-4 predate that format
  (lecture-only, no quick-checks).
- **EK1225-IPP** (public; typo'd name, "1225" not "125", permanent/live --
  inherited from a local folder name, not worth renaming now) -- a sibling
  site cloned from the Slides repo's pattern, publishing per-class
  Individual Practice Problem (IPP) handouts as marimo decks. Convention
  established there: **IPP decks show the questions only, no answer
  reveal** (unlike GPP decks, which may reveal answers) -- IPPs are
  individual assessments, kept as blank practice worksheets by deliberate
  choice.
- **EK125-hw-help**, **EK125-discussions** (public) -- companion sites for
  homework-help-session and discussion-section notebooks. Not yet audited
  by any Claude session as of this writing; check their own README/
  CONVENTIONS (if any) before assuming this file's conventions apply.
- **EK125-Instructors** (private) -- the raw-material working repo, organized
  by semester (`S26`, `F25`, `F26`, `copyOfShared`). **This was transferred
  from a personal repo (`briandepasquale/EK125WIP`) into the org and
  renamed** -- same repo, same git history, formerly known as "EK125WIP" in
  older notes/transcripts. A local checkout's remote may still point at the
  old `briandepasquale/EK125WIP.git` URL (pushes still work via GitHub's
  redirect, but should be repointed to
  `https://github.com/BU-EK125/EK125-Instructors.git` when convenient). This
  is upstream of EK125-notebooks -- GPP solutions in EK125-notebooks were
  minted from files here. Also where next-semester (F26) marimo lecture-deck
  drafts for Classes 2-4 already exist (`F26/Class N/Slides/`), not yet
  pushed to EK125-C1-DePasquale-Slides -- check there before redrafting a
  deck for one of those classes.

## Course structure (Acts)

- **Act 1 = "Python in Colab"**: Classes 1-7. Class 8 does not exist by
  design (numbering jumps 7 to 9).
- **Act 2 = "Python in an IDE"**: Classes 9-14.
- **Classes 15-19 = the "Fitness Tracker Analyzer" team project**, its own
  `_toc.yml` caption ("Team Project: Fitness Tracker") between "Python in
  an IDE" and "MATLAB" -- see "The Fitness Tracker team project" below.
- **Act 3 = MATLAB**: Class 21 (visualization, in Python) leads into
  Class 22 (the Python-to-MATLAB bridge class), then vectors/matrices,
  scripts, and user-defined functions through Class 26. **This is a
  renumbering of what used to be Classes 15/16/18/19/20/21** -- see
  "Renumbering" below before assuming any `ClassN.md` file's number is
  stable across sessions from before 2026-10-23.

## The Fitness Tracker team project (ported 2026-10-23)

`EK125-Instructors/F26/New Material Drafts/` has a complete draft of a
multi-class team project, "EK125 Fitness Tracker Analyzer," occupying
**Classes 15-19 (Mon 10/26 - Mon 11/9 2026)**, plus a plotting add-on at
Class 21 (Mon 11/16, not yet drafted -- see "Known open items"). Confirmed
against `EK125-Instructors/F26/Course Docs/F26 Class Schedule.docx`
(extracted via `zipfile`+`xml.etree.ElementTree` on `word/document.xml`,
since this repo has no docx reader) -- that schedule is the single source
of truth for every class number from here through the end of the
semester (Class 27, Exam 3 practice).

- **The project**: teams of 3 build a 3-function program
  (`load_tracker_data`/`analyze_metric`/`write_report`, wired together by
  `main.py`) that reads a 28-day fitness-tracker CSV and writes a summary
  report. Fixed function signatures across all teams; everything else
  (blank-value handling, metrics/goals, dict keys, rounding, report
  format) is a team decision recorded in a **Team Contract** that's
  amended continuously through Class 19 (Decision Log, Integration Log).
  Explicit "no new Python syntax" framing -- it's pure review of Classes
  12-14 (dictionaries, functions, file I/O); the new skill is
  collaboration (contracts-before-code, stubs, incremental integration,
  debugging someone else's code).
- **Published, by explicit instructor direction** (prereadings are normal
  readings; the Project Overview applies across all five classes and gets
  its own page; Team Activity files are the per-day deliverable,
  structured as Morning + Afternoon sections; downloadable files should be
  `.md`, not `.docx`):
  - `class/FitnessTrackerProject.md` -- standalone page (not nested under
    any one class), first chapter in the new caption, ported from
    `FitnessTracker_Project_Overview.md`.
  - `class/Class15.md` through `class/Class19.md` -- ported from each
    class's `Preread.md`.
  - `gpps/Class15_TeamActivity.md` through `gpps/Class19_TeamActivity.md`
    -- ported from each class's `Team_Activity.md`. Named `_TeamActivity`,
    not `_GPP`, and **never paired with a `.py` scaffold** -- there is no
    starter code to give out, teams write their files from scratch against
    their own contract. See CONVENTIONS.md's "Team Activity pages" section
    for the full pattern.
  - `gpps/fitness_data.csv` and `gpps/Team_Contract_Template.md` (the
    `.md` source, not the `.docx` export -- downloadable files in this
    project are markdown per instructor direction) -- both linked from
    Class 15's Team Activity page.
  - Three in-class debugging exercises, each a small multi-file Python
    program with planted bugs, copied into their own subfolder under
    `gpps/` (filenames collide across them -- all three have their own
    `loader.py`/`analyzer.py`/`main.py`/`reporter.py` -- hence the
    subfolders) and linked from the relevant Team Activity page:
    `gpps/class16_broken_skeleton/` (3 bugs, linked from Class 16),
    `gpps/class18_integration_clinic/` (1 silent bug: `loader.py` checks
    each column for blanks independently instead of skipping the whole
    row, so `"day"` ends up longer than the other lists and everything
    after the first blank row is misaligned -- explains why the best
    step-day comes out as Day 25 instead of the correct Day 27, linked
    from Class 18), `gpps/class19_team7_bug_hunt/` (5 bugs + an
    `expected_report.txt` to diff against, linked from Class 19). All
    three reuse the single `gpps/fitness_data.csv` rather than duplicating
    an identical copy (confirmed byte-identical via `diff` before relying
    on that).
  - Verified every one of the project's numeric claims against the real
    `fitness_data.csv` before publishing (the Class 18 "data facts" table:
    25 complete days, steps avg 8843.4/min 4569/max 14773/best day 27,
    resting HR avg 63.0/min 58/max 67/best day 14, sleep min 5.7/max
    8.9/best day 7, active-minutes avg 41.4/best day 7 -- all confirmed
    correct via an independent Python recomputation). No bugs found in the
    project's own content (unlike the Class 13/14 GPP ports -- this
    material was clean).
  - **Not published**: `Preclass_Assessment` (a graded quiz) and
    `IPP`/`IPP_AnswerKey` (individual assessment -- belongs in
    `EK1225-IPP`, never here) -- not mentioned by the instructor's
    direction and excluded consistent with this repo's existing
    no-quizzes/no-IPP policy. `Instructor_Notes` obviously private too.
- **Cross-reference links added**: Class 15's reading links to Class 12
  (`#dictionaries`), Class 13 (`#part-1-user-defined-functions-morning`),
  and Class 14 (`#part-2-file-input-and-output-i-o`); Class 16 additionally
  links back to Class 5 (`#what-is-a-module`) and Class 14
  (`#the-if-name-main-pattern`); Class 17 and Class 18 link forward/back to
  Class 15's Team Activity page's hand-calculation section
  (`gpps/Class15_TeamActivity.html#part-e-work-out-the-expected-answers-
  by-hand-about-20-minutes-together`).

## Renumbering (2026-10-23): Classes displaced by the Fitness Tracker project

The Fitness Tracker project's slot (Classes 15-19) was previously occupied
by other live content, which got renumbered forward rather than deleted,
per the confirmed mapping in the official `F26 Class Schedule.docx`:

| Old number | New number | Topic |
|---|---|---|
| 15 | 21 | Visualizing Data and Plotting in Python |
| 16 | 22 | From Python to MATLAB: Syntax and Plotting |
| 18 | 23 | Creating Vectors and Matrices in MATLAB |
| 19 | 24 | Vector and Matrix Operations in MATLAB |
| 20 | 25 | MATLAB Scripts, Documentation, and File I/O |
| 21 | 26 | User Functions and Modular Programming in MATLAB |

Each move was a `git mv` (processed in descending old-number order so a
later move never overwrote a file still waiting to be moved out of its
target slot) plus a one-line edit to that file's own `# Class N:` title
heading -- no other content changed, and none of these files had internal
cross-references to other class numbers (checked by grep before moving).
**Old Class 22 ("Useful MATLAB Toolboxes") has no confirmed new slot** --
the official schedule's last two classes are 26 (User Functions, above)
and 27 (Exam 3 practice, no matching content) -- so it was moved to
`archive/Class22_UsefulMATLABToolboxes.md` rather than guessed into a
number. `intro.md`'s Act 3 description also dropped its "tour of MATLAB's
toolboxes" line for the same reason -- don't re-add it without a confirmed
slot for this content.

## Toolchain trap

`pip install jupyter-book` installs v2.x by default, an incompatible
ground-up MyST rewrite (`myst.yml`, new CLI) that does NOT work with this
repo's classic `_config.yml`/`_toc.yml` Sphinx-book-theme format. Always
pin `jupyter-book<2` (currently built against 1.0.4).

## Build-breaking trap: link-only headings

A Markdown/MyST heading whose entire text is a link -- e.g. `## [HW5.py
](HW5.py)` -- crashes the whole `jb build` with `KeyError: 'anchorname'`
deep in Sphinx's `document_toc` (building that page's own sidebar
"Contents"). It's not a warning, it's a hard build failure, and the
traceback's "Last messages" can point at a totally unrelated page (the
crash surfaces wherever Sphinx next touches the global toctree, not
necessarily the page with the bad heading) -- bisect by reverting changes
one file at a time if you hit this blind. The fix: never make a heading's
full text a link. Put the link in the body text below the heading instead
(e.g. `## Download the Assignment File` followed by `Download: [HW5.py
](HW5.py)` as a separate line). Found while adding download-file headings
to `homework/HW5.md` and `gpps/Class9_GPP.ipynb`.

## PII lesson (critical)

Raw notebook files sourced from EK125-notebooks (or further upstream,
EK125-Instructors) can carry real personal information in Colab execution metadata
-- `executionInfo.user.displayName`/`userId` per cell, `colab.provenance`
at the notebook level. **Never copy a cell directly from an upstream
source into this repo.** Always rebuild each cell from scratch, keeping
only `cell_type` and the joined `source` text, with fresh minimal metadata
(`{"id": <new-uuid>}`). See this repo's own CONVENTIONS.md for the full
porting-pattern writeup.

## Orphaned legacy files

This repo predates its current `ClassN.md`/`ClassN.ipynb` naming --
content was originally organized as `Week1A`/`Week1B` ... `Week15B` before
being renamed. Old `Week*.md` files may still exist in the repo unreferenced
by `_toc.yml` and unbuilt -- don't mistake one for live content if you find
it; check `_toc.yml` to see what's actually published.

## Process lessons from repo history

- **Verify which remote a local checkout tracks** before treating it as
  source-of-truth for seeding or comparing against another repo -- a
  personal fork can silently diverge (missing recent renames/restructures,
  or carrying unpushed local-only edits) from the canonical `BU-EK125/EK125`
  origin.
- **Before bulk-copying content into a sibling repo** (e.g. EK125-notebooks
  or EK125-Instructors/EK125WIP), check the destination's own `git log`/`git status` first --
  a blind copy can clobber already-completed, already-pushed work that a
  different session did in the meantime.
- When converting a static reading into an executed notebook, watch for
  prose that reads a file before another cell has written it (needs a
  hidden setup cell inserted first for correct sequential execution), and
  never try to execute pure pseudocode blocks (undefined placeholder
  functions) -- those need `skip-execution`, not a real run.
- **GPP-solutions scope was extended to Classes 9-10 on 2026-10-02**, by
  explicit instructor request in a Claude Code session -- previously Act 1
  (Classes 1-7) only. `Class9_GPP_Solutions.ipynb` and
  `Class10_GPP_Solutions.md`/`.py` were ported from EK125-notebooks'
  `gpp/Class_9_GPP_Solutions.*`/`gpp/Class_10_GPP_Solutions.*` after
  cross-checking them line-for-line against the current public GPPs.
- **Scope extended again to Classes 11-12 on 2026-10-05**, by explicit
  instructor request. Unlike Classes 9-10, Classes 11-12 didn't have a
  public GPP at all yet -- both the GPP and its solutions were ported
  together, as new `.py`/`.md` script-based pairs (per CONVENTIONS.md's
  "Script-based pages" section), sourced from `EK125-Instructors/F26/`
  (the freshest copies, "just received from the instructor" per the
  request) and cross-checked against EK125-notebooks' `gpp/
  Class_11_GPP*`/`gpp/Class_12_GPP*` (older, notebook-format versions with
  identical problem content). Found and fixed a real bug while verifying
  Class 11's solutions: Challenge 1 asks to sum values "greater than or
  equal to 4" but both sources' solution code used `v > 4` (strict),
  silently dropping the boundary value -- fixed to `v >= 4`.
- **Scope extended again to Classes 13-14 on 2026-10-16**, by explicit
  instructor request, after a newly-drafted `EK125-Instructors/F26/Copy of
  class14_gpp.py` turned out to reproduce the exact Class 13/14 topic
  mismatch described below under "Known open items" -- Class 13's GPP was
  ported straight from that same WIP batch (clean, matches its reading),
  but Class 14's GPP was instead sourced from EK125-notebooks' `gpp/
  Class_14_GPP.py`/`_Solutions.py` (the version already correctly fixed
  there in September). Verifying Class 14's solutions end-to-end surfaced
  four more real bugs, all fixed: two crashes (top-level illustrative code
  using undefined variables; a `credits`/`course_credits` typo causing a
  `NameError`) and two wrong docstring example outputs (`3.72` should be
  `3.67`; `83.5` should be `83.50333333333333`). Do not extend further
  into Act 2 (Class 15) or Act 3 without being asked again.

## Known open items worth checking before assuming fixed

- ~~Class 14 and 15's GPPs were found misaligned with their own readings by
  one class~~ -- **resolved 2026-10-16.** This was already fixed once, in
  EK125-notebooks (2026-09-16, commits `2a8590a`/`a131231`): Class 14's slot
  had Class 13's scope/copying content, and Class 15's slot had content
  ("Scripts, Comments, and Documentation") that actually matched Class 14's
  reading -- moved into Class 14's slot, Class 15's GPP deleted (no
  replacement existed). That fix never made it into this repo's own
  `CLAUDE.md` or into `EK125-Instructors`, which is why a freshly-drafted
  WIP file for Class 14 reproduced the *exact same* mismatch again on
  2026-10-16 (see the GPP-solutions scope history above). **Note: this
  bullet is about the old Class 13/14 scope-porting mismatch, not the
  2026-10-23 Fitness Tracker renumbering** -- Class 15 (the number) now
  refers to a completely different reading than either of those; see
  "The Fitness Tracker team project" above.
- **Class 21's plotting add-on has no draft content yet.** The Fitness
  Tracker Project Overview and the Class 19 Team Activity's homework note
  both describe Class 21 (Mon 11/16) as "each teammate adds one plotting
  function to their project," and the live `class/Class21.md` (renumbered
  from old Class 15) already covers matplotlib -- but no `Class21
  _TeamActivity`-equivalent exists yet, because `EK125-Instructors/F26/New
  Material Drafts/` only has folders for Classes 15-19. Check there again
  before Class 21's actual date approaches.
- **Old Class 22 ("Useful MATLAB Toolboxes") is sitting in `archive/`
  with no confirmed new slot** (see "Renumbering" above) -- the official
  schedule's last class is 27 ("Exam 3 practice"), which doesn't match
  this content at all. Ask the instructor where (or whether) this belongs
  before either restoring it or deleting it outright.
- A reading's "WRONG" example once claimed `int(line)` fails on a file
  read's trailing newline -- Python's `int()` actually tolerates trailing
  whitespace, so the demo may not raise as the prose claims. Worth
  spot-checking Class 14's file-I/O reading if you're ever in that content.
- A pedagogical sequencing critique was raised for Classes 1-4: `input()`/
  type-casting aren't formally taught until Class 4, even though Class 3's
  examples rely on them conceptually, and Class 4 opens by admitting it's
  a "wrap-up... retread some ground" catch-up class. Not acted on as of
  this writing -- a design question for the instructor, not a bug to fix
  unilaterally.

## Sidebar bug to watch for

A class page with **more than one top-level `#` (H1) heading** (instead of
`##` for its major sections) silently drops its nested TOC children from
the sidebar -- the page still builds cleanly with no warning and is
directly reachable, it's just invisible in navigation. Fixed once already
for `class/Class4.md`; if a future class's GPP/Solutions seem to build
fine but don't show up in the sidebar, check this first.
