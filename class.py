class Employee:
    # class attributes
    company_name="Infosys!"
    # constructor
    def __init__(self,name,age,salary):
        # Instance attributes
        self.name=name
        self.age=age
        self.salary=salary

     # class methods
    def method1(self):
        return (f"Hii, {self.name} !!")

    def method2(self):
        return (f"Hii, {self.name} !!")
# create object
employee1=Employee("Vikas",24,50000) # object1
employee2=Employee("Ganesh",30,45000) # object2
print(employee1.method1(),employee2.method2())
print(f"Company name:-{Employee.company_name} name:-{employee1.name} age:-{employee1.age} salary:- {employee1.salary}")
print(f"Company name:-{Employee.company_name} name:-{employee2.name} age:-{employee2.age} salary:- {employee2.salary}")



