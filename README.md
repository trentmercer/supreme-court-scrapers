## Supreme Court Scrapers

This repository contains the code responsible for scraping from the Supreme Court website

## Schedule 
https://www.supremecourt.gov/oral_arguments/2022TermCourtCalendar.pdf

- Court calendar
- Argument Audio and Transcripts

# Setup

```pip3 install -r requirements.txt```

# Scrape argument audio and transcripts (2010 - present)

outputs to data/ directory

Scrape arguments for the current session ```python3 scrapers/arguments.py```

Scrape arguments from a specific year ```python3 scrapers/arguments.py 2019```


# Scrape archived argument transcripts

Coming Soon

- Orders of the court
- Orders by circuit
- Case Documents
- Current members
- Circuit assignments 
- Opinions of the court
- Online sources cited in opinions
- Opinions relating to orders 