from stats import *
import sys

def main():
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = args[1]
    file_contents = get_book_text(path)
    
    words_count_msg = f"Found {count_words(file_contents)} total words"
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(words_count_msg)
    print("--------- Character Count -------")
    sorted_count = sort_count(count_letters(file_contents))
    for char_and_num in sorted_count:
        print(f"{get_char(char_and_num)}: {get_num(char_and_num)}")
    print("============= END ===============")


main()