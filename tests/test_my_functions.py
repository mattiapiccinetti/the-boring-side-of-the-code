# # # # # # # # # # # # # # # #
#                             #
# The boring side of the code #
#                             #
# # # # # # # # # # # # # # # #

from src.my_functions import join_with_dash

# Good
def test_join_with_dash():
    word_1 = "foo"
    word_2 = "bar"

    actual = join_with_dash(word_1, word_2)

    assert actual == "foo-bar"


# Bad
def test_ok():
    word_1 = "foo"
    word_2 = "bar"
    r = join_with_dash(word_1, word_2)
    assert r == "foo-bar"


# Too many assertions
# def test_join_with_dash():
#     word_1 = "foo"
#     word_2 = "bar"

#     actual = join_with_dash(word_1, word_2)

#     assert actual == "foo-bar"

#     word_3 = "baz"
#     word_4 = "gaglioffo"

#     actual = join_with_dash(word_3, word_4)

#     assert actual == "baz-gaglioffo"

#     word_empty = ""
#     word_none = None

#     actual = join_with_dash(word_empty, word_none)

#     assert actual == ""


# Too much JS minifier :D
# def test_join_with_dash():
#     word_1 = "foo"
#     word_2 = "bar"
#     word_3 = "baz"
#     word_4 = "gaglioffo"
#     word_empty = ""
#     word_none = None
#     actual = join_with_dash(word_1, word_2)
#     assert actual == "foo-bar"
#     actual = join_with_dash(word_3, word_4)
#     assert actual == "baz-gaglioffo"
#     actual = join_with_dash(word_empty, word_none)
#     assert actual == ""


def test_join_with_dash_empty_first():
    word_1 = ""
    word_2 = "bar"

    actual = join_with_dash(word_1, word_2)

    assert actual == "-bar"


def test_join_with_dash_none_second():
    word_1 = "foo"
    word_2 = None

    actual = join_with_dash(word_1, word_2)

    assert actual == "foo-None"
