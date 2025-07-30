class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    @classmethod
    def input(cls):
        name=str(input("Enter the name:"))
        marks=int(input("Enter the marks:"))
        return cls(name,marks)
    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Student Marks: {self.marks}")
s=student.input()
s.display()
        