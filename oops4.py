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

harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")

harry.change_leaves(34)

print(harry.no_of_leaves)