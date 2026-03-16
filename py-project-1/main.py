computer = -1
you = input("enter you choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
youDict = {1: "s", -1: "w", 0: "g"}
you = youDict[you]

print(f"you choice {reverseDict[you]}\ncomputer choice {reverseDict[computer]}")

if(computer == you):
    print("draw")

else:
 if (computer ==-1 and you ==1):
    print("you win")

 elif (computer ==1 and you ==0):
      print("you lose")

 elif (computer ==1 and you ==-1):
    print("you lose")

 elif (computer ==1 and you ==0):
     print("you win")

 elif (computer  ==0 and you ==-1):
        print("you win")

 elif (computer ==0 and you ==1):
        print("you lose")

 else:
     print("something went wrong")        