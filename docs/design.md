# SQLUE design notes

This document records the architecture, module interfaces, and important decisions of SQLUE. Each section links to the issue where the decision was made.

## Continuous integration (#8)

The workflow `.github/workflows/ci.yml` runs `python -m pytest` with GitHub Actions on every pull request into `main` and on every push to `main`.

**What CI checks**

- The Case 001 data (`tests/test_case01_data.py`): the case has 27 students, every `student_id` in `room_access_log`, `club_membership` and `cafe_purchases` refers to an existing student, and `solution.sql` returns exactly one row.
- The game logic tests added in #3 (case loader), #4 (SQL engine) and #5 (answer checking), once they are merged.

**What CI does not check**

- The Tkinter screens. The CI machine has no display, so the tests must not import the UI package (`sqlue/ui/`). The screens are checked by hand using `docs/manual-checks.md`.

**Decisions**

- Python versions: CI tests **3.13**, the lowest supported version and the one the team uses, and **3.15**, the latest release, so that the README's "Python 3.13 or later" is checked at both ends.
- Merging: both checks (`test (3.13)` and `test (3.15)`) are required in the `main` branch protection settings, so a pull request cannot be merged while they fail.
- Dependencies: pytest is the only development dependency and is listed in `requirements-dev.txt`. CI and `CONTRIBUTING.md` use the same install command.
- The workflow only reads the repository (`permissions: contents: read`) and needs no secrets or tokens.
