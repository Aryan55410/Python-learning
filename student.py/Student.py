import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Students.csv")

print(df.head())

# average score add kar
df["average"] = (df["math score"] + df["reading score"] + df["writing score"])


#grade system add kar
def grade(avg):
    if avg>= 270:
        return "A"
    elif avg >= 240:
        return "B"
    elif avg >= 210:
        return "C"
    elif avg >= 180:
        return "D"
    else:
        return "F"
df["grade"] = df["average"].apply(grade)

print(df.head())

#topper student find
topper = df.sort_values(by="average", ascending=False)

print("Topper student:")
print(topper.head(1))

#gender wise average score
gender_avg = df.groupby("gender")["average"].mean()
print(gender_avg)




df[["math score", "reading score", "writing score"]].mean().plot(kind="bar")
plt.title("Average Score By Subject")
plt.show()

#result save kar
df.to_csv("Students_with_grades.csv", index=False)