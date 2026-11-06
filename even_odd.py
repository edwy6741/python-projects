n = int(input("pick a number you chud:"))

count_3 = 0
count_5 = 0
count_both = 0
sum_neither = 0
largest_both = 0

for i in range (1, n + 1):
    if i % 3 == 0:
        count_3 += 1
    if i % 5 == 0:
        count_5 += 1
    if i % 3 == 0 and i % 5 == 0:
        count_both += 1
    if i % 3 == 0 and i % 5 == 0:
        largest_both = i 
    if i % 3 != 0 and i % 5 != 0:
        sum_neither += i

if largest_both == 0:
   largest_both = "There is no number."
print("The largest number divisible by both 3 and 5 that does not exceed your number:", largest_both)
print("Number of numbers that are divisible by both 3 and 5:", count_both)
print("Number of numbers that are divisible by 5:", count_5)
print("Number of numbers that are divisible by 3:", count_3)
print("Sum of all numbers that are divisible by neither 3 nor 5:", sum_neither)