# # # # # # # # # # # # # # # #
#                             #
# The boring side of the code #
#                             #
# # # # # # # # # # # # # # # #

from unittest.mock import Mock
from src.user_normalizer_v2 import UserNormalizer
from src.user_service_client import UserServiceClient
from typing import Optional

# Option 1
def test_normalize_should_return_lowercase_user_with_mock():
    client = UserServiceClient()
    client.get_user_by_id = Mock(return_value=(42, "John Doe"))
    user_normalizer = UserNormalizer(client)

    actual = user_normalizer.normalize(42)

    assert actual == (42, "john doe")


# Option 2
def test_normalize_should_return_lowercase_user():
    fake_client = FakeClient()
    user_normalizer = UserNormalizer(fake_client)

    actual = user_normalizer.normalize(2)

    assert actual == (2, "john doe")


class FakeClient(UserServiceClient):
    def get_user_by_id(self, id: int) -> tuple[int, Optional[str]]:
        return (id, "John Doe")
