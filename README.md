<!-- TODO: Replace every [TBD] item with the team's final decision, then delete this comment. -->

# SQLUE
> Track down the culprit by following the traces left in a database, one SQL query at a time.

**SQLUE** is a desktop detective game in which the player investigates a case by writing SQL queries against a case database, collecting clues, and naming the culprit. It is built with Python and Tkinter and runs locally on your own computer.

---

## Why we built this

Students who learn `SELECT`, `JOIN`, and `GROUP BY` in a database course often struggle to see where they would actually use them. Textbook example tables are dull, and syntax that is only memorized is quickly forgotten.

This game lets players experience SQL not as **syntax to memorize** but as **a tool for solving a case**.

## Intended users

- People who want to learn SQL in a fun way and practice putting it to use

## Features

### Minimum usable version

- **Query editor**: type a SQL query, press Run, and see the result as a table
- **Case data and schema viewer**: query the case database and check which tables and columns it contains
- **Clue file**: read the case overview and witness statements
- **Accusation**: enter the culprit's name and get a correct/incorrect verdict
- **SELECT only**: only `SELECT` queries can be run; queries that modify data (such as `INSERT` or `DROP`) are blocked

### Planned after the minimum usable version

- SQL guide (a cheat sheet for `SELECT`, `WHERE`, `JOIN`, and more)
- Step-by-step hints
- Notepad for writing down clues
- Exit to the title / case selection screen

## Case preview — Case #01

> Room 302 in Frontier Hall is a lab room that can only be entered by tapping a student ID card. While the professor stepped out for a moment, someone spilled a drink over the professor's laptop and ran off. The drink left on the keyboard is an unusual one. Investigate the café orders, the room's access records, and the witness statements to find out who did it.

| Table | Columns | Contents |
|---|---|---|
| `students` | `student_id`, `name` | All suspects |
| `room_access_log` | `student_id`, `access_time` | Room 302 entry records |
| `club_membership` | `student_id`, `club` | Each student's club |
| `cafe_purchases` | `student_id`, `item` | Café purchase records |

## Setup and run

### Requirements

- Python 3.13 or later (tested on 3.13 and 3.15)
- Tkinter: included in the official Python installers for Windows and macOS. On Linux it may need to be installed separately (for example, on Ubuntu: `sudo apt install python3-tk`).
- No other packages are needed to play. Developers also need pytest, listed in `requirements-dev.txt`.

### Run the game

```bash
# 1. Clone the repository
git clone https://github.com/kdy00/SQLUE.git
cd SQLUE

# 2. Start the game
python -m sqlue
```

### Run the tests (for developers)

```bash
python -m pip install -r requirements-dev.txt
python -m pytest
```

The tests cover the case data and the game logic: loading cases, running queries (including blocking queries that modify data), and checking answers. The Tkinter screens are not covered by automated tests. Tests run automatically on every pull request through GitHub Actions, and a pull request cannot be merged until they pass. See [CONTRIBUTING.md](CONTRIBUTING.md#running-checks) for details.

## Example usage

1. Start the game. The case introduction appears.
2. Read the clue file to learn what happened and what the witnesses saw.
3. Open the schema viewer to see which tables and columns are available.
4. Type a query into the query editor and press Run to examine the evidence.
5. Use what you find to narrow down the suspects with further queries.
6. When you have identified the culprit, enter their name in the accusation box and submit.

<!-- TODO: Add a first example query and a screenshot once the data and screen are finished. -->

## Current limitations

- Only one case is currently playable.
- Progress is not saved; closing the program means starting over.
- The SQL guide, hints, notepad, and exit screen have not been developed yet.
- The Tkinter screens have no automated tests; they are checked manually using the procedure in [docs/manual-checks.md](docs/manual-checks.md).

## Project structure

```
SQLUE/
├── README.md
├── LICENSE
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md                  # How to report issues, branch, open PRs, and review
├── .gitignore
├── requirements-dev.txt             # Development dependencies (pytest)
│
├── .github/
│   ├── PULL_REQUEST_TEMPLATE.md
│   ├── ISSUE_TEMPLATE/
│   └── workflows/
│       └── ci.yml                   # Runs the tests on Python 3.13 and 3.15 (Tkinter screens excluded)
│
├── docs/
│   ├── design.md                    # Architecture, module interfaces, decision log
│   └── manual-checks.md             # Manual check procedure for the screens
│
├── cases/                           # Case data, kept separate from the code
│   └── case01/
│       ├── schema.sql               # Table definitions
│       ├── data.sql                 # Evidence data
│       ├── solution.sql             # Reference solution, used by the data test
│       └── case.json                # Introduction, hints, answer information
│
├── sqlue/                           # Game package (no src/ layout)
│   ├── __init__.py
│   ├── __main__.py                  # Entry point for python -m sqlue
│   ├── case_loader.py               # Reads cases from cases/ (no UI code)
│   ├── database.py                  # Creates the database and runs queries (no UI code)
│   ├── game.py                      # Game state and answer checking (no UI code)
│   └── ui/
│       ├── __init__.py
│       └── app.py                   # Tkinter screens and event wiring only
│
└── tests/
    ├── test_case01_data.py          # Case 001 data and solution.sql check
    ├── test_case_loader.py
    ├── test_database.py             # Includes tests for blocking data-modifying queries
    └── test_game.py
```

Game logic (`case_loader.py`, `database.py`, `game.py`) does not depend on the user interface, so it can be tested without opening a window.

## How we work

1. Create an **issue** for each unit of work, describing its goal, scope, assignee, and acceptance criteria.
2. The assignee works on a **branch** and verifies the change locally.
3. The assignee opens a **pull request** linked to the issue and describes how the change was verified.
4. **Another team member reviews** the pull request; requested changes are addressed before merging.
5. Progress is tracked on our [GitHub Projects board](https://github.com/users/kdy00/projects/2) (Backlog → Ready → In progress → In review → Done).

The `main` branch is protected and cannot be merged into without an approved review.

## Use of AI tools

- Every AI-assisted contribution has a responsible team member and goes through human review.
- Pull requests involving AI describe the tool used, what it helped with, what humans checked, and what was accepted, changed, or rejected, in the "AI use disclosure" section of the PR template.

## Contributing

Bug reports and suggestions are welcome.

- Please read [CONTRIBUTING.md](CONTRIBUTING.md) before contributing.
- Open issues in [Issues](https://github.com/kdy00/SQLUE/issues) using the issue template.
- All participants are expected to follow our [Code of Conduct](CODE_OF_CONDUCT.md).

## Team

Industrial Engineering (ITM), Seoul National University of Science and Technology · Open Source Software team project


| Name | Main responsibilities | GitHub |
|---|---|---|
| Kim Dong yeon | Repository setup (#1), SQL execution engine (#4), CI workflow (#8) | [@kdy00](https://github.com/kdy00) |
| Kim Yun | Case data (#2), answer checking (#5), clue and table screens (#7) | [@yuoonnu](https://github.com/yuoonnu) |
| Jeong Yeon ji | Case loader (#3), main screen (#6) | [@jyg061201-cyber](https://github.com/jyg061201-cyber) |

## License

This project is released under the [MIT License](LICENSE).

<!-- TODO: Confirm that this reason matches the team's reason for choosing MIT. -->

**Why MIT:** We want students learning SQL to be able to use the game freely and adapt it for course materials or other learning tools. MIT is a short, permissive license that allows use, modification, and redistribution as long as the copyright notice is kept, which fits this goal.
