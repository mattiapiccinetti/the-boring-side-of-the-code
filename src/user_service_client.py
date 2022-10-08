# # # # # # # # # # # # # # # #
#                             #
# The boring side of the code #
#                             #
# # # # # # # # # # # # # # # #

from typing import Optional

_USER_DATABASE: dict[int, str] = {
    0: "Ray Proctor",
    1: "Ila Harrison",
    2: "Leo Brock",
    3: "Jon Carrillo",
    4: "Liz Shepherd",
    5: "Von Hayden",
    6: "Son Fuller",
    7: "Ann Crawford",
    8: "Ken Mack",
    9: "Bud Wagner",
}


class UserServiceClient:
    def __init__(self) -> None:
        pass

    def get_user_by_id(self, id: int) -> tuple[int, Optional[str]]:
        return _long_http_call(id)


def _long_http_call(id: int) -> tuple[int, Optional[str]]:
    import time

    time.sleep(5)

    return (id, _USER_DATABASE.get(id))
