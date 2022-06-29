
class Person:

    def __init__(self,nm,age):
        self.name = nm
        self.age = age
        

class Student(Person):

    def __init__(self,nm,age,roll,marks):
        super().__init__(nm,age)
        self.roll= roll
        self.marks = marks



s1 = Student('JAY',22,1,99)
print(s1.name)
print(s1.roll)
print(s1.age)
print(s1.marks)