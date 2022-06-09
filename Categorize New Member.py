def open_or_senior(data):
    category = []
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            category.append("Senior")
        else:
            category.append("Open")
    return category


input = [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
print(open_or_senior(input))

category = []
for i in input:
    if i[0] >= 55 and i[1] > 7:
        category.append("Senior")
    else:
        category.append("Open")

print(category)