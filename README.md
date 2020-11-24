# uk-election-timetables

[![Build Status](https://travis-ci.org/DemocracyClub/uk-election-timetables.svg?branch=master)](https://travis-ci.org/DemocracyClub/uk-election-timetables)
[![Documentation Status](https://readthedocs.org/projects/uk-election-timetables/badge/?version=latest)](https://uk-election-timetables.readthedocs.io/en/latest/overview.html?badge=latest)
[![Coverage Status](https://coveralls.io/repos/github/DemocracyClub/uk-election-timetables/badge.svg?branch=master)](https://coveralls.io/github/DemocracyClub/uk-election-timetables?branch=master)
[![PyPI](https://img.shields.io/pypi/v/uk-election-timetables.svg)](https://pypi.org/project/uk-election-timetables/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)


> Given the polling day of an election in the UK, when are candidate lists published?

This library encapsulates timetable legislation for elections run in the United Kingdom and its devolved administrations.

The election timetable varies based on:

 * *Type of Post* - Parliamentary, Local, devolved Government, etc.
 * *Country* - The United Kingdom has up to four different rules for the same type of election, one for each country.
 * *Calendar* - each country has their own unique set of Bank Holidays.

## Usage (publishing of candidate lists)

```python

from uk_election_timetables.sopn import StatementPublishDate
from datetime import date

publish_date = StatementPublishDate()

print(publish_date.national_assembly_for_wales(date(2016, 5, 5)))

# datetime.date(2016, 4, 7)
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
 - [x] National Assembly for Wales
 - [x] Northern Ireland Assembly
 - [x] Mayoral
 - [x] Mayoral (London)
 - [x] European Parliament
 - [x] Greater London Assembly
 - [x] Police and Crime commissioner
