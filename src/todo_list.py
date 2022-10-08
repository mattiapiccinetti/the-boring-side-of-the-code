# # # # # # # # # # # # # # # #
#                             #
# The boring side of the code #
#                             #
# # # # # # # # # # # # # # # #
from typing import Optional


class ToDoList:
    def __init__(self, tasks: list[str] = None) -> None:
        self.tasks = [] if tasks is None else tasks

    def add_task(self, text: str) -> int:
        self.tasks.append(text)

        return len(self.tasks) - 1

    def get_by_name(self, task_name: str) -> Optional[str]:
        return next((x for x in self.tasks if x == task_name), None)

    def delete_task(self, task_id: str) -> None:
        raise NotImplementedError

    def clear(self) -> None:
        raise NotImplementedError
