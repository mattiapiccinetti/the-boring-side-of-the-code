# # # # # # # # # # # # # # # #
#                             #
# The boring side of the code #
#                             #
# # # # # # # # # # # # # # # #

from src.todo_list import ToDoList


def test_add_task_should_return_zero():
    todo_list = ToDoList()

    actual = todo_list.add_task("go to the doctor")

    assert actual == 0


def test_tasks_should_be_empty():
    todo_list = ToDoList()

    actual = todo_list.tasks

    assert len(actual) == 0


def test_tasks_should_return_2_tasks():
    todo_list = ToDoList()
    todo_list.add_task("go to the doctor")
    todo_list.add_task("buy some beers")

    actual = todo_list.tasks

    assert len(actual) == 2
    assert "go to the doctor" in actual
    assert "buy some beers" in actual


def test_get_by_name_should_return_the_inserted_task():
    todo_list = ToDoList()
    todo_list.add_task("pizza tech")

    actual = todo_list.get_by_name("pizza tech")

    assert actual == "pizza tech"


def test_get_by_name_should_return_None_if_not_found():
    todo_list = ToDoList()
    todo_list.add_task("Johnny Dorelli")
    todo_list.add_task("Pippo Cappuccio")

    actual = todo_list.get_by_name("pizza tech")

    assert actual == None
