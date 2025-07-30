'''code to view the memory info in a class , which  given the type of the class , size of the class,
and size of the instance
constant: use of package _ sys for the size of
given value of num=10
#code for given program
import sys
class MemoryInfo:
    def __init__(self, cls_type, num=10):
        self.cls_type = cls_type
        self.num = num
        self.class_size = sys.getsizeof(cls_type)
        self.instance_size = sys.getsizeof(cls_type())
    
    def display_info(self):
        print(f"Class type: {self.cls_type}")
        print(f"Size of class object: {self.class_size} bytes")
        print(f"Size of class instance: {self.instance_size} bytes")
        print(f"Given constant num: {self.num}")

class MyClass:
    def __init__(self):
        self.a = 1
        self.b = 2

info = MemoryInfo(MyClass)
info.display_info()
'''
import sys
class A:
    n=int(input("Enter the number:"))
a=A()
print(type(A))
print(sys.getsizeof(A))
print(sys.getsizeof(a))