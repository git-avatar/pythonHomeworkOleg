from collections import Counter

words_list = ["apple", "banana", "apple", "cherry", "banana", "banana", "apple", "date"]

word_frequency = {}
for word in words_list:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1


for word, frequency in word_frequency.items():
    print(f"{word}: {frequency}")
print("***********************************************************************")
from collections import Counter

result = Counter(word_frequency)
print(result)

