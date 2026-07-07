import random

# Special character library
SPECIAL_CHARACTERS = ["!", "@", "#", "$", "%", "&", "*", "~", "_", "-", "+", "="]

def generate_password(elements):
    # Randomly choose two different special characters
    special_chars = random.sample(SPECIAL_CHARACTERS, 2)

    # Randomize element order and randomly choose two different insertion positions
    random_elements = random.sample(elements, len(elements))
    positions = sorted(random.sample(range(len(random_elements)), 2))

    password = ""
    special_index = 0

    for i, element in enumerate(random_elements):
        password += element

        if i in positions:
            password += special_chars[special_index]
            special_index += 1

    return password
