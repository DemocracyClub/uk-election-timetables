from uk_election_timetables.calendars import UnitedKingdomBankHolidays

uk_calendars = UnitedKingdomBankHolidays()

scotland = uk_calendars.scotland()
england_and_wales = uk_calendars.england_and_wales()
northern_ireland = uk_calendars.northern_ireland()


def test_should_separate_by_country():
    should_not_contain_holiday(england_and_wales, "St Patrick’s Day")

    should_not_contain_holiday(
        scotland, "Battle of the Boyne (Orangemen’s Day)"
    )

    should_not_contain_holiday(northern_ireland, "St Andrew’s Day")


def should_not_contain_holiday(calendar, name):
    assert not [
        holiday for holiday in calendar.exempted_dates() if holiday.name == name
    ]


def test_scotland_exempted_dates_contain_easter_monday():
    # We know Easter Monday 2024 is not in the Scotland Bank Holidays JSON
    # https://github.com/DemocracyClub/uk-election-timetables/blob/a4c33fd8b1befc801d83537bdbb8300a5e011318/uk_election_timetables/bank-holidays.json#L1486-L1497
    # but it should be in Scotland exempted dates anyway
    easter_monday_2024 = next(
        (
            d
            for d in scotland.exempted_dates()
            if d.name == "Easter Monday" and d.year == 2024
        ),
        None,
    )
    assert easter_monday_2024 is not None
    assert easter_monday_2024.month == 4
    assert easter_monday_2024.day == 1
