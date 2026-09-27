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
  statements, and (Fall 2026 on) homework problem statements and Act 1
  (Classes 1-7) GPP solutions.
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
- **EK125-Instructors** (private) -- exists, purpose not yet documented by
  any Claude session.
- **EK125WIP** (`briandepasquale/EK125WIP`, personal, NOT under the BU-EK125
  org) -- the actual raw-material working folder, organized by semester
  (`S26`, `F25`, `F26`, `copyOfShared`). This is upstream of
  EK125-notebooks -- GPP solutions in EK125-notebooks were minted from
  files here. Also where next-semester (F26) marimo lecture-deck drafts
  for Classes 2-4 already exist (`F26/Class N/Slides/`), not yet pushed to
  EK125-C1-DePasquale-Slides -- check there before redrafting a deck for
  one of those classes.

## Course structure (Acts)

- **Act 1 = "Python in Colab"**: Classes 1-7. Class 8 does not exist by
  design (numbering jumps 7 to 9).
- **Act 2 = "Python in an IDE"**: starts around Class 9.
- **Act 3 = MATLAB**: starts at Class 16 (Python-to-MATLAB bridge class).
  Classes 16, 18, and 19's GPPs are `.md` pointers to third-party MathWorks
  interactive tutorials with their own built-in "reveal solution" UI --
  they have no separate GPP-solutions file by design, not a gap to fill.

## Toolchain trap

`pip install jupyter-book` installs v2.x by default, an incompatible
ground-up MyST rewrite (`myst.yml`, new CLI) that does NOT work with this
repo's classic `_config.yml`/`_toc.yml` Sphinx-book-theme format. Always
pin `jupyter-book<2` (currently built against 1.0.4).

## PII lesson (critical)

Raw notebook files sourced from EK125-notebooks (or further upstream,
EK125WIP) can carry real personal information in Colab execution metadata
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
  or EK125WIP), check the destination's own `git log`/`git status` first --
  a blind copy can clobber already-completed, already-pushed work that a
  different session did in the meantime.
- When converting a static reading into an executed notebook, watch for
  prose that reads a file before another cell has written it (needs a
  hidden setup cell inserted first for correct sequential execution), and
  never try to execute pure pseudocode blocks (undefined placeholder
  functions) -- those need `skip-execution`, not a real run.

## Known open items worth checking before assuming fixed

- **Class 14 and 15's GPPs were found misaligned with their own readings by
  one class** (Class 14's GPP covered Class 13's scope/argument-passing
  material) in an earlier audit. Not confirmed fixed -- verify before
  relying on it.
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
