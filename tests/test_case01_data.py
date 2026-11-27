"""Data checks for Case 001 (issue #8).

These tests load cases/case01/schema.sql and data.sql into an empty
in-memory SQLite database using only the standard library, so they do
not depend on the case loader (#3) or the SQL engine (#4).
"""

import sqlite3
from pathlib import Path

import pytest

CASE_DIR = Path(__file__).resolve().parent.parent / "cases" / "case01"

# Number of fictional students agreed in issue #2.
EXPECTED_STUDENT_COUNT = 27

EVIDENCE_TABLES = ["room_access_log", "club_membership", "cafe_purchases"]


@pytest.fixture
def db():
    conn = sqlite3.connect(":memory:")
    conn.executescript((CASE_DIR / "schema.sql").read_text(encoding="utf-8"))
    conn.executescript((CASE_DIR / "data.sql").read_text(encoding="utf-8"))
    yield conn
    conn.close()


def test_case01_has_expected_number_of_students(db):
    (count,) = db.execute("SELECT COUNT(*) FROM students").fetchone()
    assert count == EXPECTED_STUDENT_COUNT, (
        f"expected {EXPECTED_STUDENT_COUNT} students, found {count}"
    )


@pytest.mark.parametrize("table", EVIDENCE_TABLES)
def test_every_student_id_refers_to_existing_student(db, table):
    (row_count,) = db.execute(f"SELECT COUNT(*) FROM {table}").fetchone()
    assert row_count > 0, f"{table} is empty, so this check would always pass"

    orphans = db.execute(
        f"""
        SELECT t.student_id
        FROM {table} t
        LEFT JOIN students s ON t.student_id = s.student_id
        WHERE s.student_id IS NULL
        """
    ).fetchall()
    assert orphans == [], (
        f"{table} refers to student_id values that are not in students: "
        f"{sorted(row[0] for row in orphans)}"
    )


def test_solution_returns_exactly_one_row(db):
    solution = (CASE_DIR / "solution.sql").read_text(encoding="utf-8")
    rows = db.execute(solution).fetchall()
    assert len(rows) == 1, (
        f"solution.sql must return exactly one row (the culprit), got {len(rows)}: {rows}"
    )
