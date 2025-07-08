# leetspeak.py

def leetspeak_variations(word):
    replacements = {
        'a': ['4', '@'],
        'e': ['3'],
        'i': ['1', '!'],
        'o': ['0'],
        's': ['$', '5'],
        't': ['7'],
    }

    variations = set()
    variations.add(word)

    for i in range(len(word)):
        char = word[i].lower()
        if char in replacements:
            for symbol in replacements[char]:
                new_word = word[:i] + symbol + word[i+1:]
                variations.add(new_word)

    return variations
