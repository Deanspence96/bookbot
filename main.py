from stats import get_words
from stats import get_characters
from stats import sort_on
import sys

def get_book_text(file_path):
    with open(file_path) as f:
    # Open file path allias to "f"
        file_contents = f.read()
        # Read contents of file "f" and store in "file_contents"
    return file_contents


def main():
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = sys.argv[1]

    book_contents = get_book_text(file_path)
    # Pull data stored in function "get_book_text" and return it
    
    number_of_words = get_words (book_contents)
    #print(f"{number_of_words} words found in the document")
    # Pull number of words from file and print
    
    number_of_characters = get_characters(book_contents)
    #print(f"{number_of_characters} characters found in the document")
    # pull number of characters from file and print

    filtered_characters = {char: count for char, count in number_of_characters.items() if char.isalpha()}
    sorted_dictionary = sorted(filtered_characters.items(), key=sort_on, reverse=True)

    #print(number_of_words, number_of_characters)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")

    for char, count in sorted_dictionary:
        print(f"{char}: {count}")

    print("============= END ===============")
    
main()