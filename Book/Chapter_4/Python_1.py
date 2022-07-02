def search4vowels():
    """Выводит гластныеб найденные во ведение слова"""
    vowels = set('aeiouy')
    word = input("Provide a word to search for vowels: ")
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)

search4vowels()