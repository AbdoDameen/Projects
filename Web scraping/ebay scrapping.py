import requests
from bs4 import BeautifulSoup
import pandas

url=("https://www.ebay.com.au/sch/i.html?_from=R40&_sacat=0&LH_TitleDesc=0&LH_Complete=1&LH_Sold=1&_nkw=rolex&_blrs=spell_check&rt=nc&Model=Rolex%2520Datejust&_dcat=31387")

def get_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup

def parse(soup):
    productlist = []
    results = soup.find_all('div', {'class': 's-item__info clearfix'})
    for item in results:
        products = {
            'title':item.find('h3',{'class': "s-item__title s-item__title--has-tags"}).text,
            'soldprice':float(item.find('span', {'class': 's-item__price'}).text.replace('$', '').replace(',','').replace('AU','').strip()),
            'solddate':item.find('span', {'class': 's-item__title--tagblock__COMPLETED'}).find('span', {'class':'POSITIVE'}).text,
            'bids':item.find('div', {'class': 'bidCount'}),
            'link': item.find('a', {'class': 's-item__link'})['href'],
        }
        productlist.append(products)

    return productlist

def output(productlist):
    productsdf = pandas.DataFrame(productlist)
    productsdf.to_csv("output.csv")
    print("saved to csv")
    return
soup = get_data(url)
productlist = parse(soup)
output(productlist)
