import time

name = input("What is your name? ")

print("Welcome to my game, " + str(name))

playing = input("Are you sure you want to play? ")

if playing.lower() != "yes":
    print("thanks for trying... ")
    quit()

print("Game loading...")

score = 0

time.sleep(2)

answer = input("What is the capital of Calfornia? ")

if answer.lower() == "sacramento":
    print("Correct")
    score += 1
else:
    print("Incorrect")

abnswer = input("How many elements are in the periodic table of elements ")

if abnswer.lower() == "118":
    print("Correct")
    score += 1
else:
    print("Incorrect")


acnswer = input("What is the chemical formula for table salt? ")

if acnswer.lower() == "nacl":
    print("Correct")
    score += 1
else:
    print("Incorrect")


adnswer = input("What is the capital of India ")

if adnswer.lower() == "new delhi":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("You got " + str(score) + " questions right")

print(" You got " + str((score / 4) * 100) + "%")
