def count_words(string):
    words = string.replace(',',' ')
    words = words.split(' ')
    return len(words)


with open('words2.txt','r') as file:
    contents = file.read()
    print(count_words(contents))