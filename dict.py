import json

def meaning(word):
    "This is a simple dictionary"

    data = json.load(open("static/db/data.json"))
    w =  word.lower()

    if w in data:
        output = data[w]
        return output
    else:
        return "There is no such word in the dictionary.You should either check your spellings or the word doesn't exit"

# mus = input("Enter a word: ")
# print(meaning(mus))