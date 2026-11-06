def count_vowels(text):
    count = 0
    for i in text:
        if i.lower() in "aeiou":
            count += 1
    return count

def count_consonants(text):
    count = 0
    for i in text:
        if i.lower() in "bcdfghjklmnpqrstuvwxyz":
            count += 1
    return count
n = input("Give me a word:")

print("Number of vowels:", count_vowels(n))
print("Number of consonants:", count_consonants(n))
