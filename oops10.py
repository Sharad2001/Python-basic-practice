# Public
# Protected
# Private

class Employee:
    var = 8
    no_of_leaves = 8
    _protec = 9
    __private = 98

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

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def print_good(string):
        print("This is good" + string)

emp = Employee("Harry", 343, "Programmer")
print(emp._protec)
print(emp._Employee__private) # This is called as name mangelling