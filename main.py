import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import num_words, num_char, sorted_dict

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    book = get_book_text(sys.argv[1])
    word_count = num_words(book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    char_count = num_char(book)
    print("--------- Character Count -------")
    report = sorted_dict(char_count)
    for char_dict in report:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")        
    


main()