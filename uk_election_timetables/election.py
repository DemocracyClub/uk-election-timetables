from abc import ABCMeta, abstractmethod
from datetime import date
from typing import Dict, List

from uk_election_timetables.calendars import (
    UnitedKingdomBankHolidays,
    Country,
    working_days_before,
)


class Election(metaclass=ABCMeta):
    BANK_HOLIDAY_CALENDAR = UnitedKingdomBankHolidays()

    def __init__(self, poll_date: date, country: Country):
        self.poll_date = poll_date
        self.country = country

    @property
    def postal_vote_application_deadline(self) -> date:
        """
        Calculates the postal vote application deadline for this Election

        This is set out in `The Representation of the People (England and Wales) Regulations 2001 <https://www.legislation.gov.uk/uksi/2001/341/regulation/56/made>`_.

        In Northern Ireland, this is set out in `The Representation of the People (Northern Ireland) Regulations 2008 <https://www.legislation.gov.uk/uksi/2008/1741/regulation/61/made>`

        :return: a datetime representing the postal vote application deadline
        """
        if self.country == Country.NORTHERN_IRELAND:
            return working_days_before(self.poll_date, 14, self._calendar())

        return working_days_before(self.poll_date, 11, self._calendar())

    @property
    def vac_application_deadline(self) -> date:
        """
        Calculates the Voter Authority Certificate (VAC) application deadline for this Election

        This is set out by the Electoral Commission here: https://www.electoralcommission.org.uk/cy/node/25624

        :return: datetime.date representing the VAC application deadline
        """
        return working_days_before(self.poll_date, 6, self._calendar())

    @property
    @abstractmethod
    def sopn_publish_date(self) -> date:
        pass

    @property
    def registration_deadline(self) -> date:
        """
        Calculates the voter registration deadline for this Election

        This explained in a `background note from the Electoral Commission <https://www.electoralcommission.org.uk/media/2457>`_

        :return: a datetime representing the voter registration deadline
        """
        return working_days_before(self.poll_date, 12, self._calendar())

    @property
    def timetable(self) -> List[Dict]:
        """
        An aggregate of all known dates for the specific election type.

        :return: a list representing the entire timetable for this particular election.
        """
        return sorted(
            [
                {
                    "label": "Register to vote deadline",
                    "date": self.registration_deadline,
                },
                {
                    "label": "List of candidates published",
                    "date": self.sopn_publish_date,
                },
                {
                    "label": "Postal vote application deadline",
                    "date": self.postal_vote_application_deadline,
                },
                {
                    "label": "VAC application deadline",
                    "date": self.vac_application_deadline,
                },
            ],
            key=lambda r: r["date"],
        )

    def _calendar(self):
        return self.BANK_HOLIDAY_CALENDAR.from_country(self.country)
