# Fitness Tracker Analyzer: Team Contract

**EK125 Fitness Tracker Project, Part 1**

Submit as a PDF to Gradescope (group submission) by **Tuesday 10/27, 11:59 PM.**

---

## Section 1: Team and Roles

**Team name / number:** ______________________

| Function | Owner (name) | File |
|---|---|---|
| `load_tracker_data(filename)` | | `loader.py` |
| `analyze_metric(data, metric, goal, higher_is_better=True)` | | `analyzer.py` |
| `write_report(results_list, filename)` | | `reporter.py` |

**Duty rotation:**

| Class | Integrator | Tester | Recorder |
|---|---|---|---|
| 15 (Mon 10/26) | | | |
| 16 (Wed 10/28) | | | |
| 17 (Mon 11/2) | | | |
| 18 (Wed 11/4) | | | |
| 19 (Mon 11/9) | | | |

---

## Section 2: Problem Definition

**What goes in?**

**What comes out?**

**What counts as success?**

**What is messy?**

---

## Section 3: Main Program Plan

Write the Python that `main.py` will run. The functions don't need to exist yet.

```python
from loader import load_tracker_data
from analyzer import analyze_metric
from reporter import write_report

# Your main program here:


```

---

## Section 4: Function Contracts

Each owner writes their own section as a complete docstring. Every section needs **all five parts**: header, parameters, returns (with an example value), side effects, and assumptions/messy cases.

### 4a. `load_tracker_data` (Owner: ______________________)

```python
def load_tracker_data(filename):
    """[One-sentence purpose.]

    Parameters:
        filename (    ): 

    Returns:
        

        Example: 

    Side effects: 

    Assumptions and messy cases: 
    """
```

### 4b. `analyze_metric` (Owner: ______________________)

```python
def analyze_metric(data, metric, goal, higher_is_better=True):
    """[One-sentence purpose.]

    Parameters:
        data (    ): 
        metric (    ): 
        goal (    ): 
        higher_is_better (    ): 

    Returns:
        

        Example: 

    Side effects: 

    Assumptions and messy cases: 
    """
```

### 4c. `write_report` (Owner: ______________________)

```python
def write_report(results_list, filename):
    """[One-sentence purpose.]

    Parameters:
        results_list (    ): 
        filename (    ): 

    Returns:
        

    Side effects: 

    Assumptions and messy cases: 
    """
```

**Example report** (the exact text `write_report` would produce for Days 1–5):

```


```

---

## Section 5: Decision Log

| Date | Decision | Reason | Who agreed |
|---|---|---|---|
| 10/26 | Blank values: | | |
| 10/26 | Metrics and goals: | | |
| 10/26 | Types (`day` and the other columns): | | |
| 10/26 | Results dictionary keys: | | |
| 10/26 | Rounding (who, how many places): | | |
| 10/26 | Ties for "best day": | | |
| 10/26 | Report file name and format: | | |
| | | | |
| | | | |

---

## Section 6: Working Agreement

**How we communicate:**

**How quickly we reply:**

**When we meet outside class (if needed):**

**Shared Google Drive folder (name and link):**

**If someone is stuck, they will:**

**Signatures:** _______________ _______________ _______________

---

## Submission Checklist

Check every box before the Recorder submits.

**Each function contract (Section 4), checked by its owner:**

- [ ] Header copied exactly (names and parameter order unchanged)
- [ ] Every parameter has a type and a description (units where they apply)
- [ ] Return value has a type, an exact structure (every dictionary key named), and a **concrete example value**
- [ ] Side effects stated, even if "none"
- [ ] Assumptions and messy cases stated (including what happens with blank values)

**Team sections, checked by the whole team:**

- [ ] The Loader's *Returns* and the Analyst's `data` parameter describe the **same** dictionary
- [ ] The Analyst's *Returns* keys match **exactly** the keys the Report Writer uses
- [ ] Main program plan (Section 3) calls all three functions with arguments that match the contracts
- [ ] Decision Log has all 7 required decisions filled in
- [ ] Example values are hand-calculated from Days 1–5 of the real data
- [ ] Every question from the lab stress test (Part F) has been answered in the contract
- [ ] Duty rotation and working agreement are filled in
