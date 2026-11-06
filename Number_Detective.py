n = int(input("Give me a number to inspect:"))
even = 0
odd = 0
count_3_no5 = 0
count_3_even = 0
large_odd_7 = 0

for i in range (1, n+1):
    if i % 2 == 0:
        even += 1
    if i % 2 != 0:
        odd +=1
    if i % 3 == 0 and i % 5 != 0:
        count_3_no5 +=1
    if i % 2 == 0 and i % 3 == 0:
        count_3_even += i
    if i % 2 != 0 and i % 7 == 0:
        large_odd_7 = i

print("Even numbers:", even)
print("Odd numbers:", odd)
print("Divisible by 3 but not 5:", count_3_no5)
print("Sum of numbers that are even and divisible by 3:", count_3_even)
print("Largest number that is odd and divisible by 7:", large_odd_7)
