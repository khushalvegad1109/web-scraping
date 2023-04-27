import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

product_name=[]
product_price=[]
product_dec=[]
product_review=[]

for i in range(2,40):
    url= "https://www.flipkart.com/search?q=mobiles+under+15000&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_2_8_na_na_ps&otracker1=AS_Query_OrganicAutoSuggest_2_8_na_na_ps&as-pos=2&as-type=RECENT&suggestionId=mobiles+under+15000&requestId=1246b6d8-5ca6-413f-a919-5dea7a54ad1f&as-searchtext=mobiles+&page="+str(i)

    rr = requests.get(url)
    #print(rr)

    soup = BeautifulSoup(rr.text,"lxml")
    #print(soup)

    box = soup.find('div',class_="_1YokD2 _3Mn1Gg")
    name = box.find_all('div',class_="_4rR01T")

    for i in name:
        name = i.text
        product_name.append(name)

        print(product_name)

    price = box.find_all('div',class_="_30jeq3 _1_WHN1")

    for i in price:
        price = i.text
        product_price.append(price)

        print(product_price)

    dec = box.find_all('ul',class_="_1xgFaf")
    

    for i in dec:
        dec = i.text
        product_dec.append(dec)

        print(product_dec)

    review = box.find_all('div',class_="_3LWZlK")
    

    for i in review:
        review = i.text
        product_review.append(review)

        print(product_review)

    df = pd.DataFrame({'products Name': product_name,'Prices': product_price,'Reviews': product_review,"Dec":product_dec})
    print(df)

    df.to_csv('flipkart.csv')
