from collections import defaultdict

def count_character_frequencies(input_string):
    char_count = defaultdict(int)
    for char in input_string:
        char_count[char] += 1
    return dict(char_count)
