# # # # # # # # # # # # # # # #
#                             #
# The boring side of the code #
#                             #
# # # # # # # # # # # # # # # #

from src.travel_card_v2 import TravelCard
from datetime import datetime
from datetime import timedelta


def test_get_expiration():
    now = datetime.now()
    travel_card = TravelCard(user_id=42, validity_in_years=4, datetime_fn=lambda: now)

    actual = travel_card.get_expiration()

    assert actual == now + timedelta(days=365 * 4)
