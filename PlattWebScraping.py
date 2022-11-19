import bs4
from bs4 import BeautifulSoup
import requests
import pandas

#empty list to store
dataList=[]

#loop through pages - does NOT include last number
for page in range(1,10):

    #request
    showCount = str(64)
    stringPage = str(page)
    baseUrl = f'https://www.platt.com/s/electrical-conduit-wire-duct-electrical-raceway?cat=r1imf5&show={showCount}&page={stringPage}'
    r = requests.get(baseUrl)
    c = r.content
    
    #parse
    soup=BeautifulSoup(c,"html.parser")
    #print(soup.prettify())

    #find all divs with specific class for name of item
    allItems=soup.find_all("div",{"class":"body-1 text--primary font-weight-medium"})
    #firstItem=allItems[0].text.strip()
    #print(firstItem)

    #find all spans with specific class for price
    allPrices=soup.find_all("span",{"class":"text--black"})
    #firstPrice=allPrices[0].text.strip()
    #print(firstPrice)

    #find all spans with specific class for unit
    allUnits=soup.find_all("span",{"class":"text-overline"})
    #firstUnit=allUnits[0].text.strip()
    #print(firstUnit)

    #loop through all items and prices
    
    for i in range(0,int(showCount)):

        #empty dictionary
        d={}

        #fill dictionary
        d["Description"] = allItems[i].text.strip()

        #add if statement
        d["Price"] = allPrices[i].text.strip()
        d["Unit"] = allUnits[i].text.strip()

        #append dictionary to list
        dataList.append(d)


#print list to test to see if you did it right lol
#print(list)

#turn into data frame
df = pandas.DataFrame(dataList)
print(df.head())
print(df.describe())

#make into csv
df.to_csv("Data.csv")




