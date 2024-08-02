import requests
import json

url = "https://jsonguide.technologychannel.org/quotes.json"

f = requests.get(url)
text = f.text
obj = json.loads(text)

print(obj)