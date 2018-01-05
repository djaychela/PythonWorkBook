def count_words(string):
    return len(string.split())


with open('words1.txt','r') as file:
    text = file.read()
    print(count_words(text))