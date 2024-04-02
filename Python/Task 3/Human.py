
from abc import ABC, abstractmethod

class Human(ABC) :
    def __init__ (self,name):
        self.name=name 
    @abstractmethod 
    def walk(self):
      pass
    @abstractmethod
    def eat(self):
       pass

class Employee(Human):
    def __init__(self,name,salary,emp_id):
        super().__init__(name)
        self.salary=salary
        self.emp_id=emp_id

    def eat(self):
        print(self.name,"is eating")
    def walk(self):
        print(self.name,"is walking")



emp1=Employee("gehad",1000,1)
print(emp1.name)
emp1.eat()
emp1.walk()
    