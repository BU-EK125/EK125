# Class 9 Preread: From Colab Notebooks to Running Python Locally

## Why Make This Shift?

Google Colab notebooks have served us well. They gave everyone a uniform coding environment from day one — no installation headaches, no "it works on my machine" mysteries. You could open a browser, start typing Python, and immediately see results. That was exactly what we needed while you were learning the fundamentals of the language.

But Colab notebooks have a limitation that becomes more important as your programs grow: code lives in **separate cells** that are somewhat disjoint. You write a function in one cell, call it from another, define a variable somewhere else, and the relationships between these pieces depend on the order you happen to run the cells. If you restart the notebook and run cells out of order, things can break in confusing ways. This is fine for experimentation and quick data exploration (which is what notebooks were originally designed for), but it is not how most real programs are written.

In practice, Python programs are written as **single `.py` files** (or collections of `.py` files) that run from top to bottom in one shot. Everything is in one place, the execution order is clear, and the program either works or it doesn't — there's no ambiguity about which cells have been run. This is the standard way that software is written, whether it's a short homework script or a large application.

Starting this week, we are going to transition to writing and running Python on **your own machine** using an application called **PyCharm**. PyCharm is an Integrated Development Environment, or **IDE** — a program specifically designed for writing, running, and debugging code. Think of it as a word processor, but for code instead of essays.

---

## What is an IDE?

An IDE (Integrated Development Environment) bundles several tools into one application:

- **A code editor** — where you write your `.py` files, with helpful features like syntax highlighting (coloring keywords, strings, etc.) and auto-completion of function names and variables.
- **A way to run your code** — you can execute your program with the click of a button or a keyboard shortcut, and see the output in a built-in console.
- **A debugger** — a tool that lets you step through your code line by line to figure out what's going wrong (we'll explore this in a later class).
- **File management** — an easy way to organize your Python files into projects.

There are many IDEs available for Python (VS Code, Spyder, IDLE, etc.), but we will use **PyCharm Community Edition**, which is free and widely used in both education and industry.

---

## What Will Be Different?

Here is a quick comparison of the workflow you're used to vs. the new one:

| | **Colab Notebook** | **PyCharm (local `.py` file)** |
|---|---|---|
| **Where code lives** | In cells in a browser tab | In a `.py` file on your computer |
| **Execution order** | You choose which cells to run and when | The file runs top to bottom, every time |
| **Output** | Appears below each cell | Appears in a console/terminal panel |
| **Saving** | Auto-saved to Google Drive | Saved as a file on your computer |
| **Internet required?** | Yes | No |
| **`input()` function** | Works, but can be clunky in notebooks | Works naturally in the console |

A few things to note:

- **`print()` becomes essential.** In Colab, if the last line of a cell is an expression, the notebook automatically displays its value. In a `.py` file, nothing is displayed unless you explicitly `print()` it. For example, in Colab you could put `x + 5` as the last line of a cell and see the result. In a `.py` file, you need `print(x + 5)`.

- **`input()` works more naturally.** If you've used `input()` in Colab, you may have noticed that the text box can be a little awkward. When running a `.py` file locally, `input()` prompts appear right in the console and the user types their response on the same line — much more like a real program.

- **No more "restart and run all" worries.** Since a `.py` file always runs from the first line to the last, there's no possibility of cells being out of sync.

---

## Installing PyCharm

Now let's get PyCharm installed on your machine. Follow the instructions for your operating system below.

### macOS

1. Open your web browser and go to: **https://www.jetbrains.com/pycharm/download/**

2. The page will show two versions. Make sure you click the download button under **PyCharm Community Edition** (the free, open-source version on the right side of the page). **Do not download PyCharm Professional** — it is a paid product and you do not need it.

