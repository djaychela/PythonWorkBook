import json
import pprint

with open('ex_56.json','r') as file:
    content = file.read()
content = json.loads(content)
pprint.pprint(content)