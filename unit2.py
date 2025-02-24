# Unit 2

"""x = 3
y = float(3)
print(x,y)

def tipCalculator():
    bill = float(input("How much was the bill?"))
    tip = int(input("How much was the tip?"))
    totalAmtPaid = bill * (tip / 100) + bill 
    print(f"You spent a total of {totalAmtPaid}")
tipCalculator

values = [1,2,3,4,5,6,7,8,9,10]
print(values)
for i in values:
    print(i)

print(values[0])
print(values[5])

"test"
["t","e","s","t"]

x = "this is a thing"
y = x.split()
z = y[0]
print(y)
print(z)

# Challenge #1
sentence_input = input("Give me a sentence, please. ") # Asks for a sentence

# Function to count words
def count_words(sentence):
    words = sentence.split() # Split the sentence into words
    return len(words)       # Count the words

# Get word count and print
word_count = count_words(sentence_input) #Call the function with the user's sentence
print(f"This sentence contains {word_count} words. ") # Print result

# Mad Libs Project
noun = input("Give me a noun.")
verb = input("Give me a verb.")
verb_2 = input("Give me a second verb.")
number = input("Give me a number.")
guest = input("Give me a celebrity guest.")

print(f"{guest} was at the {noun} shop, {verb} around. Paparazi {verb_2} them around. In just {number} licks of their {noun}, the paparazi had already found them!")

day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect")

number = int(input("Give me a number, please. "))
if number % 2 == 1:
    print('Odd')
elif number % 2 == 0:
    print('Even')

service  = input("How was the service? ")
if service == 'bad':
    print('0% tip')
elif service == 'okay':
    print('15%')
elif service == 'good':
    print('20%')
elif service == 'great':
    print('25%')"""

integer = int(input("Give me an integer. "))
def factor():
    factors = []
    for i in range(1, integer+1):
        if integer % i == 0:
            factors.append(i)
    print(factors)
(factor())