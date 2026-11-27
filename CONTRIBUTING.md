<!-- TODO: Replace every [TBD] item with the team's decision, then delete this comment. -->

# Contributing to SQLUE

Thank you for your interest in contributing. This document describes how our team works, so that every change goes through the same process: **issue → branch → pull request → peer review → merge**.

All contributors are expected to follow our [Code of Conduct](CODE_OF_CONDUCT.md). It also explains how to raise a concern.

## Reporting issues and proposing work

Every unit of work, whether it is a feature, a bug fix, a test, documentation, or an investigation, starts as an issue.

1. Open a new issue and choose the **Task** template.
2. Fill in every section of the template:
   - **Goal**: what will exist or work when the task is done
   - **Background**: context a teammate needs, such as design decisions and related issues (delete it if the goal is self-explanatory)
   - **Scope**: what is in scope and what is out of scope, with the issue number that covers anything left out
   - **Responsible student**: the student who owns the issue, and a reviewer who is not that student
   - **Acceptance criteria**: observable conditions that show the task is complete
   - **Dependencies**: issues that must be finished first, or "None"
   - **Notes for review**: what the reviewer should check, and how
3. Assign the responsible student in the issue's **Assignees** sidebar as well, not only in the issue text.
4. Keep each issue small enough for one person to finish and for another person to review.

If you find a problem while working on another issue, open a new issue for it instead of fixing it silently in an unrelated pull request.

Small documentation changes, such as fixing typos or reflecting a decision the team has already made (for example, the project name), may be made with a pull request without opening an issue first. The pull request must still explain what changed and why, and it still needs a review before merging.

## Project board

We track all issues on our [GitHub Projects board](https://github.com/users/kdy00/projects/2). Each issue moves through these columns:

| Column | Meaning |
|---|---|
| **Backlog** | The issue exists but is not ready to start yet. |
| **Ready** | The issue has an assignee and clear acceptance criteria, and its dependencies are finished or agreed. |
| **In progress** | The assignee is working on it on a branch. |
| **In review** | A pull request is open and waiting for review. |
| **Done** | The pull request has been reviewed and merged. |

Move your issue to the next column when its state changes, so the board always shows the current status. Record important scope changes and decisions as comments on the issue when they happen.

## Setting up the project

You need **Python 3.13 or later**. The team develops with Python 3.13, and CI tests both 3.13 and 3.15.

1. Clone the repository and move into it:

   ```bash
   git clone https://github.com/kdy00/SQLUE.git
   cd SQLUE
   ```

2. Create and activate a virtual environment, so that development tools stay separate from your other Python projects:

   ```bash
   python -m venv .venv
   ```

   - Windows: `.venv\Scripts\activate`
   - macOS / Linux: `source .venv/bin/activate`

3. Install the development dependencies (pytest):

   ```bash
   python -m pip install -r requirements-dev.txt
   ```

The game itself uses only the Python standard library, so no other packages are needed.

## Making a change

1. Make sure the issue is in **Ready** and assigned to you, then move it to **In progress**.
2. Update your local `main` branch:

   ```bash
   git checkout main
   git pull
   ```

3. Create a branch for the issue. Name it `<issue number>-<short-description>` in lowercase, with words separated by hyphens (for example, `4-sql-engine` or `5-answer-checking`).

   The easiest way is the **Development → Create a branch** button in the issue's sidebar, which creates a branch in this format and links it to the issue. Then fetch it locally:

   ```bash
   git fetch origin
   git checkout <branch name>
   ```

   Or create it from the command line:

   ```bash
   git checkout -b <branch name>
   ```

4. Make your change. Keep it within the scope of the issue.
5. Run the checks locally (see [Running checks](#running-checks)) and check each acceptance criterion of the issue yourself.
6. Commit and push your branch:

   ```bash
   git add <files>
   git commit -m "<message>"
   git push -u origin <branch name>
   ```

   Commit messages are written in English as one short line that starts with a verb in the imperative form and says what the commit does, for example:

   - `Add error message for missing case file`
   - `Fix name comparison in answer checking`
   - `Update README with run instructions`

## Running checks

Run all tests from the repository root:

```bash
python -m pytest
```

Add `-v` to see the result of each test. Use `python -m pytest` rather than `pytest`, so that the `sqlue` package in the repository root can be imported by the tests.

The automated tests cover the case data and the game logic. They must not import the UI package (`sqlue/ui/`), because the CI machine has no display. Tkinter screens are checked manually; see `docs/manual-checks.md` (TBD).

### Continuous integration

The workflow in `.github/workflows/ci.yml` runs the same command on **Python 3.13 and 3.15** on every pull request into `main` and on every push to `main`. The results appear as two checks on the pull request: `test (3.13)` and `test (3.15)`.

Both checks are **required**: a pull request cannot be merged until they pass. If a check fails, open it from the pull request and read the log to see which test failed and why.

If the Python versions in `ci.yml` are changed, the check names change too, so the required checks in the `main` branch protection settings must be updated at the same time.

## Opening a pull request

1. Open a pull request from your branch into `main`. The pull request template appears automatically.
2. Fill in every section of the template:
   - **Related issue**: write `Closes #<number>` so the issue closes when the pull request is merged. If the pull request only covers part of the issue, write `Part of #<number>` instead.
   - **Summary of changes**: what changed and why. Explain anything that goes beyond the issue's scope.
   - **Verification**: what you ran and checked yourself, and the results. For UI changes, attach a screenshot or GIF.
   - **AI use disclosure**: see [Use of AI tools](#use-of-ai-tools).
3. Request a review from the reviewer named in the issue.
4. Move the issue to **In review**.

Keep pull requests small enough that another student can read and understand the whole change.

## Reviewing a pull request

The reviewer is responsible for checking the actual change, not only for approving it.

- Read the actual code and tests in the **Files changed** tab. Do not approve based only on an AI review result.
- Check that the change meets the issue's acceptance criteria and that the expected results in the tests match the requirements.
- Run the change locally when it affects behavior.
- Leave comments on specific lines when something should be changed or explained.
- Finish the review with **Request changes** if something must be fixed, or **Approve** when the change is ready.
- Use the reviewer checklist at the bottom of the pull request template.

Discuss the reviewer's concerns in the pull request and resolve them before merging. A pull request cannot be merged while a review conversation is unresolved.

## Merging

The `main` branch is protected: a pull request needs an approving review and passing CI checks before it can be merged.

- The **author of the pull request** merges it, after the reviewer's concerns have been resolved, the reviewer has approved, and the required checks (`test (3.13)` and `test (3.15)`) have passed.
- After merging, check that the issue is closed and moved to **Done** on the board.

## Use of AI tools

AI tools may be used to help implement a bounded task, debug, write tests, improve documentation, or review a pull request. The student responsible for the issue remains responsible for the result.

- Every AI-assisted contribution has a responsible student and goes through human review.
- In the pull request, fill in the **AI use disclosure**: the tool used, what it helped with, what humans checked, and what was accepted, changed, or rejected.
- If AI helped with a review, say so in the review comment.
- Do not hand an entire feature to an AI tool and upload the result without understanding and checking it.

## Questions

If something in this document is unclear or does not match how we actually work, open an issue so we can fix it.
