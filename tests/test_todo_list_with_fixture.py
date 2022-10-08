# # # # # # # # # # # # # # # #
#                             #
# The boring side of the code #
#                             #
# # # # # # # # # # # # # # # #

from src.todo_list import ToDoList
import pytest


@pytest.fixture
def todo_list():
    return ToDoList()


def test_tasks_should_be_empty(todo_list):
    actual = todo_list.tasks

    assert len(actual) == 0


def test_tasks_should_return_1_task(todo_list):
    todo_list.add_task("go to the doctor")

    actual = todo_list.tasks

    assert len(actual) == 1
    assert "go to the doctor" in actual


def test_tasks_should_return_2_tasks(todo_list):
    todo_list.add_task("go to the doctor")
    todo_list.add_task("go to the pharmacy")

    actual = todo_list.tasks

    assert len(actual) == 2
    assert "go to the doctor" in actual
    assert "go to the pharmacy" in actual
