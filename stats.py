def get_words (book_contents):
    # Provides word count of input file
    num_words = 0
    words = []

    words = book_contents.split()

    for word in words:
        num_words += 1
    
    return num_words

def get_characters (book_contents):

    characters = list(book_contents.lower())
    # Pulls characters out of words and into a list
    character_dictionary = {}
    # Creates dictionary

    for character in characters:
        if character not in character_dictionary:
            character_dictionary[character] = 1
        # Loops through characters and checks if in dictionary, if not, add it and assign count as 1
        else:
            character_dictionary[character] += 1
        # Loops through characters and adds 1 to the counter if it exists in the dictionary
    
    return character_dictionary


def sort_on(item):
    return item[1]  # this gets the count