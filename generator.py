# generator.py

from leetspeak import leetspeak_variations

def generate_passwords(base_words):
    wordlist = set()

    years = [str(y) for y in range(1980, 2025)]
    numbers = [str(n).zfill(3) for n in range(1, 301)]  # '001' to '300'
    symbols = ['!', '@', '#', '$', '?', '*', '&', '%', '+', '=', '-', '_']

    for word in base_words:
        word = word.strip()
        if not word:
            continue

        variants = leetspeak_variations(word)
        for variant in variants:
            wordlist.add(variant)

            for num in numbers:
                wordlist.add(variant + num)
                wordlist.add(num + variant)

            for year in years:
                wordlist.add(variant + year)
                wordlist.add(year + variant)

            for symbol in symbols:
                wordlist.add(variant + symbol)
                wordlist.add(symbol + variant)

            for num in numbers:
                for symbol in symbols:
                    wordlist.add(variant + num + symbol)
                    wordlist.add(symbol + num + variant)

            for year in years:
                for symbol in symbols:
                    wordlist.add(variant + year + symbol)
                    wordlist.add(symbol + year + variant)

            for num in numbers:
                for year in years:
                    wordlist.add(variant + num + year)
                    wordlist.add(year + num + variant)

    return sorted(wordlist)
