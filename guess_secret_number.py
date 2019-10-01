secret = 13
guess = int(input("Guess the number (between 0 and 25): "))
if guess == secret:
    print("Congratulations, you got the right number!")
elif guess == 12:
    print("Sooo close... but still wrong.")
elif guess == 14:
    print("Sooo close... but still wrong.")
else:
    print("Oh no, that's not the right number. Sorry!")
