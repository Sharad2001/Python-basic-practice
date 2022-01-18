class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithharry.com"

    def expalin(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.lname == None or self.lname == None:
            return "Email is not set. Please set it using setter."
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter
    def email(self, string):
        print("Setting Now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

skillf = Employee("skill", "f")
# print(dir(skillf))

o = "This is a string"
# print(dir(o))

import inspect
print(inspect.getmembers(skillf))