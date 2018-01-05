import requests

f1 = requests.get("http://www.pythonhow.com/data/sampledata.txt").text
f2 = requests.get("http://www.pythonhow.com/data/sampledata_x_2.txt").text[3:]

with open('ex_74.txt','w') as file:
    file.write(f1 + f2)

print(f1 + f2)