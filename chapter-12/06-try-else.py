try:
    a = int(input("Enter a number: "))
    print(a)


except Exception as e:
    print(e)

else:
    print("No exceptions were raised.")