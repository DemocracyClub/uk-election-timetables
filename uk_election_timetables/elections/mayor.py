from datetime import date

from uk_election_timetables.calendars import Country, working_days_before
from uk_election_timetables.election import Election


class MayoralElection(Election):
    def __init__(self, poll_date: date):
        """
        :param poll_date: a datetime representing the date of the poll
        """
        Election.__init__(self, poll_date, Country.ENGLAND)

    @property
    def sopn_publish_date(self) -> date:
        """
        Calculate the publish date for an election to the position of Mayor in England and Wales

        This is set out in
        - `The Local Authorities (Mayoral Elections) (England and Wales) (Amendment) Regulations 2014 <https://www.legislation.gov.uk/uksi/2014/370/made>`_
        - `The Combined Authorities (Mayoral Elections) Order 2017 <https://www.legislation.gov.uk/uksi/2017/67/made>`_

        :return: a datetime representing the expected publish date
        """
        return working_days_before(self.poll_date, 19, super()._calendar())
