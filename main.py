import sys
from stats import get_num_words, get_count_characters, sort_characters

def get_book_text(filepath):
    with open(filepath, "r") as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]


    book_text = get_book_text(filepath)
    num_words = get_num_words(book_text)
    character_counts = get_count_characters(book_text)
    sorted_characters = sort_characters(character_counts)

    print("============ BOOKBOT =============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count -----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count --------")
    for item in sorted_characters:
        print(f"{item['char']}: {item['num']}")
    print("============= END ================")

main()