3. The site should auto-detect that you're on a Mac. If it gives you a choice between **Apple Silicon** and **Intel**, choose the one that matches your Mac:
   - If your Mac was purchased in **2021 or later**, it almost certainly uses Apple Silicon (M1/M2/M3/M4 chip). Choose **Apple Silicon (.dmg)**.
   - If you're unsure, click the Apple menu () in the top-left corner of your screen, then **About This Mac**. Look for the **Chip** line. If it says "Apple M1" (or M2, M3, M4), choose Apple Silicon. If it says "Intel", choose Intel.

4. Once the `.dmg` file has downloaded, **double-click it** to open it.

5. In the window that appears, **drag the PyCharm CE icon into the Applications folder**.

6. Open **Finder**, navigate to **Applications**, and double-click **PyCharm CE** to launch it.

7. If macOS asks "Are you sure you want to open it?" click **Open**. (This happens because the app was downloaded from the internet.)

8. PyCharm will launch and show a welcome screen. You're in!

### Windows

1. Open your web browser and go to: **https://www.jetbrains.com/pycharm/download/**

2. Scroll down if necessary. Make sure you click the download button under **PyCharm Community Edition** (the free, open-source version on the right side of the page). **Do not download PyCharm Professional.**

3. The site should auto-detect that you're on Windows and offer a `.exe` installer. Click **Download**.

4. Once the `.exe` file has downloaded, **double-click it** to run the installer.

5. The installer will walk you through several screens:
   - **Welcome screen**: Click **Next**.
   - **Choose Install Location**: The default is fine. Click **Next**.
   - **Installation Options**: Check the following boxes:
     - **Create Desktop Shortcut** (makes it easy to launch PyCharm later)
     - **Add "Open Folder as Project"** (handy but optional)
     - **Add launchers dir to the PATH** (recommended)
   - Click **Next**, then **Install**.

6. When the installation finishes, check **Run PyCharm Community Edition** and click **Finish**.

7. PyCharm will launch and show a welcome screen. You're in!

---

## First Launch and Initial Configuration

These steps are the same on both Mac and Windows.

1. On the **Welcome to PyCharm** screen, you may be asked to accept a privacy policy and choose a theme (Light or Dark). Pick whichever you prefer — this is purely cosmetic and can be changed later.

2. If PyCharm asks whether you want to **import settings** from a previous installation, choose **Do not import settings** and click **OK**.

3. You should now see the **Welcome** screen with options like "New Project", "Open", etc.

---

## Disable AI Assistance Features

PyCharm includes AI-powered coding features that we do **not** want you to use in this course. Standard auto-complete (suggesting function names, variable names, and syntax as you type) is perfectly fine and helpful — but AI-generated code suggestions go beyond that and would interfere with your learning. Let's turn those off.

### Disable the AI Assistant Plugin

1. From the **Welcome** screen, click the **Plugins** tab on the left side. (If you already have a project open, go to the menu: **PyCharm > Settings** on Mac, or **File > Settings** on Windows, then select **Plugins** in the left sidebar.)

2. Click the **Installed** tab at the top of the Plugins panel.

3. Look for a plugin called **AI Assistant** (or **JetBrains AI Assistant**).

4. If it is listed and **enabled** (the checkbox is checked), **uncheck the box** or click **Disable** to disable it.

5. If PyCharm asks you to restart the IDE to apply the change, click **Restart IDE**.

6. If you do not see an AI Assistant plugin listed, that's fine — it may not be bundled with the Community Edition by default.

### Disable Inline AI Completions (if present)

Even with the plugin disabled, let's double-check that full-line AI completions are off:

1. Open Settings (**PyCharm > Settings** on Mac, or **File > Settings** on Windows).

2. Navigate to **Editor > General > Inline Completion** (if this section exists).

3. **Uncheck** "Enable inline completion suggestions" or any option mentioning AI-powered completions.

4. Click **Apply**, then **OK**.

### What Should Still Work

After these steps, you will still have:

- **Basic code completion**: When you start typing a function name like `pri`, PyCharm will suggest `print`. This is just looking up known Python names — it is not AI. This is helpful and you should use it!
- **Syntax highlighting**: Keywords, strings, and numbers will be colored differently to make your code easier to read.
- **Error underlining**: If you misspell a variable name or forget a colon, PyCharm will underline the problem in red, similar to a spell-checker in a word processor.

