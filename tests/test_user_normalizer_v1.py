# # # # # # # # # # # # # # # #
#                             #
# The boring side of the code #
#                             #
# # # # # # # # # # # # # # # #

from src.user_normalizer_v1 import UserNormalizer

# Too slow
def test_normalize_should_return_lowercase_user():
    user_normalizer = UserNormalizer()

    actual = user_normalizer.normalize(2)

    assert actual == (2, "leo brock")
