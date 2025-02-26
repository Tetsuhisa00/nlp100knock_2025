# 2025.2.26
text = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'

words = text.split()


one_word = [1, 5, 6, 7, 8, 9, 15, 16, 19]
dict = {}
for index, word in enumerate(words):
    if index in one_word:
        dict[index] = word[0]
    else:
        dict[index] = word[:2]
print(dict)