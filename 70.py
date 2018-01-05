import requests, pprint

req = requests.get("http://www.pythonhow.com/data/universe.txt")
pprint.pprint(req.text)