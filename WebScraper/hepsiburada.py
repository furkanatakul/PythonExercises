import requests
from bs4 import BeautifulSoup

url = "https://www.hepsiburada.com/laptop-notebook-dizustu-bilgisayarlar-c-98"

header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"}

html = requests.get(url, headers=header).content

soup = BeautifulSoup(html,"html.parser")

list = soup.find_all("li",{"class" : "productListContent-zAP0Y5msy8OHn5z7T_K_"})

j  = 1
for i in list:
    productName = i.find("div", {"class" : "moria-ProductCard-fHiOwt"}).h3.text
    price = i.find("div", {"data-test-id" : "price-current-price"}).text
    print(f"{j}.Ürün:", productName, price)
    j += 1
