def lang(num, text):
    french = 0
    english = 0
    # these variables only exist inside the function
    for letter in text:
        if letter == "s" or letter == "S":
                french = french + 1
        if letter == "t" or letter == "T":
            english += 1   
    if french >= english:
        print("french")
    else:
        print("english")
(lang(69, "Le chat dort sur le canapé près de la fenêtre."))