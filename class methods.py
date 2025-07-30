'''basic math operation using @classmethod'''

class calculator:
    def __init__(s,a,b):
        s.a = a
        s.b = b
    @classmethod
    def input(cls):
        a=int(input("Enter the value of a:"))
        b=int(input("Enter the value of b:"))
        return cls(a,b)
    def op(s):
        print("1.Addition:",s.a+s.b)
        print("2.Substration:",s.a-s.b)
        print("3.Product:",s.a*s.b)
            
c=calculator.input()
c.op()
