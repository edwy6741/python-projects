numbers = [2,7,8,11,14,16,19]

def count_even(numbers):
    count = 0
    for i in numbers:
        if i % 2 == 0:
            count += 1
    return count

print(count_even(numbers))