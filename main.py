import random
from random_word import RandomWords
r = RandomWords()

list_of_Words = ["finger", "computer", "halloween", "avengers", "chocolate", "spiderman", "time",
"person",
"government",
"company",
"number",
"group",
"problem",
"avenue",
"awkward",
"beekeeper",
"duplex",
"equip",
"exodus",
"funny",
"galaxy",
"gossip",
"icebox",
"injury",
"ivory",
"jackpot",
"jelly",
"jockey",
"joking",
"joyful",
"jumbo",
"kayak",
"khaki",
"kiosk",
"lengths",
"lucky",
"luxury"]



num = random.randint(0, (len(list_of_Words)-1))


word = list_of_Words[num]

name = input("Enter Name: ")
print("Hello" + name)
print("What's your first guess?")
guesses = ""
turns = int(input("How many turns do you want? "))
while turns >0 :
    failed = 0
    for char in word: 
        if char in guesses:
            print(char)
        elif char == " ":
          print(" ")
        else:
            print("🚫")
            failed += 1
    if failed == 0:
        print("⚔️ You Won ⚔️")
        break
    print()
    guess = input("Guess the Letter, " + str(turns) + " guesses left: ")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("Wrong Guess")
        print("You have " + str(turns) + "turns")
    if turns == 0:
        print("You lose")
    