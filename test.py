#Script that acts as an interactive dictionary


import json
from difflib import get_close_matches #Import used to judge word similarity

json_file= json.load(open('data.json'))

def translate(w):
    w= w.lower()
    if w in json_file:
        return json_file[w]
    elif w.title() in json_file: #Finding words startin with capital letters eg: Delhi i.e from lower to uppercase
        return json_file[w.title()]
    elif w.upper() in json_file: #in case user enters words like USA or NATO convert all to uppercase 
         return json_file[w.upper()]
    elif len(get_close_matches(w,json_file.keys())) > 0 :
        option=input('Did you mean {0} instead of {1}?Please enter Y for yes or N for no '.format(get_close_matches(w,json_file.keys())[0], w))
        if option =="Y" or option =="y" :
            return json_file[get_close_matches(w,json_file.keys())[0]]
        elif option == "N" or option =="n":
            return "Word does not exist. Please try again."
        else:
            return "Please try again"

    else:
        return 'Word does not exist'

word = input("Enter Word ! : ")
result = translate(word)

if type(result)==list:
    for i in result:
        print(i)
else:
    print(result)


