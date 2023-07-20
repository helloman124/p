def remove_duplicates_and_sort(words):
    word_list = words.split()
    unique_words = sorted(set(word_list))
    return unique_words
input_sequence = input("Enter a sequence of whitespace separated words: ")
result = remove_duplicates_and_sort(input_sequence)
print("Words after removing duplicates and sorting:",result)

