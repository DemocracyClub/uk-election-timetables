# sopn-publish-date

> Given the polling day of an election in the UK, when should the Statement of Persons Nominated (SoPN) should be published?

Turns out this is a non-trivial question, depending on:

- type of election
- country
- calendars and bank holidays

## Usage

This library defines a single function `sopn_publish_date` which takes a string `election_id` in [uk-election-ids](https://elections.democracyclub.org.uk/reference_definition/) format and returns a `datetime` representing the day when the SoPN is published.

```python
from sopn_publish_date import sopn_publish_date

local_election_sopn = sopn_publish_date('local.cardiff.2019-02-21')

# datetime.datetime(2019, 1, 25)
```

## Test

`python -m pytest`

## Todo

Election types:

 - [x] Local
 - [x] Parliament
 - [x] Scottish Parliament
 - [ ] National Assembly for Wales
 - [ ] Northern Irish Assembly
 - [ ] Mayoral
 - [ ] EU parliament
 - [ ] Greater London Assembly
 - [ ] Police and Crime commissioner
 
Calendars:
 - [x] England + Wales
 - [x] Scotland
 - [ ] Northern Ireland
 - [ ] Isle of Man?
 - [ ] Fixed-date bank holidays e.g. royal weddings
 
 
 
 