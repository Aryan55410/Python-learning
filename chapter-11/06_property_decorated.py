class employee:
    a = 1

    @classmethod
    def show (cls):
        print(f"the class attributes  of  a is : {cls.a}")
    
    @property 
    def name(self):
        return self.ename
    
    @name.setter
    def name(self, value):
        self.ename = value
e = employee()        
e.a = 45

e.name = "aryan"
print(e.name)

e.show()