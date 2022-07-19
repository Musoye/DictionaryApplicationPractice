import json
from difflib import get_close_matches

class Dictionary:
    """ A Simple Dictionary Appplication"""
    def __init__(self,word):
        self.word = word
           
    def meaning(self):
        data = json.load(open("static/db/data.json"))
        w =  self.word.lower()

        if w in data:
            output = data[w]
            return output

            
        elif len(get_close_matches(w, data.keys())) > 0:
            answer = input("Did you mean %s instead? if yes press Y and N if no.: " % get_close_matches(w, data.keys())[0])
            if answer == "Y":
               return   data[get_close_matches(w, data.keys())[0]]

            elif answer == "N":
                return "No such word in the dictionary"
            else:
                return "we didn't understand your entry"
        else:
            return "There is no such word"



        

        



        