class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and " \
               f"role is {self.role}"

    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary
    def __floordiv__(self, other):
        return self.salary // other.salary
    def __repr__(self):
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"
    def __str__(self):
        return f"The name is {self.name}. Salary is " \
               f"{self.salary} and role is {self.role}."
emp1 = Employee("Harry", 345, "Programmer")
# emp2 = Employee("Harry", 85, "Cleaner")
#
# print(emp1 + emp2)
# print(emp1/emp2)
# print(emp1 // emp2)
print(str(emp1))
print(repr(emp1))