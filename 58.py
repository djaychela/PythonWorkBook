import json

with open('ex_58.json','r') as file:
    content = json.loads(file.read())
print(content)
content['employees'].append({'firstName':'Albert','lastName':'Bert'})
print(content)
with open('ex_58.json','w') as file:
    file.write(json.dumps(content, sort_keys=True, indent=4))