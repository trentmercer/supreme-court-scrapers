## Supreme Court Scrapers

This repository contains the code responsible for scraping from the Supreme Court website

## Schedule 
https://www.supremecourt.gov/oral_arguments/2022TermCourtCalendar.pdf

- Court calendar
- Day Call 
- Argument Audio and Transcripts
- Opinions of the court
- Case documents

# Setup

```pip3 install -r requirements.txt```

# Scrape argument audio and transcripts (2010 - present)

outputs to data/ directory

Scrape arguments for the current session ```python3 scrapers/arguments.py```

Scrape arguments from a specific year ```python3 scrapers/arguments.py 2019```


# Scrape archived argument transcripts

Coming Soon