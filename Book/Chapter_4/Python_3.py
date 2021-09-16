def search4vowels(pharse:str) -> set:
    """Возращает гласные, найденые в указоной фразе."""
    vowels = set('aeiou')
    found = vowels.intersection(set(pharse))
    return found

def search4letters(phrase:str, letters:str) -> set:
    return set(letters).intersection(set(phrase))


print(search4vowels('heloo world, my name roma'))