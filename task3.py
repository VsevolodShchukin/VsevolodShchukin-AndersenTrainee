
array = list(input())
l = []

for element in array:
    if int(element) % 3 == 0:
        l.append(element)

print(l)