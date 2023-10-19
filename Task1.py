def most_wanted_letter(string):
    letters = {}
    string = string.lower()
    for i in string:
        if i.isalpha():
            letters.update({string.count(i): i})
    if letters: 
        res = "The most popular letter is " + (max(letters.items())[1])
    else:
        res = "There are no letters in the string. "
    return(res)

print(most_wanted_letter("......HeLlo......"))
print(most_wanted_letter("String ssss ttAAds TTTTTTT"))
print(most_wanted_letter("!@#$%^&*(*&^%$#@@#$%^&*DFGBQQQQQQQQqqqrrrrrrrr"))
print(most_wanted_letter("!@#$%^&*543234%^&*%$#@345677^%$#@#$%^&"))
print(most_wanted_letter("....пррррривет..."))
print(most_wanted_letter("....Tschüüüüüüüss!..."))
