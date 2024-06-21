import requests
def cryptoData():
    response = requests.get("")
    if response.status_code == 200:
        return response.json()
    #print(response.json())
    #for crypto in response.json():
        #print(crypto["currency"] + " --> " + crypto["price"])

cryptoResponse = cryptoData()
userInput = input("Enter your crypto currency: ")
for crypto in cryptoResponse:
        if crypto["currency"] == userInput:
            print(crypto["price"])
            break


