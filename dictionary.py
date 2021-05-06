import json
from difflib import get_close_matches


data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        match = get_close_matches(word, data.keys())[0]
        print(f"Did you mean {match} instead")
        decide = input("Press 'y' for yes or 'n' for no:    ")
        if decide.lower() == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif decide.lower() == 'n':
            return("Word doesn't exist!")
        else:
            return("You have entered wrong input please enter just 'y' or 'n'")
    else:
        print("Word Doesn't exist!")


word = input("Enter the word you want to search:    ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
