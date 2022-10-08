# # # # # # # # # # # # # # # #
#                             #
# The boring side of the code #
#                             #
# # # # # # # # # # # # # # # #
from src.user_service_client import UserServiceClient
from typing import Optional


class UserNormalizer:
    def __init__(self) -> None:
        pass

    def normalize(self, user_id: int) -> tuple[int, Optional[str]]:
        client = UserServiceClient()
        response = client.get_user_by_id(user_id)

        normalized_user = None if response[1] is None else response[1].lower()

        return (user_id, normalized_user)
