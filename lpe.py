def count_strings(strings):
    count = 0
    for s in strings:
        if len(s) >= 2 and s[0] == s[-1]:
            count += 1
    return count
strings_list = ["hello", "world", "level", "abca", "a", "aa"]
result = count_strings(strings_list)
print("Number of strings with the same first and last characters:", result)
