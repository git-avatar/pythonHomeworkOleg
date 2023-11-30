from collections import Counter
import os

def create_directory(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)

def read_file(file_path):
    with open(file_path, "r") as f:
        return f.read()

def count_word_occurrences(file_content, word, case_sensitive=True):
    if not case_sensitive:
        file_content = file_content.lower()
        word = word.lower()
    word_count = Counter(file_content.split())
    return word_count[word]

def word_counter():
    directory = "directory"
    create_directory(directory)

    file_path = os.path.join(directory, "test_file.txt")

    with open(file_path, "w") as f:
        f.write("File content: ")

    with open(file_path, "a") as f:
        f.write("TEST FILE")

    file_content = read_file(file_path)

    while True:
        question_type = input("Do you want to check for a specific word or a non-specific word?: ").lower()

        while question_type not in ["specific", "non-specific"]:
            print("You can only answer this question with specific or non-specific!")
            question_type = input("Do you want to check for a specific word or a non-specific word?: ").lower()

        case_sensitive = True
        if question_type == "non-specific":
            case_sensitive = False

        word_input = input("Enter the word you want to be counted: ")
        word_occurrences = count_word_occurrences(file_content, word_input, case_sensitive)
        print(f"{word_input} was found: {word_occurrences} times in the file")

        continue_check = input("Do you want to check for another word? (yes/no): ").lower()
        while continue_check not in ["yes", "no"]:
            print("You can only answer this question with yes or no")
            continue_check = input("Do you want to check for another word? (yes/no): ").lower()

        if continue_check == "no":
            break


word_counter()





