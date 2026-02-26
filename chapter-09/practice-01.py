import random
def game():
    print("Welcome to the Number Guessing Game!")
    score = random.randint(1, 100)
    with open("high_score.txt") as file:
      high_score = file.read()
      if(high_score!=""):
        high_score = int(high_score)
      else:
        high_score = 0  

    print(f"your score: {score}")
    if(score>high_score):
       
       with open("high_score.txt","w") as file:
          file.write(str(score))
       return score

game()