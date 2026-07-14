import random

def generate_platform_id(platform):
    # Random mode 1 = UPPER, 2 = lower, 3 = Original
    mode = random.randint(1, 3)

    # Ignore conjunctions
    stop_words = {"of", "and", "the", "for", "to"}
    words = platform.split()

    # Process with 1 word
    if len(words) == 1:
        if mode == 1:
            return platform.upper()
        elif mode == 2:
            return platform.lower()
        else:
            return platform

    # Process with not 1 word
    abbreviation = ""
    for word in words:
        if word.lower() not in stop_words:
            abbreviation += word[0].upper()
    if random.randint(1, 2) == 1:
        return abbreviation.upper()
    else:
        return abbreviation.lower()