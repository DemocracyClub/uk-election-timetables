from sopn_publish_date.calendars import working_days, UnitedKingdomBankHolidays, as_date

from datetime import datetime, date


class InvalidElectionId(BaseException):
    pass


class AmbiguousElectionId(BaseException):
    pass


class StatementPublishDate(object):
    def __init__(self):
        self.calendar = UnitedKingdomBankHolidays()

    @staticmethod
    def _extract_from_id(election_id):
        try:
            election_type, *_, poll_date = election_id.split(".")

            date_of_poll = datetime.strptime(poll_date, "%Y-%m-%d").date()

            return election_type, date_of_poll
        except Exception:
            raise InvalidElectionId(
                "Parameter [%s] is not in election id format" % election_id
            )

    def for_id(self, election_id):

        election_type, poll_date = StatementPublishDate._extract_from_id(election_id)

        if election_type == "nia":
            return self.northern_ireland_assembly(poll_date)
        elif election_type == "sp":
            return self.scottish_parliament(poll_date)
        elif election_type == "naw":
            return self.national_assembly_for_wales(poll_date)
        elif election_type == "gla" or "mayor.london" in election_id:
            return self.greater_london_assembly(poll_date)
        elif election_type == "pcc":
            return as_date(poll_date - working_days(18, self.calendar.england_and_wales()))
        elif election_type == "mayor":
            return as_date(poll_date - working_days(19, self.calendar.england_and_wales()))
        else:
            raise AmbiguousElectionId(
                "Cannot derive country from election id [%s]" % election_id
            )

    def northern_ireland_assembly(self, poll_date: date) -> date:
        return as_date(poll_date - working_days(16, self.calendar.northern_ireland()))

    def scottish_parliament(self, poll_date: date) -> date:
        return as_date(poll_date - working_days(23, self.calendar.scotland()))

    def national_assembly_for_wales(self, poll_date: date) -> date:
        return as_date(poll_date - working_days(19, self.calendar.england_and_wales()))

    def greater_london_assembly(self, poll_date: date) -> date:
        return as_date(poll_date - working_days(23, self.calendar.england_and_wales()))

    def police_and_crime_commissioner(self, poll_date: date) -> date:
        return as_date(poll_date - working_days(18, self.calendar.northern_ireland()))

    def for_country(self, country, poll_date: date) -> date:

        if country == "northern-ireland":
            return as_date(poll_date - working_days(16, self.calendar.northern_ireland()))
        elif country == "scotland":
            return as_date(poll_date - working_days(23, self.calendar.scotland()))
        elif country == "england" or country == "wales":
            return as_date(poll_date - working_days(19, self.calendar.england_and_wales()))
        else:
            raise Exception(
                "Not implemented for election: [%s,%s]" % (country, poll_date)
            )
