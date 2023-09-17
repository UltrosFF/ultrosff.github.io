import requests
import json

page = 1
base_url = "https://server.jpgstoreapis.com/policy/a5bb0e5bb275a573d744a021f9b3bff73595468e002755b447e01559/listings"
jpg_url = "https://www.jpg.store/asset/"
response_page = f"{base_url}?page={page}"
results = []
data = requests.get(response_page).json()

class Offer:
    def __init__(self, offer, ratio):
        self.asset = offer["asset_id"]
        self.count = len(offer["bundled_assets"])
        self.price = int(int(offer["price_lovelace"]) / 1000000)
        self.ratio = round(ratio, 2)
        self.link = jpg_url + self.asset

    def to_dict(self):
        return {
            "asset": self.asset,
            "count": self.count,
            "price_total": self.price,
            "price_per": self.ratio,
            "link": self.link
        }

while True:
    response_page = f"{base_url}?page={page}"
    data = requests.get(response_page).json()
    
    print(f"current page: {page}")
    for offer in data:
        if "listing_type" in offer:
            if offer["listing_type"] == "BUNDLE":
                
                asset = offer["asset_id"]
                asset_count = len(offer["bundled_assets"])
                price = int(int(offer["price_lovelace"]) / 1000000)
                ratio = price / asset_count
                test_class = Offer(offer, ratio)
                results.append(test_class)
                
    if len(data) < 75:
        break
    page += 1

sorted_results = sorted(results, key=lambda offer: offer.ratio)

# Convert the results to a dictionary
output_data = {"content": sorted_results}

# Save the output data to output.json
with open("output.json", "w") as outfile:
    json.dump(output_data, outfile, indent=4)
