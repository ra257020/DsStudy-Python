# Selection Sort

list = [2,5,4,1,3,6,9,7,8,10]
for i in range(0, len(list)):
    current = i
    for j in range(i, len(list)):
        if list[current] > list[j]:
            current = j
    temp = list[current]
    list[current] = list[i]
    list[i] = temp

print(list)
