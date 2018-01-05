with open('urls.txt','r') as file:
    for url in file.readlines():
        url = url.replace('https:/','http://')
        print(url)
