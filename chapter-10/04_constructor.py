class employee:
    language = "Python" 
    salary = 10000

    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language
        print("i am creating an object")

    def getinfo(self):
      print(f"the language is {self.language}. the salary is {self.salary}")

    @staticmethod
    def greet():
            print("Good morning, sir")


het = employee("het patel", 100000, "python")
het.name = "het patel"
print(het.name, het.salary)
