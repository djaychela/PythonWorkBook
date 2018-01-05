import webbrowser

url = input('enter search term: ')
url = 'https://www.google.co.uk/search?dcr=0&source=hp&ei=MrlIWrPDGIa00gXyr46oDA&q=' + url
webbrowser.open(url)