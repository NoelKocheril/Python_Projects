import json
from difflib import SequenceMatcher
from difflib import get_close_matches

dict = json.load(open("dict.json"))

def strip_def(w):
    out = ""
    for e in w:
        out += e + '\n'
    return out

def define(w):
    w = w.lower()
    if w in dict:
        return strip_def(dict[w])
    elif w.title() in dict:
        return strip_def(dict[w.title()])
    elif w.upper() in dict:
        return strip_def(dict[w.upper()])
    else:
        matches = get_close_matches(w,dict.keys())
        for m in matches:
            if(input("Did you mean %s? (press Y) " % m).upper() == "Y"):
                return strip_def(dict[m])
        return "The Word does not exist, please try again"

word = input("Enter a Word: ")
print(define(word))
