import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

url= "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

rr = requests.get(url)
soup = BeautifulSoup(rr.text,"lxml")
# find()
price = (soup.find('h4',{'class':"pull-right price"}))
print(price.string)

desc = (soup.find('p',{'class':"description"}))
print(desc.string)

d = (soup.find('p', class_="description"))
print(d.string)

# find_all()

c = (soup.find_all('h4', class_="pull-right price"))
#print(len(c))

for i in c :
    print(i.text)
    
e = (soup.find_all('p', class_="description"))
print(e[3].string)

# find_all() with Rejex

f = (soup.find_all(string ="Galaxy Tab 3"))
print(f)

ff = (soup.find_all(string =re.compile("Galaxy")))
print(ff)

# findall() with Pandas

name = soup.find_all('a',class_ = 'title')
product_name=[]

for i in name:
    name = i.text
    product_name.append(name)
    
print(product_name)

prices = soup.find_all('h4',class_ = 'pull-right price')
prices_list=[]

for i in prices:
    prices = i.text
    prices_list.append(prices)
    
print(prices_list)

dec = soup.find_all('p',class_ = 'description')
dec_list=[]

for i in dec:
    dec = i.text
    dec_list.append(dec)
    
print(dec_list)


reviews = soup.find_all('p',class_ = 'pull-right')
reviews_list=[]

for i in reviews:
    reviews = i.text
    reviews_list.append(reviews)
    
print(reviews_list)

df = pd.DataFrame({'products name': product_name,'Prices': prices_list,'Reviews': reviews_list})
print(df)

#df.to_csv('us.csv')


# nested Data scraping

box = soup.find_all('div',class_ = 'col-sm-4 col-lg-4 col-md-4') [3]
print(box)

name = box.find('a').text
print(name)

decc = box.find('p').text
print(decc)

r = box.find('p',class_='pull-right').text
print(r)

# scrap data from multiple pages

