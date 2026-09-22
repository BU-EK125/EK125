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
8. **Add cross-reference links** between the reading and its GPP (see below).
9. **Audit for "common mistake" callout opportunities** (see below).
10. **Build and verify** (see "Verifying a build," below) before opening a PR.
11. **Do not auto-merge.** Open the PR, report the preview link, and wait for
    an explicit go-ahead to merge.

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
- Placement should be tied to a real, specific correspondence -- a GPP
  problem that uses the exact concept/example from that reading section --
  not generic "see the reading" boilerplate scattered everywhere. It's fine
  to skip optional/challenge problems that don't have a clean 1:1 match.
- Cross-references aren't only reading↔GPP within a class -- link backward to
  a prerequisite class's reading when a later class's material directly
  builds on a specific earlier section (e.g. Class 6's reading links back to
  Class 5's accumulator-pattern section).

## "Common mistake" callouts

When auditing a reading for places to flag common student mistakes, use this
exact format:

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
  exclusive-vs-inclusive boundary.
- Place it immediately after the explanation/example it relates to, in the
  same cell if possible.
- Aim for the density already set in Classes 5-7 (roughly five to eight
  well-justified callouts per class) -- more than that starts to feel like
  noise rather than a flag.

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

The baseline warning count for this book is **2** (pre-existing lexing
warnings in `class/Class10.md` and `class/Class12.md`, unrelated to notebook
content -- caused by literal code blocks containing characters like `` ` ``
or `!` that trip up the Python lexer in strict mode; harmless, and not
something to "fix" as part of an unrelated change). If your build shows more
than 2 warnings, or fails outright, investigate before opening the PR --
don't assume a new warning is pre-existing without checking.

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
