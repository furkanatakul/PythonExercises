import requests

#targetInput = input("Enter your target website: ")
targetInput = "google.com"
with open("subdomainlist.txt", "r") as subdomainList:
    for word in subdomainList:
        word = word.strip()
        url = "http://" + word + "." + targetInput
        try:
            response = requests.get(url)
            print("Subdomain Found --->", url)
        except requests.exceptions.ConnectionError:
            continue