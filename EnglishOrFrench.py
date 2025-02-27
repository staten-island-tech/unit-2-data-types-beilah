some_text = "The red cat sat on the mat. Why are you so sad cat? Don't ask that."

def lang(text):
    french = 0
    english = 0
    # these variables only exist inside the function
    for letter in some_text:
        if letter in some_text:
            if letter == "s" or letter == "S":
            # if letter == "s" or letter == "S"
            # if letter in ["s" "S"]
                french = french + 1
        elif letter == "t" or letter == "T":
            english += 1
        if french >= english:
            print('french')
        else:
            print('english')
(lang("The red cat sat on the mat. Why are you so sad cat? Don't ask that."))