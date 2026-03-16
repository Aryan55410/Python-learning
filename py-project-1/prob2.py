import random

# Mapping choices
youDict = {"s": 1, "w": -1, "g": 0}   # user input mapping
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}  # for display

# Computer random choice
computer = random.choice([-1, 0, 1])

# User choice
you_input = input("Enter your choice (s for Snake, w for Water, g for Gun): ")

if you_input not in youDict:
    print("❌ Invalid choice! Please enter s, w, or g.")
else:
    you = youDict[you_input]

    print(f"\nYou chose: {reverseDict[you]}")
    print(f"Computer chose: {reverseDict[computer]}\n")

    # Game logic
    if computer == you:
        print("🤝 It's a Draw!")
    elif (computer == -1 and you == 1) or (computer == 0 and you == -1) or (computer == 1 and you == 0):
        print("🎉 You Win!")
    else:
        print("😢 You Lose!")
