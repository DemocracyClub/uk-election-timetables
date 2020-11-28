# uk-election-timetables

[![Build Status](https://travis-ci.com/DemocracyClub/uk-election-timetables.svg?branch=main)](https://travis-ci.com/DemocracyClub/uk-election-timetables)
[![Documentation Status](https://readthedocs.org/projects/uk-election-timetables/badge/?version=latest)](https://uk-election-timetables.readthedocs.io/en/latest/overview.html?badge=latest)
[![PyPI](https://img.shields.io/pypi/v/uk-election-timetables.svg)](https://pypi.org/project/uk-election-timetables/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

This library encapsulates timetable legislation for elections run in the United Kingdom and its devolved administrations.

The election timetable varies based on:

 * *Type of Post* - Parliamentary, Local, devolved Government, etc.
 * *Country* - The United Kingdom has up to four different rules for the same type of election, one for each country.
 * *Calendar* - each country has their own unique set of Bank Holidays.

## Usage (publishing of candidate lists)

```python
from datetime import date
from uk_election_timetables.elections.uk_parliament import UKParliamentElection

election = UKParliamentElection(date(2019, 2, 21))

print(election.sopn_publish_date) # date(2019, 1, 25)
```

## Documentation

Hosted by readthedocs at [https://uk-election-timetables.readthedocs.io/](https://uk-election-timetables.readthedocs.io/en/latest/overview.html)

## Installation

`pip install uk_election_timetables`
 
## Test

`pytest`

## Supported Election Types

 - [x] Local
 - [x] United Kingdom Parliament
 - [x] Scottish Parliament
 - [x] Senedd Cymru
 - [x] Northern Ireland Assembly
 - [x] Mayoral
 - [x] Mayoral (London)
 - [x] Greater London Assembly
 - [x] Police and Crime commissioner
