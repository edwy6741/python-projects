my_number = 23
guess = 0
attempts = 0

while guess != my_number:
    guess = int(input("Guess my number:"))
    attempts += 1
    if guess > my_number:
        print("Not right! Guess again.")        
        print("Attempts:", attempts)
        print("Too high!")
    if guess < my_number:
        print("Not right! Guess again.")        
        print("Attempts:", attempts)
        print("Too low!")
    if attempts == 5 and guess != my_number:
        print("Game over!")
        break
    if guess == 23:
        print("Attempts:", attempts)
        print("You got it!")
        break

#alternative solution
guess = 0
my_number = 67
attempt = 0
while guess != my_number:
    guess = int(input("Guess my number:"))
    attempt += 1
    print("Attempts:", attempt)
    if guess > my_number:
        print("Too high!")
        print("Guess again!")
    elif guess < my_number:
        print("Too low!")
        print("Guess again!")
    else:
        print("You got it")
        break
    if guess == 5:
        print("You couldn't guess my number :(.")
        print("Game over!")
        break

