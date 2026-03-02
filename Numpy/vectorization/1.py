list1 = [1,2,3]
list2 = [4,5,6]

result = [a + b for a, b in zip(list1, list2)]
print(result)