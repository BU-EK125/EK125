# Conventions for maintaining this book

This file documents the recurring patterns used across this repo, so they can be
followed consistently without having to reconstruct them from PR history each
time. It's aimed at whoever (human or AI assistant) is doing the next piece of
maintenance -- porting a class, adding cross-references, or auditing content.

If you're just editing text in an existing page, you probably don't need this.
See [CONTRIBUTING.md](CONTRIBUTING.md) for the basic "how to open a PR" guide
instead. This file is for the more structural, repeatable jobs below.

## Porting a class from `.md` to `.ipynb`

Some readings and GPPs live in [EK125-notebooks](https://github.com/BU-EK125/EK125-notebooks)
as executable notebooks before they're "graduated" into this repo. The
end-to-end workflow for bringing one over:

1. **Diff-audit first.** Compare the EK125-notebooks version against this
   repo's current `.md` version, cell by cell / section by section. Confirm
   any differences are either cosmetic (heading numbering, title wording) or
   genuine improvements (corrected references, fixed typos) -- not lost
   content. Watch out for false-positive diffs from naive text normalization
   (e.g. stripping `**` for markdown-bold comparison also strips Python's
   `**` exponentiation operator inside code -- verify any suspicious diff
   against the raw source before trusting it).
2. **Test-execute** both the reading and its GPP notebook in EK125-notebooks
   to confirm they run clean (exit 0) before porting.
3. **Check `skip-execution` cells** in the GPP for baked-in output. Scaffold
   cells like `squares =` (an intentionally incomplete "your code here" line)
   need no output. Cells with real `input()` prompts and no baked transcript
   need one synthesized and baked in (see "Baking notebook output," below).
4. **Copy the files** into this repo at `class/ClassN.ipynb` and
   `gpps/ClassN_GPP.ipynb`.
5. **Archive, never delete, the old `.md`:** `git mv class/ClassN.md
   archive/ClassN.md`. This repo's rule is that nothing gets deleted outright
   -- superseded content moves to `archive/`, which is excluded from the
   build via `exclude_patterns` in `_config.yml`.
6. **Update `_toc.yml`** -- nest the GPP under its reading with a `sections:`
   entry (see the existing Class 5/6/7 entries for the pattern).
7. **Update `README.md` and `intro.md`** -- both have a running list of which
   classes are notebooks (e.g. "Classes 1, 5, 6, and 7"); keep it current.
8. **Add cross-reference links** between the reading and its GPP, in **both**
   directions (see below).
9. **Audit for "common mistake" callout opportunities in both the reading
   and its GPP** (see below).
10. **Build and verify** (see "Verifying a build," below) before opening a PR.
11. **Do not auto-merge.** Open the PR, report the preview link, and wait for
    an explicit go-ahead to merge.

Steps 8 and 9 aren't one-time steps that only apply while porting a class for
the first time -- **treat them as a standing checklist for any audit or
maintenance pass on an already-published class too.** If you're touching a
reading or GPP for any reason (fixing a bug, adding content, responding to a
reported student mistake), check both of these before opening the PR, even
if they weren't why you started the change:
- Does the reading link to the GPP problem(s) that practice what it just
  covered? Does the GPP link back to the reading section(s) it's drawing on?
  A one-way link (only reading→GPP, or only GPP→reading) is an audit gap.
- Does either the reading or the GPP now warrant a new 🚩 callout for a
  mistake that just came up (e.g. a student-reported error), and if the
  reading already flags something similar, does the GPP problem that
  practices it cross-reference that callout specifically (not just the
  section in general)?

## Porting a homework assignment

As of Fall 2026, homework problem statements (not solutions) are allowed on
this site, for assignments graded for submission only, not correctness --
see README.md for why. Source material lives in the instructor's own
working folder (not `EK125-notebooks`), organized by week, e.g.
`EK125WIP/<term>/Class Materials/Week N/Homework N`. Porting one:

1. **Read the whole source file first.** A week's homework is usually one
   notebook spanning two classes (e.g. "Homework 4" covers Classes 5 and
   6), already split into named parts (e.g. "Part A: Class 5 Problems" /
   "Part B: Class 6 Problems") -- confirm that split before assuming it.
2. **Verify any embedded example code, not just the blank scaffold
   cells.** Homework often includes short "here's some code, what happens"
   snippets as part of the problem statement itself (a bug to find, a
   security lesson, a puzzle to solve) -- actually run each one and confirm
   it produces the claimed behavior before publishing it. Don't assume a
   snippet is correct just because it's already written.
3. **Port as a single `homework/HWN.ipynb`, not split per class.** Unlike
   a GPP, homework doesn't belong to one class -- give it a single page
   with the source's own Part A/Part B (or similar) structure preserved as
   section headings, and register it in `_toc.yml` as its own top-level
   chapter entry, positioned after the last class it covers (not nested
   under either class's `sections:`).
4. **Preserve "discovery" framing.** Some problems are deliberately
   designed for the student to find an undiscussed function themselves
   (e.g. "`os.chdir()` wasn't shown in lecture -- discover it using
   `help()`!") -- keep that framing as-is rather than adding a hint that
   defeats the exercise.
5. **Only code cells that were already filled in the source stay filled**
   (e.g. a single worked first sub-part shown as a model for the rest);
   leave every other code cell as a blank `# Your code here` scaffold,
   matching GPP convention. Never port the assignment's solutions file.
6. **Cross-reference links and common-mistake callouts** follow the exact
   same rules as GPPs (see above) -- tie them to a genuine, specific
   correspondence with the reading, don't force one where none exists. Sweep
   every sub-problem individually rather than stopping once a few obvious
   ones are covered -- a first pass on Homework 4 caught the easy matches
   (the module intro problems) but missed six more real ones buried in
   later, less obviously-related sub-parts (nested while loops, exhaustive
   search bounds, per-item validation) that only turned up on a second,
   more careful pass.
7. **Build and verify**, same as any other port (see "Verifying a build,"
   below), then open a PR and wait for an explicit go-ahead to merge.

## Cross-reference links

### Why absolute URLs, not relative links

This book's `_config.yml` sets `heading_anchors: 0`, which means headings are
**not** registered as MyST cross-reference targets. A plain relative link like
`[text](../class/Class5.html#anchor)` silently breaks -- it renders with a
mangled, non-functional `href` (you'll see `myst.xref_missing` warnings in the
build log if you try). The fix that actually works: use the full published
absolute URL, e.g.:

```
https://BU-EK125.github.io/EK125/class/Class5.html#looping-with-indices
```

MyST treats this as an ordinary external link and passes it through
untouched. Always use this `https://BU-EK125.github.io/EK125/...` form for
any link between pages in this book.

### Finding the real anchor slug

Don't guess an anchor from the heading text (`## Looping with Indices` is
*not* guaranteed to become `#looping-with-indices` -- Sphinx can append
disambiguating suffixes like `#id1` when heading text repeats elsewhere on
the page). Instead, build the book locally and check the real, rendered
anchor:

```bash
jb build .
grep -oE '<section id="[^"]*"' _build/html/class/ClassN.html
```

Match the `id` to the right heading by its position in the list, then use
that exact string as the `#anchor` in your link.

### Where to put the links, and what they should say

- Cross-reference links live **inside the relevant existing markdown cell**,
  appended as a short closing sentence -- not as a new standalone "See also"
  cell (with rare exceptions, e.g. inserting a one-line pointer cell when a
  section's last cell is a code cell with no trailing markdown to append to).
- From the reading, pointing at the GPP: *"You'll practice this exact pattern
  in today's GPP -- see [Problem N: Title](url#anchor)."*
- From the GPP, pointing at the reading: *"See the reading's [Section
  Title](url#anchor) section for ..."*
- A homework page follows the same rule as a GPP, pointing at whichever
  reading section(s) each problem draws on -- the same "See the reading's
  [Section Title](url#anchor) section for ..." phrasing, once per problem
  where a real match exists. Unlike a GPP, homework isn't itself a common
  target for reading→homework links (readings are ported once, well before
  a given week's homework exists) -- the direction that matters is
  homework→reading.
- Placement should be tied to a real, specific correspondence -- a GPP or
  homework problem that uses the exact concept/example from that reading
  section -- not generic "see the reading" boilerplate scattered everywhere.
  It's fine to skip optional/challenge problems that don't have a clean 1:1
  match.
- Cross-references aren't only reading↔GPP within a class -- link backward to
  a prerequisite class's reading when a later class's material directly
  builds on a specific earlier section (e.g. Class 6's reading links back to
  Class 5's accumulator-pattern section).

## "Common mistake" callouts

When auditing a reading, its GPP, **or a homework page** for places to flag
common student mistakes, use this exact format:

```
🚩 **Common mistake:** <description of the mistake and why it happens, plus
how to recognize or avoid it>.
```

- The 🚩 emoji is the flag used specifically for this callout type (other
  emoji, like ⚠️ or 👉, may already exist in some notebooks for other kinds
  of notes -- leave those as-is; don't retrofit them to 🚩 unless asked).
- Only add a callout where there's a **real, specific, common** error tied to
  the material right there -- not generic advice. Good candidates: syntax
  that silently does the wrong thing instead of erroring (e.g. `range()`
  producing an empty sequence), a beginner conflating two similar-looking
  operations (e.g. `grid[2, 0]` vs `grid[2][0]`), or a subtle off-by-one /
  exclusive-vs-inclusive boundary. A real student-reported error is the
  strongest possible source for one -- don't wait for an audit to add it.
- Place it immediately after the explanation/example it relates to, in the
  same cell if possible. In a GPP, that's usually right in the problem
  statement it's relevant to (see Class 5's GPP, Problem 2.5, for an
  example) -- GPPs don't have to confine callouts to one dedicated section,
  though a short dedicated "Common Mistakes" section (e.g. at the end,
  summarizing a few mistakes tied to specific problems above) is also fine
  where a GPP's problems don't have a natural per-problem spot for one.
- Aim for the density already set in Classes 5-7 (roughly five to eight
  well-justified callouts per class) -- more than that starts to feel like
  noise rather than a flag. This density guideline is per reading; a GPP
  usually warrants fewer, since not every problem has a genuine, common,
  specific failure mode worth flagging.
- **Cross-reference it from the other document.** A callout in the reading
  about a mistake that a specific GPP problem is likely to trigger should be
  linked from that problem (see "Cross-reference links" above) -- and vice
  versa, a callout added to a GPP problem in response to something that came
  up in class is worth a pointer from the reading section it relates to, if
  one exists.

## Notebook cell tags

- **`raises-exception`** -- tag a cell that's *supposed* to error (e.g.
  demonstrating a bug on purpose). Without this tag, `execute_notebooks:
  force` treats any error as a broken build and fails the check.
- **`skip-execution`** -- tag a cell that should be left untouched during a
  forced re-execution. Used for: (a) `input()`-based cells that have a baked
  transcript already committed as output, since a fresh execution can't
  simulate interactive input, and (b) intentionally-incomplete GPP scaffold
  cells (e.g. `squares =` with no right-hand side) that would raise a
  `SyntaxError` if actually run.

## Baking notebook output

For a `skip-execution`-tagged `input()` cell with no existing output, write a
realistic sample transcript and bake it into the cell's `outputs` field
directly (matching the `stream`/`stdout` output format nbformat expects)
rather than leaving it blank -- readers should see what a real run looks
like even though the cell itself won't be re-executed at build time.

## Verifying a build

Before opening a PR:

```bash
jb build .
```

The baseline warning count for this book is **1** (a pre-existing lexing
warning in `class/Class12.md`, unrelated to notebook content -- caused by a
literal code block containing a `!` that trips up the Python lexer in strict
mode; harmless, and not something to "fix" as part of an unrelated change).
`class/Class10.md`'s matching warning was a real bug, not lexer noise -- a
copy-pasted-twice section in the source content, fixed when that class was
ported to `.ipynb` (see git history for `class/Class10.ipynb`). If your
build shows more than 1 warning, or fails outright, investigate before
opening the PR -- don't assume a new warning is pre-existing without
checking.

To spot-check that new cross-reference links actually resolve to the right
anchor (not just that the build didn't warn), grep the built HTML directly:

```bash
grep -oE 'href="https://BU-EK125\.github\.io/EK125/[^"]*"' _build/html/class/ClassN.html
```

## Archiving, never deleting

Anything superseded -- an old `.md` replaced by a `.ipynb`, a doc replaced by
a reformatted version -- gets `git mv`'d into `archive/`, not deleted. This
keeps history recoverable and matches `exclude_patterns` in `_config.yml`,
which already excludes `archive/*` and `archive/**/*` from the build.

## PR-preview deploys

Every PR in this repo (and the other 4 `BU-EK125` repos) automatically builds
and publishes a live preview via `rossjrw/pr-preview-action`, commented
directly on the PR, at `pr-preview/pr-<N>/` on the `gh-pages` branch. The
production deploy step (on merge to `main`) uses
`peaceiris/actions-gh-pages` with `keep_files: true` specifically so it
doesn't wipe out other PRs' active previews when it publishes. Don't switch
that back to a full-replace deploy (e.g. `ghp-import -f`) without accounting
for this.
