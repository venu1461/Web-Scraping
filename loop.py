# It gives the easy to understand the code and headers 
import requests
import bs4
port=requests.get("https://www.cricbuzz.com/live-cricket-scores/105778/ind-vs-eng-4th-test-india-tour-of-england-2025")
soup=bs4.BeautifulSoup(port.content,'html.parser')
print(soup.prettify())
print(port.headers.items())
for key,value in port.headers.items():
    print(f"{key}--{value}")