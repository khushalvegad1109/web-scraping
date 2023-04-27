import requests
from bs4 import BeautifulSoup

url= "https://webscraper.io/test-sites/e-commerce/allinone/computers"

rr = requests.get(url)
#print(rr.status_code)
#print(rr.text)
soup = BeautifulSoup(rr.text,"lxml")
#print(soup)
#print(soup.div)
#print(soup.div.a)
# tag = soup.header
# atb = (tag.attrs)
# print(atb['class'])

tag = soup.header.a.button.span
print(tag.string)

