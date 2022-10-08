# # # # # # # # # # # # # # # #
#                             #
# The boring side of the code #
#                             #
# # # # # # # # # # # # # # # #

from src.travel_card_v1 import TravelCard
from datetime import datetime
from datetime import timedelta
from freezegun import freeze_time


@freeze_time()
def test_get_expiration():
    travel_card = TravelCard(42, 7)

    actual = travel_card.get_expiration()

    assert actual == datetime.now() + timedelta(days=365 * 7)
