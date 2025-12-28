from stats import count_words, get_char_number, sorted_char_number
import sys

def get_book_text(f_path):
    with open(f_path) as f:
        text = f.read()
        return text
    
    
def main():
    # path = "./books/frankenstein.txt"
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(f_path=sys.argv[1])
    char_dict = get_char_number(text)
    char_list = sorted_char_number(char_dict)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    print("--------- Character Count -------")
    for i in char_list:
        print(f"{i['char']}: {i['num']}")
    print("============= END ===============")

main()

