class employee:
    language = "Python" 
    salary = 10000


    def getinfo(self):
      print(f"the language is {self.language}. the salary is {self.salary}")


het = employee()
het.language = "javascript"
# het.getinfo()
employee.getinfo(het)




# here name is instance attribute and salary and language are class attribute as they directly belong to the class
  