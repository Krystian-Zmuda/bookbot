def get_book_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letter_count= {}
    words = text.split()
    for word in words:
        word = word.lower()
        letters = list(word)
        for letter in letters:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count

def get_num(dict):
    return dict["num"]
def get_char(dict):
    return dict["char"]

def sort_count(dictionary):
    list = []
    for key in dictionary:
        if key.isalpha():
            dict = {"char": key, "num": dictionary[key]}
            list.append(dict)
    list.sort(reverse=True, key=get_num)
    return list
