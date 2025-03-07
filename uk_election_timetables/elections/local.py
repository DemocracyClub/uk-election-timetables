from datetime import date

from uk_election_timetables.calendars import Country, working_days_before
from uk_election_timetables.election import Election


class LocalElection(Election):
    @property
    def sopn_publish_date(self) -> date:
        """
        Calculate the publish date for a local election.

        This is set out in:

         * `The Local Elections (Principal Areas) (England and Wales) (Amendment) Rules 2014 <https://www.legislation.gov.uk/uksi/2014/494/made>`_
         * `The Local Elections (Northern Ireland) Order 2010 <https://www.legislation.gov.uk/uksi/2010/2977/schedule/1/part/4/made>`_
         * `The Scottish Local Government Elections Order 2011 <https://www.legislation.gov.uk/ssi/2011/399/made>`_

        :return: a datetime representing the expected publish date
        """

        country_specific_duration = {
            Country.ENGLAND: 19,
            Country.NORTHERN_IRELAND: 16,
            Country.SCOTLAND: 23,
            Country.WALES: 19,
        }

        days_prior = country_specific_duration[self.country]

        return working_days_before(
            self.poll_date,
            days_prior,
            super()._calendar(),
        )
