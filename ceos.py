import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

url= "https://www.linkedin.com/search/results/people/?geoUrn=%5B%22103644278%22%5D&keywords=ceos&origin=FACETED_SEARCH&searchId=e21f9d9c-a051-4f69-b5c0-57fd1b9120d6&sid=i3v"

rr = requests.get(url)
#print(rr.status_code)
#print(rr)

soup = BeautifulSoup(rr.text,"lxml")
#print(soup)

#name = soup.main.ul.div.a.span

name = soup.find('a', class_="app-aware-link  scale-down ").get("href")
print(name)


