import random

def enhance_length(elements, min_length=12):
# Add one dictionary word if the original password elements are too short.

    dictionary_by_length = {
        2: ["in", "AT", "On", "Is"],
        3: ["key", "WIN", "key", "pro"],
        4: ["HAVE", "plan", "Pass", "Plus"],
        5: ["Doing", "using", "about", "EVERY"],
        6: ["WorkIn", "stayIn", "health", "INSIDE"],
        7: ["working", "StudyIn", "PassKey", "SUPPORT"]
    }

    current_length = len("".join(elements))

    # If original password already reaches minimum length, return directly.
    if current_length >= min_length:
        return elements

    need_length = min_length - current_length

    # If password is too short and needs more than 7 characters,
    # use a 7-character dictionary word.
    if need_length > 7:
        need_length = 7

    # Select dictionary words with lengths between
    # need_length and need_length + 2
    valid_words = []

    upper_length = min(need_length + 2, 7)

    for length in range(need_length, upper_length + 1):
        if length in dictionary_by_length:
            valid_words.extend(dictionary_by_length[length])

    # Randomly select one dictionary word
    if valid_words:
        selected_word = random.choice(valid_words)
        elements.append(selected_word)

    return elements
