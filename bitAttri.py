class abc():
    def __init__(self,var1,var2):
        self.var1=var1
        self.var2=var2
    def display(self):
        print("Var1:",self.var1)
        print("Var2:",self.var2)
n1=int(input("Enter the n1:"))
n2=float(input("Enter the n2:"))
o=abc(n1,n2)
print("object.__dict__-",o.__dict__)
print("object.__doc__-",o.__doc__)
print("Class.__name__-",abc.__name__)
print("object.__module__-",o.__module__)
print("Class.__base__-",abc.__base__)
