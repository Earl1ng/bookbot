def num_words(book):
    words = book.split()
    counter = len(words)
    return counter

def num_char(book):
    char_counts = {}
    for char in book.lower():
        if char in char_counts:
            char_counts[char] += 1 
        else:
            char_counts[char] = 1
    return char_counts

def sorted_dict(char_count):
    def sort_by_count(dict):
        return dict["count"]

    dictionaries = []
    for char, count in char_count.items():
        dictionaries.append({"char": char, "count": count})
    dictionaries.sort(reverse=True, key=sort_by_count)
    return dictionaries


    