These features help you write correct code without writing code *for* you.

---

## Make Sure Python is Configured

PyCharm needs to know where Python is installed on your computer.

### If You Already Have Python Installed

If you have previously installed Python (e.g., from python.org or Anaconda), PyCharm will usually detect it automatically. You can verify this in the next section when you create a project.

### If You Do Not Have Python Installed

Don't worry — PyCharm can download Python for you during project creation. When you create a new project (next section), PyCharm will offer to set up a Python interpreter. If none is found, it will give you the option to download one. Choose the latest **Python 3.x** version offered (e.g., Python 3.12 or 3.13).

---

## Create Your First Project and Run a Program

### Create a New Project

1. From the Welcome screen, click **New Project**.

2. For the **Location**, choose a folder that makes sense to you. For example:
   - Mac: `/Users/yourname/Documents/EK125`
   - Windows: `C:\Users\yourname\Documents\EK125`

3. Under **Python Interpreter**, make sure a Python version is selected. If PyCharm found your installed Python, it will show something like `Python 3.12`. If not, use the option to download Python.

4. You may see an option for "Create a main.py welcome script." You can **uncheck** this — we'll create our own file.

5. Click **Create**.

6. PyCharm will open your new project. You should see a file browser panel on the left showing your project folder.

### Create and Run hello.py

1. In the Project panel on the left, **right-click** on your project folder name (e.g., `EK125`).

2. Select **New > Python File**.

3. Type `hello` as the file name and press **Enter**. PyCharm will create `hello.py` and open it in the editor.

4. Type the following code in the editor:

```python
print("Hello, world!")
print("I am running Python on my own computer!")
```

5. To run the program, **right-click** anywhere in the editor and select **Run 'hello'**. (Alternatively, you can click the green **Run** button (triangle/play icon) in the top-right area of the window, or use the keyboard shortcut: **Ctrl+Shift+F10** on Windows, **Ctrl+Shift+R** on Mac.)

6. A **Run** panel will appear at the bottom of the screen showing the output:

```
Hello, world!
I am running Python on my own computer!
```

Congratulations — you just ran your first local Python program! We will practice more in class during the Group Practice Problems.

---

## Key Things to Remember

| Task | How to Do It |
|---|---|
| **Create a new file** | Right-click project folder > New > Python File |
| **Run a file** | Right-click in editor > Run, or use the green play button |
| **See output** | Look at the Run panel at the bottom of the screen |
| **Type input** | Click in the Run panel and type when prompted |
| **Save a file** | PyCharm auto-saves! But you can also press Ctrl+S (Cmd+S on Mac) |
| **Open an existing file** | Double-click it in the Project panel on the left |

---

## What to Expect in Class

In class this week, we will:

1. **Troubleshoot any installation issues** — if you ran into problems getting PyCharm installed or configured while working through this preread, we will help you get everything up and running.
2. **Work through coding problems in PyCharm** — we'll practice writing and running `.py` files together so you're comfortable with the new workflow.
3. **Support you on your homework assignments** — this week's homework will be completed in PyCharm rather than Colab, and we'll be available to help you get started on it during class.

---

## Troubleshooting

**"No Python interpreter configured"**: Go to **Settings > Project > Python Interpreter** and either select an existing Python installation or click the gear icon to add/download one.

**"Permission denied" on Mac**: If macOS blocks PyCharm from running, go to **System Settings > Privacy & Security** and click **Open Anyway** next to the PyCharm message.

**The Run panel says "Process finished with exit code 1"**: This means your program encountered an error. Read the red error text in the Run panel — it will tell you the line number and type of error, just like in Colab.

**I can't type input in the Run panel**: Make sure you click inside the Run panel before typing. The cursor needs to be in the console area, not in the editor.

**My code runs but I don't see any output**: Make sure you are using `print()`. Unlike Colab, simply writing an expression on a line (like `x + 5`) will not display anything.
