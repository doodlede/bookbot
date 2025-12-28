def count_words(text: str):
    words = text.split()
    return len(words)

def get_char_number(text: str):
    counts = {}

    for char in text.lower():
        if char.isalpha():
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1

    return counts

def sort_on(items):
    return items["num"]

def sorted_char_number(char_dict: dict):
    char_list = []

    for item in char_dict:
        value = char_dict[item]
        char_list.append({"char" : item, "num" : value})

    char_list.sort(reverse=True, key= sort_on)
    return char_list
        
