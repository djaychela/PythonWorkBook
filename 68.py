d = dict(weather = "clima", earth = "terra", rain = "chuva")
def translate(string):
    if string not in d.keys():
        return "That word doesn't exist"
    else:
        return d[string]

trans = input("Enter Word: ")
print(translate(trans.lower()))