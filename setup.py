from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="uk-election-timetables",
    url="https://github.com/DemocracyClub/uk-election-timetables",
    version="2.2.3",
    description="Derives significant dates for UK elections",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Alex Wilson",
    author_email="alex+github@probablyfine.co.uk",
    license="MIT",
    packages=find_packages(exclude=("tests",)),
    package_data={"uk_election_timetables": ["bank-holidays.json"]},
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development",
        "Topic :: Software Development :: Documentation",
    ],
)
