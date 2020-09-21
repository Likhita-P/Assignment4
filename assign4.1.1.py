class parent:
    def __init__(self):
        pass
    def inputsides(self):

        self.a=int(input("Enter side 1:"))
        self.b=int(input("Enter side 2:"))
        self.c=int(input("Enter side 3:"))

class child:
    def __init__(self):
        pass
    def calculatearea(self,ob1):
        self.s=(ob1.a+ob1.b+ob1.c)//2
        area = (self.s * (self.s - ob1.a) * (self.s - ob1.b) * (self.s - ob1.c)) ** 0.5
        print("Area:",area)

ob1=parent()
ob1.inputsides()
ob2=child()
ob2.calculatearea(ob1)