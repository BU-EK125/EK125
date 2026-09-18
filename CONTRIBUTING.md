# How to make changes to this site (a guide for instructors)

This guide walks through the whole process of editing a reading or GPP and getting your change published, assuming you've never used git or GitHub before. Follow the steps in order the first few times -- once it clicks, it takes about a minute of actual work per change.

**Before you start:** see the [README](README.md) for what belongs in this repo (readings, lecture notes, GPPs, GPP solutions -- no quizzes, exams, homework, or IPPs).

## One-time setup

You only need to do this once, ever, on a given computer.

1. **Install git.**
   - Mac: open Terminal and type `git --version`. If it's not installed, it'll prompt you to install it -- follow the prompt.
   - Windows: download and install [Git for Windows](https://git-scm.com/download/win). This also gives you "Git Bash," a terminal you'll use for the commands below.
2. **Get a GitHub account** if you don't have one already, at [github.com](https://github.com).
3. **Ask to be added as a collaborator** on `BU-EK125/EK125` (whoever manages the repo can add your GitHub username under the repo's Settings → Collaborators). Without this, you won't be able to push changes.
4. **Download ("clone") the repo to your computer.** Open Terminal (or Git Bash on Windows), navigate to wherever you'd like the folder to live (e.g., `cd Documents`), then run:
   ```
   git clone https://github.com/BU-EK125/EK125.git
   ```
   This creates a folder called `EK125` with a full copy of the repo. You only do this once -- from now on you'll just update this same folder.

## Every time you want to make a change

Think of this as a 5-step recipe: **update → branch → edit → commit/push → open a pull request.**

### 1. Make sure you're starting from the latest version

Open a terminal, move into the repo folder, and pull the latest changes:
```
cd EK125
git checkout main
git pull
```

### 2. Create a new branch for your change

A "branch" is just an isolated workspace for one change, so your edits don't collide with anyone else's. Name it something short and descriptive:
```
git checkout -b fix-class7-typo
```
(Replace `fix-class7-typo` with whatever describes your change.)

### 3. Make your edit

Open the file in whatever editor you like (VS Code, Notepad, even TextEdit) and make your change. Readings live in `class/ClassN.md`, GPPs live in `gpps/`. If you're adding a brand-new page rather than editing an existing one, see the "Adding a new page" section in the [README](README.md) -- you'll also need to add one line to `_toc.yml`.

If you're editing a notebook (`.ipynb`), just write real, working code in the code cells -- there's no separate "run it and save the outputs" step. The site executes every notebook itself, fresh, every time it builds, so whatever your code actually produces is exactly what gets published. All that matters is that it runs without erroring -- if it doesn't, step 6 below will catch it before your change can merge.

**Want a cell to intentionally raise an error** -- e.g. to show students what a bug or a real error message looks like? Tag that cell `raises-exception`, otherwise the build treats the error as broken code and fails. In Jupyter/JupyterLab: View → Cell Toolbar → Tags, then type `raises-exception` in the tag box that appears at the top of the cell. Class 1's `del x; print(x)` cell does exactly this, if you want a working example to copy.

**Want students to be able to click the 🚀 rocket icon and open your page in Colab?** That icon only shows up on `.ipynb` (Jupyter notebook) pages -- never on plain `.md` pages. So:
- Write it as a notebook (`ClassN.ipynb` or `gpps/ClassN_GPP.ipynb`), not markdown. Look at Class 1 or Class 5's reading as a template -- explanations go in markdown cells, real runnable code goes in code cells.
- The rocket button only works once your file is merged into `main` at its final path -- it links directly to that file on GitHub, so it 404s for anyone who clicks it while your change is still sitting in an unmerged PR.
- Everything else (the launch button itself, linking to Colab) is already configured for the whole site -- you don't need to touch any settings, just get the `.ipynb` merged in the right place.

Save the file when you're done.

### 4. Save your change to git ("commit") and upload it ("push")

Back in the terminal:
```
git add .
git commit -m "Fix typo in Class 7"
git push -u origin fix-class7-typo
```
- `git add .` stages every change you made.
- `git commit -m "..."` saves a snapshot with a short description -- replace the text in quotes with a plain-English summary of what you changed.
- `git push ...` uploads your branch to GitHub. The `-u origin fix-class7-typo` part is only needed the very first time you push this branch; after that, plain `git push` works.

### 5. Open a pull request ("PR")

A pull request is a request to merge your branch into the live site. After you push, GitHub will print a URL in the terminal like:
```
remote: Create a pull request for 'fix-class7-typo' on GitHub by visiting:
remote:      https://github.com/BU-EK125/EK125/pull/new/fix-class7-typo
```
Open that link in your browser (or go to the repo on github.com -- it'll show a yellow banner offering to create the PR for your recently-pushed branch). Give it a title, optionally a description, and click **Create pull request**.

### 6. Wait for the automatic check, then merge

Every PR automatically runs a check called `pr-check` that rebuilds the whole site -- since that build executes every notebook, this is also where a broken notebook gets caught. You'll see a status at the bottom of the PR page:
- 🟡 Yellow = still running, wait a few minutes.
- ✅ Green = passed. Click **Merge pull request**.
- ❌ Red = something's broken. Click "Details" next to the check to see what failed, fix it (edit the file, then repeat step 4 to push another commit to the same branch -- no need to open a new PR), and it'll re-run automatically.

Once merged, the live site rebuilds and republishes automatically within a few minutes -- no further action needed.

## Cheat sheet

Once you're comfortable, this is the whole thing:
```
git checkout main
git pull
git checkout -b my-branch-name
# ...edit files...
git add .
git commit -m "Describe the change"
git push -u origin my-branch-name
# ...open the PR link GitHub gives you, wait for the green check, click Merge...
```

## Common hiccups

- **"Permission denied" / "403" when pushing:** you're probably not yet added as a collaborator on the repo (see step 3 of setup), or you're not signed into git with the right GitHub account. Try `git config --global user.email` to check which email git thinks you are.
- **"Your branch is behind" or a merge conflict:** someone else's change landed on `main` before yours. Run `git checkout main && git pull`, then from your branch run `git merge main` and resolve any conflicts it flags (or just ask for help -- conflicts are the one part of git that's genuinely easier with a second pair of eyes).
- **You edited a notebook (`.ipynb`) and the check failed:** the site executes the whole notebook when it builds, so this almost always means a cell errors out. Open the "Details" link on the failed check to see which cell and why, fix the code, and push again.
- **Not sure if your change is safe to make directly, or you'd like someone to look before it goes live:** that's exactly what the pull request is for -- it doesn't touch the live site until someone clicks "Merge." Feel free to open it and ask a question in the PR description rather than merging right away.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
