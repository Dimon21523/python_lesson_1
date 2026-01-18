import os
import sys
import uuid

from sqlalchemy import select

CURRENT_DIR = os.path.dirname(__file__)
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

from models import Student  # noqa: E402


def test_add_student(db_session):
    email = f"{uuid.uuid4()}@example.com"
    student = Student(name="Ivan", email=email)

    db_session.add(student)
    db_session.commit()

    found = db_session.execute(
        select(Student).where(Student.email == email)
    ).scalar_one()

    assert found.name == "Ivan"
    assert found.is_deleted is False


def test_update_student(db_session):
    email = f"{uuid.uuid4()}@example.com"
    student = Student(name="Petr", email=email)

    db_session.add(student)
    db_session.commit()

    student.name = "Peter"
    db_session.commit()

    found = db_session.execute(
        select(Student).where(Student.email == email)
    ).scalar_one()

    assert found.name == "Peter"


def test_soft_delete_student(db_session):
    email = f"{uuid.uuid4()}@example.com"
    student = Student(name="Anna", email=email)

    db_session.add(student)
    db_session.commit()

    student.is_deleted = True
    db_session.commit()

    found = db_session.execute(
        select(Student).where(Student.email == email)
    ).scalar_one()

    assert found.is_deleted is True
