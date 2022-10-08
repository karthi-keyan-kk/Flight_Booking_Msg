import requests
from pprint import pprint

SHEET_ENDPOINT = "https://api.sheety.co/b4ba44c8a7eeeed6d3453481bbd12ae7/copyOfFlightDeals/prices"


class DataManager:
    def __int__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEET_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_dictionary(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEET_ENDPOINT}/{city['id']}", json=new_data)
            print(response.text)
