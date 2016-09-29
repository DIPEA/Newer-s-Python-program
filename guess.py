import random
secret = random.randint(1,99)
guess = 0
tries = 0
print("game start")
while guess != secret and tries < 6:
    guess = input("what is your guess?")
    if int(guess) < secret:
        print("too low")
    elif int(guess) > secret:
        print("too high")

    tries = tries + 1

if int(guess) == secret:
    print("congratulations!")
    input()
else:
    print("you lose, game over.")
    print("the secret number was:", secret)
    input()
