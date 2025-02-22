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