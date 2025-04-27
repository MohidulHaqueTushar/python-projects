import requests
import json

api_request = requests.get(
    "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5&convert=USD&CMC_PRO_API_KEY=b2b7050d-9b1c-4cf8-85ed-dd17f3af9634"
)

api = json.loads(api_request.content)

my_coins = ["BTC", "ETH"]

for i in range(0, 5):
    for coin in my_coins:
        if api["data"][i]["symbol"] == coin:
            print(api["data"][i]["symbol"])
            print("{0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
            print("-----------------------")