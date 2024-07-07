import re
import requests
from bs4 import BeautifulSoup

anyList=[]
anyObject={}

target_url="https://www.amazon.com.tr/Karadeniz-Siyah-Bardak-Po%C5%9Fet-100l%C3%BC/dp/B07MF98XZ3?pd_rd_w=UMgVr&content-id=amzn1.sym.8c686600-0807-4f40-a265-5a598b06d7aa&pf_rd_p=8c686600-0807-4f40-a265-5a598b06d7aa&pf_rd_r=KXC82YD3CM8SJSB0TK66&pd_rd_wg=K0HD6&pd_rd_r=b26488eb-434e-4702-b710-4d720fa90e1c&pd_rd_i=B07MF98XZ3&ref_=pd_bap_d_grid_rp_0_1_ec_pr_pd_hp_d_atf_rp_2_i&th=1"
headers={"accept-language": "en-US,en;q=0.9","accept-encoding": "gzip, deflate, br","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"}

resp = requests.get(target_url,headers=headers)
print(resp.status_code)

soup=BeautifulSoup(resp.text,'html.parser')

try:
    anyObject["title"]=soup.find('span',{'id':'productTitle'}).text.strip()
except:
    anyObject["title"]=None

# allimages = soup.find_all("div",{"class":"imgTagWrapper"})
# print(len(allimages))

images = re.findall('"hiRes":"(.+?)"', resp.text)
anyObject["images"]=images

print(anyObject["title"])
imageslist = list()
for word in anyObject["images"]:
    if word not in imageslist:
        imageslist.append(word)
print(imageslist)


try:
    anyObject["price"]=(soup.find("span",{"class":"a-price-whole"}).text + soup.find("span",{"class":"a-price-fraction"}).text)
except:
    anyObject["price"]=None

print(anyObject["price"])