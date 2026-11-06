n = int(input("What is 2 + 2?:"))
answer = 4

while n != answer:
    if n > answer:
        print("Smaller!:")
    elif n < answer:
        print("Bigger!:")

    print("Try again!:")

print("You got it!")