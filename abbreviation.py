def generate_platform_id(platform):
# This function is for get user input and perform simple processing

    # Ignore conjunctions
    stop_words = {"of", "and", "the", "for", "to"}

    words = platform.split()

    # Return when there is only 1 word (e.g. "Steam" is a simple remember word)
    if len(words) == 1:
        return platform

    abbreviation = ""
    for word in words:
        if word.lower() not in stop_words:
            abbreviation += word[0].upper()

    return abbreviation