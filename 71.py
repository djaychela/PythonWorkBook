import requests, pprint

req = requests.get("http://www.pythonhow.com/data/universe.txt")
text_list = list(req.text)
print(text_list.count('a'))

