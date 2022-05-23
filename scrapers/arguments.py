import requests
from bs4 import BeautifulSoup
import sys
import json

supreme_court_arguments = []

# scrape from most current
url = 'https://www.supremecourt.gov/oral_arguments/argument_audio.aspx'

# scrape from specific year (earliest is 2010)
if len(sys.argv) > 1:

    year = sys.argv[1] 
    url = 'https://www.supremecourt.gov/oral_arguments/argument_audio/' + year

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

for a in soup.find_all('a'):
    if 'href' in a.attrs:
        path = a.get('href')
        if '../audio' in path:

            path = path.replace("../", "")
            r = requests.get('https://www.supremecourt.gov/oral_arguments/' + path)
            soup = BeautifulSoup(r.content, 'html.parser')

            title = soup.find(id="ctl00_ctl00_MainEditable_mainContent_lblCaseName")
            docket = soup.find(id="ctl00_ctl00_MainEditable_mainContent_lblDocket")
            date = soup.find(id="ctl00_ctl00_MainEditable_mainContent_lblDate")

            transcript_url = ""
            audio_url = ""

            for a in soup.find_all('a'):
                if 'href' in a.attrs:
                    path = a.get('href')

                    if '.mp3' in path:
                        audio_url = path  
                    if 'argument_transcripts' in path:
                        transcript_url = 'https://www.supremecourt.gov' + path 

            supreme_court_arguments.append({
                'title': title.text, 'date': date.text, 'docket': docket.text, 
                'audioUrl': audio_url, 'transcriptUrl': transcript_url
            })


if len(sys.argv) > 1:
    year = sys.argv[1] 
    with open('data/arguments-' + year + '.json', "w") as outfile:
        json.dump(supreme_court_arguments, outfile, indent=4)
else:
    with open('data/arguments.json', "w") as outfile:
        json.dump(supreme_court_arguments, outfile, indent=4)




