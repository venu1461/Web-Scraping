# this is basic introduction for web scraping
import requests
import bs4
port=requests.get("https://www.cricbuzz.com/live-cricket-scores/105778/ind-vs-eng-4th-test-india-tour-of-england-2025")
soup=bs4.BeautifulSoup(port.content,'html.parser')
print(soup.prettify())