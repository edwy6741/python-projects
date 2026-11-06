number = [2, 7, 8, 11, 14]

def analyze_numbers(number):
    count_even = 0
    count_sum = 0
    for i in number:
        if i % 2 == 0:
            count_even += 1
    for i in number:
        if i % 2 == 0:
            count_sum += i
    return count_even, count_sum 

result = analyze_numbers(number)

print("(a, b) where a is the number of even numbers and b is the sum of even number", result)

number2 = [-8, -3, -12, -5]

def analyze_numbers2(number2):
    count_even = 0
    count_3 = 0
    largest = number2[0]
    for i in number2:
        if i % 2 == 0:
            count_even += 1
        if i % 3 == 0:
            count_3 += i
        if i > largest:
            largest = i
    return count_even, count_3, largest

result2 = analyze_numbers2(number2)
print("(a, b, c) where a is the number of even numbers, b is the sum of the numbers divisible by 3, and c is the largest number within the list", result2)

number3 = [8, 3, 12, 5, 7]

def sorting(number3):
    largest = number3[0]
    second_largest_number = None
    for i in number3:
        if i > largest:
            second_largest_number = largest
            largest = i
        elif i < largest:
            if second_largest_number is None or second_largest_number < i:
                second_largest_number = i
    return largest, second_largest_number

result3 = sorting(number3)
print(result3)

# This solution accounts for duplicates and doesn't put the second largest as the largest if they're duplicates in the list
number4 = [9, 9, 6, 4]

def sort(number4):
    largest = number4[0]
    second_largest = None
    for i in number4:
        if i > largest:
            second_largest = largest
            largest = i
        elif i != largest and (second_largest is None or i > second_largest):
            second_largest = i
    return second_largest

return4 = sort(number4)

print(return4)

number5 = [5, 4, 3]

def third_largest(number5):
    largest = number5[0]
    second = None
    third = None
    for i in number5:
        if i > largest:
            third = second
            second = largest
            largest = i
        elif i < largest and (second is None or i > second):
            third = second
            second = i
        elif second is not None and i < second and (third is None or i > third):
            third = i
    return third

return5 = third_largest(number5)
print(return5)

number_final = [8, 3, 12, 5, 7, 10]

def final_list(number_final):
    total = 0
    numbers = 0
    smallest = number_final[0]
    sum_even = 0
    divide_3 = 0
    largest = number_final[0]
    second = None
    third = None
    for i in number_final:
        total += i
        numbers += 1
        if i < smallest:
            smallest = i
        if i % 2 == 0:
            sum_even += i
        if i % 3 == 0:
            divide_3 += 1
        if i > largest:
            third = second
            second = largest
            largest = i
        elif i < largest and (second is None or i > second):
            third = second
            second = i
        elif second is not None and i < second and (third is None or i > third):
            third = i
    average = total/numbers
    return average, largest, smallest, sum_even, divide_3, third

return_final = final_list(number_final)
print(return_final)