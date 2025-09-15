"""
create two std objects with different details
call display() method for each object
"""
class Student:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks

    def display(self):
        print("Name of student = ",self.name," RollNo of student = ",self.roll," marks of studen = ",self.marks)

std=Student("aaaaa",65,89)
std.display()
std1=Student("bbbbb",21,90)
std1.display()