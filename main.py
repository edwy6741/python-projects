n = int(input("give me a number, any number:"))
largest = 0
even = 0
for i in range (1, n+1):
    if i % 7 == 0:
        largest = i
    if i % 3 == 0 and i % 5 == 0:
        print("numbers divisible by both 3 and 5:", i)

print("largest multiple of 7:", largest)
 
print("sum from 1 to", n,":", sum(range(1, n+1)) )

for i in range (1, n+1):
    if i % 2 == 0:
        even += 1

print("number of even numbers:", even)