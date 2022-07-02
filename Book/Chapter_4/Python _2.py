def search4vowels(word):
    """Display any vowels found in a supplied word."""
    vowels = set('aeiouy')
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)



search4vowels('hello world namy')