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
- **Act 2 = "Python in an IDE"**: starts around Class 9.
- **Act 3 = MATLAB**: starts at Class 16 (Python-to-MATLAB bridge class).
  Classes 16, 18, and 19's GPPs are `.md` pointers to third-party MathWorks
  interactive tutorials with their own built-in "reveal solution" UI --
  they have no separate GPP-solutions file by design, not a gap to fill.
  **This is stale as of 2026-10-20** -- see "Incoming curriculum change"
  below. Classes 16, 18, 19 are being replaced by a Python team project;
  MATLAB content's new slot (if any) is not yet determined.

## Incoming curriculum change: the Fitness Tracker team project (not yet ported)

As of 2026-10-20, `EK125-Instructors/F26/New Material Drafts/` has a
**complete draft** of a new multi-class team project, "EK125 Fitness
Tracker Analyzer," replacing live Classes 15-19 content (currently
"Visualizing Data and Plotting" at 15, MATLAB at 16/18/19) with a single
arc spanning **Classes 15-19 (Mon 10/26 - Mon 11/9 2026)**, plus a
plotting add-on at the already-scheduled Class 21 (Mon 11/16). Confirmed
against both `F26 Class Schedule.docx` files in `EK125-Instructors/F26/
Course Docs/` (identical content, no discrepancies) -- the new topic
titles below are the *official* schedule now, not just a draft idea.

- **The project**: teams of 3 build a 3-function program
  (`load_tracker_data`/`analyze_metric`/`write_report`, wired together by
  `main.py`) that reads a 28-day fitness-tracker CSV and writes a summary
  report. Fixed function signatures across all teams; everything else
  (blank-value handling, metrics/goals, dict keys, rounding, report
  format) is a team decision recorded in a **Team Contract** (template:
  `Class 15/Markdown/Team_Contract_Template.md`) that's amended
  continuously through Class 19 (Decision Log, Integration Log). Explicit
  "no new Python syntax" framing -- it's pure review of Classes 12-14
  (dictionaries, functions, file I/O), the new skill is collaboration
  (contracts-before-code, stubs, incremental integration, debugging
  someone else's code).
- **Per-class topics** (each has a complete `Preread.md` + `Team_Activity.md`
  + `Preclass_Assessment.md` + instructor notes + IPP/answer-key, all in
  `EK125-Instructors/F26/New Material Drafts/Class N/Markdown/`):
  - **Class 15** (Mon 10/26) -- Problem definition & initial decisions.
    Deliverable: Team Contract, due Tue 10/27.
  - **Class 16** (Wed 10/28) -- Stub building. Deliverable: running
    4-file skeleton, due Sun 11/1.
  - **Class 17** (Mon 11/2) -- Writing real functions (tests-before-code).
    Deliverable: real functions + tests, due Tue 11/3.
  - **Class 18** (Wed 11/4) -- Integrating it all together (one function
    at a time, "it runs" != "it's right"). Deliverable: working program +
    report, due Sun 11/8.
  - **Class 19** (Mon 11/9) -- Debugging & reflection (5-step debugging
    method, Start/Stop/Continue retrospective). Deliverable: bug log +
    reflection, due Tue 11/10.
  - **Class 21** (Mon 11/16, already on the schedule as "Visualizing data
    and plotting in Python") -- each teammate adds one plotting function
    to their team's program. **No draft content exists yet for this one**
    (checked -- only Classes 15-19 have `New Material Drafts/` folders).
- **Publish-eligibility note for whoever ports this**: this repo's rules
  (README.md) only allow readings, GPP problem statements, GPP solutions
  (Act 1 + 9-14 only), and HW problem statements -- so of this project's
  file set, `Preread.md` (-> `class/ClassN.md`) and `Team_Activity.md`
  (-> the GPP-equivalent) are plausibly publishable; `Preclass_Assessment`
  (a graded quiz) and `IPP`/`IPP_AnswerKey` (individual assessment --
  belongs in `EK1225-IPP`, never here) are not; `Instructor_Notes` is
  obviously private. Not yet decided/confirmed with the instructor which
  of these actually get ported, or whether Team_Contract_Template/
  FitnessTracker_Project_Overview get a shared page of their own -- ask
  before assuming.
- **As of 2026-10-20, nothing from this project has been ported** --
  `appendix/Fall2026Schedule.md`'s Week 9 row lists the new Class 15/16
  topic titles as plain, unlinked text (same pattern used for an
  unpublished Homework entry) so the calendar stays accurate, but
  `class/Class15.md` etc. on the live site still have the old content.
  Weeks 10-11 (Classes 17-19, Exam 2 practice/review) have not been added
  to the calendar yet either -- only "next week" (Week 9) was requested
  so far.

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
  2026-10-16 (see the GPP-solutions scope history above). Class 15 still
  has no GPP, by design, not a gap -- see if a genuine
  visualization/matplotlib group exercise ever surfaces before assuming
  one should be added.
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
