import random, easygui
secret = random.randint(1, 99)
guess = 0
tries = 0
easygui.msgbox("""AHOY! I am Judy, and I have a secret!
It is a number from 1 to 99. I'll give you 6 tries.""")
while guess != secret and tries < 6:
    guess = easygui.integerbox("What's your guess, matey?")
    if not guess: break
    if guess < secret:
        easygui.msgbox(str(guess) + " is too low, you stupid dog!")
    elif guess > secret:
        easygui.msgbox(str(guess) + " is too high, landlubber!")
    tries += 1
if guess == secret:
    easygui.msgbox("Avast! You got my secret! You did!")
else:
    easygui.msgbox("No more guesses! The secret is" + str(secret))
