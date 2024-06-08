def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_char_count(text)
    chars_dict_list = list_dict(chars_dict)
    chars_dict_list.sort(reverse=True, key=sort_on)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    for char_dict in chars_dict_list:
        char = char_dict["char"]
        num = char_dict["num"]
        print(f"The '{char}' character was found {num} times")
    print("--- End Report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    lowered_string = text.lower()
    counted = {}
    for i in lowered_string:
        counted[i] = counted.setdefault(i, 0) + 1
    return counted

def list_dict(dict):
    list = []
    for char, count in dict.items():
        if char.isalpha():
            new_dict = {"char": char,  "num": count}
            list.append(new_dict)
    return list

def sort_on(dict):
    return dict["num"]

main()        