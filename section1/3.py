# 2025.4.24
# output the number of strings in each words
str = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
print(str.split())


# # 2025.2.26
""""
str = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
print(str.split())
"""

# 2025.2.22
"""""
str = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

strs = []

total = 0
for word in str:
    if word == ' ':
        strs.append(total)
        total = 0
    else:
        total += 1
strs.append(total)

print(strs)
"""""
# 正規表現で書き直す