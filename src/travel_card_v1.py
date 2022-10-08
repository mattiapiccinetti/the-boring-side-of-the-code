# # # # # # # # # # # # # # # #
#                             #
# The boring side of the code #
#                             #
# # # # # # # # # # # # # # # #

from datetime import datetime, timedelta


class TravelCard:
    def __init__(self, user_id: str, validity_in_years: int) -> None:
        self.user_id = user_id
        self._created_at = datetime.now()
        self._validity_in_years = validity_in_years

    def get_expiration(self) -> datetime:
        return self._created_at + timedelta(days=365 * self._validity_in_years)
