tempreatures =  [32.5, 31.0, 29.8, 28.4, 30.2, 33.1, ]

total = 0
for temp in tempreatures:
    total += temp
average = total / len(tempreatures)
print("Average temperature:", average)