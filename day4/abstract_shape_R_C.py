"""
Create an abstract class Shape that defines:
 
An abstract method area() (no implementation).
Create two child classes that inherit from Shape:
Rectangle → has attributes length, breadth, and implements area().
Circle → has attribute radius, and implements area().
Task:
Define the abstract class Shape using the abc module.
Implement Rectangle and Circle classes by providing their own version of area().
Create one object of Rectangle and one of Circle, then display their areas.
 
from abc import ABC, abstractmethod
 
# Abstract class
class Shape(ABC):
 
    @abstractmethod           # Abstract method
    def area(self):
        pass   
"""
from abc import ABC , abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,raduis):
        self.raduis=raduis

    def area(self):
        print("Area of circle with raduis ",self.raduis," is = ",end="")
        return 3.14*(self.raduis)*(self.raduis)

class Rectangle(Shape):
    def __init__(self,length,breath):
        self.length=length
        self.breath=breath

    def area(self):
        print("Area of resctangle with length ",self.length," and breath ",self.breath," is = ",end="")
        return (self.length)*(self.breath)

c=Circle(10)
print(c.area())

r=Rectangle(20,20)
print(r.area())