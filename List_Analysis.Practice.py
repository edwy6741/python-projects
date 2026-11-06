def count_even(a,b,c,d,e):
    count = 0
    for i in a,b,c,d,e:
        if i % 2 == 0:
            count += 1
    return count

def sum_even(a,b,c,d,e):
    count = 0
    for i in a,b,c,d,e:
        if i % 2 == 0:
            count += i
    return count

def count_divisiblebythree(a,b,c,d,e):
    count = 0
    for i in a,b,c,d,e:
        if i % 3 == 0:
            count += 1
    return count

print("Number of even numbers:", count_even(2,7,8,11,14))
print("Sum of all even numbers within the list:", sum_even(2,7,8,11,14))
print("Number of numbers divisible by 3 within the list:", count_divisiblebythree(2,7,8,11,14))