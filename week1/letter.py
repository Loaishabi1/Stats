import random
letters = "abcdefghijklmnopqrstuvwxyz"
input_letter = random.choice(letters)

# don't edit the code above
# put your code below here:

enter=input('would you like to random a letter')
if enter.lower() == "no":
    print("Game ended.")
    exit()
if enter=='yes':
       print(input_letter)
if input_letter in ['a', 'e', 'i', 'o', 'u']:
    output = "vowel"
elif input_letter == 'y':
    output = "it depends"
else:
    output = "consonant"

print(output)


