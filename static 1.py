class student:
    gender='male'
    def __init__(self,name):
        self.name=name
    def display(s):
        print(f"name:{s.name}")
    @classmethod
    def get_name(cls):
        return cls.gender
    @staticmethod
    def resident(type_of_resident):
        if type_of_resident.lower()=='indian':
            return "the person is an indian"
        else:
            return "the person is not an indian resident"
name=str(input("eter your name:"))
type=input("ENTER RESIDENCE OR NON-RESIDENE:")
s=student(name)
s.display()
print("student gender:",student.get_name())
print(s.resident(type))