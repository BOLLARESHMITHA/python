class Emp:
    a=[]
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Emp.a.append(self.name)
    def display(self):
        print("employee details")
        print("Name of emp : ",self.name,"\nSalary for emp = ",self.salary)

class Manager(Emp):
    def __init__(self,name,salary,dep):
        super().__init__(name,salary)
        self.dep=dep

    def display(self):
        super().display()
        print(len(Emp.a))
        print("dep of emp :",self.dep)

class staff(Emp):
    def __init__(self,name,salary,dep):
        super().__init__(name,salary)
        self.dep=dep

    def display(self):
        super().display()
        print(len(Emp.a))
        print("dep of emp :",self.dep)

class boss(Emp):
    print(Manager.dep)
    print(staff.dep)

m=Manager("aaaaa",50000,"sales")
n=m.name
m.display()