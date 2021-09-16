vowels = ['a', 'e', 'i', 'o', 'u', 'y']
word = input("Provide a word to search for vowels: ")
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
if found == []:
    print("There is no vowels")
for vowel in found:
    print(vowel)