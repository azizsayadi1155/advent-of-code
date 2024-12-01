# initiate two arrays
arr1 = []
arr2 = []
# Reading input file
with open("input.txt", 'r') as f:
    for line in f:
        tmp = line.split()
        arr1.append(int(tmp[0]))
        arr2.append(int(tmp[1]))
print(len(arr1))
print(arr1)
print(len(arr2))
print(arr2)


arr1.sort()
arr2.sort()
print(arr1)
print(arr2)

# PART 1
result = 0
for i in range(len(arr1)):
    result += abs(arr1[i] - arr2[i])
print(result)

# PART 2
similarity = 0
dict = {}
for i in range(len(arr1)):
    dict[arr1[i]] = 0
print(dict)
for i in range(len(arr1)):
    dict[arr1[i]] = arr2.count(arr1[i])
    similarity += (arr1[i]*dict[arr1[i]])
print(dict)
print(similarity)