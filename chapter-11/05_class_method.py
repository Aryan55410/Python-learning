class employee:
    a = 1
    @classmethod
    def show (cls):
        print(f"the class value of is : {cls.a}")

e = employee()        
e.a = 45

e.show()