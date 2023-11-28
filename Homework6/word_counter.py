from collections import Counter
import os

directory = "directory"

if not os.path.exists(directory):
    os.mkdir(directory)

file_path = os.path.join(directory, "test_file.txt")

with open(file_path, "w") as f:
    f.write("File content: ")

with open(file_path, "a") as f:
    f.write("TEST FILE")

question = input("Do you want to check for a word (capital or non-capital) or for a specific word (specific/non-specific)?: ").lower()

if question not in ['specific', 'non specific']:
    print("You can only answer this question with specific/non-specific!")
    question = input("Do you want to check for a word (capital or non-capital) or for a specific word (specific/non-specific)?: ").lower()

with open(file_path, "r") as f:
    file_content = f.read()

if question == "specific":
    specific_word = input("Enter the word you want to be counted: ")
    specific_word_count = Counter(file_content.split())
    print(f"{specific_word} was found: {specific_word_count[specific_word]} times in the file")

elif question == "non specific":
    non_specific_word = input("Enter the word you want to be counted: ").lower()
    non_specific_word_count = Counter(file_content.lower().split())
    print(f"{non_specific_word} was found: {non_specific_word_count[non_specific_word]} times in the file")






