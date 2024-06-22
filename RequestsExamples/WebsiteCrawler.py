import requests
from bs4 import BeautifulSoup
foundLinks = []
targetUrl = "https://www.sis.itu.edu.tr/"
def makeRequest(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")
    return soup

def crawl(url):
    links = makeRequest(url)
    for link in links.find_all("a"):
        foundLink = link.get("href")
        if foundLink:
            if "#" in foundLink:
                continue
            if url in foundLink and foundLink not in foundLinks:
                foundLinks.append(foundLink)
                print(foundLink)
                # recursive function
                crawl(foundLink)
        with open("yonlendirmeler.txt", "w") as y:
            for a in foundLinks:
                y.write(a + "\n")
            y.close()
crawl(targetUrl)