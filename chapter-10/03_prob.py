from random import randint

class train:

    def __init__(self, trainNo):
        self.trainNo = trainNo
        

    def book(self, fro, to):   
        print(f"ticket fare in train no: {self.trainNo} from {fro} to {to}")
    
    def getstatus(self):
         print(f" train no: {self.trainNo} is running on time")

    def getFare(self,fro,to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(100,500)}")

t = train(12345)    
t.book("delhi","mumbai")
t.getstatus()
t.getFare("delhi","mumbai")