import requests
import json

response = requests.get("https://api.coincap.io/v2/assets/bitcoin")

print(json.dumps(response.json(), indent=4))
