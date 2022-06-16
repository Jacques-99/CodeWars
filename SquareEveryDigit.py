def square_digits(num):
    l = []
    for i in str(num):
        l.append(str(int(i)**2))
        s = int("".join(l))
    return s

print(square_digits(1623))

