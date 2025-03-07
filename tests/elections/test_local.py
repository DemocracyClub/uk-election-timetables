from datetime import date

from uk_election_timetables.calendars import Country
from uk_election_timetables.elections import LocalElection


# Reference election: local.highland.wester-ross-strathpeffer-and-lochalsh.by.2018-12-06
def test_publish_date_scottish_local():
    election = LocalElection(date(2018, 12, 6), Country.SCOTLAND)

    assert election.sopn_publish_date == date(2018, 11, 2)


# Reference election: local.belfast.balmoral.2019-05-02
def test_publish_date_northern_ireland_local():
    election = LocalElection(date(2019, 5, 2), Country.NORTHERN_IRELAND)

    assert election.sopn_publish_date == date(2019, 4, 8)


# Reference election: local.herefordshire.ross-north.2019-06-06
def test_publish_date_local_election_england():
    election = LocalElection(date(2019, 6, 6), country=Country.ENGLAND)

    assert election.sopn_publish_date == date(2019, 5, 9)


# Reference election: local.2021-05-06
def test_registration_deadline_local_election_england():
    election = LocalElection(date(2021, 5, 6), country=Country.ENGLAND)

    assert election.registration_deadline == date(2021, 4, 19)


# Reference election: local.2021-05-06
def test_postal_vote_application_deadline_local_election_england():
    election = LocalElection(date(2021, 5, 6), country=Country.ENGLAND)

    assert election.postal_vote_application_deadline == date(2021, 4, 20)


# Reference election: local.belfast.2023-05-18
def test_postal_vote_application_deadline_local_election_northern_ireland():
    deadline = LocalElection(
        date(2023, 5, 18), country=Country.NORTHERN_IRELAND
    ).postal_vote_application_deadline

    assert deadline == date(2023, 4, 26)
