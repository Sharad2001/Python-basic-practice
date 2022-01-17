class Emlpoyee:
    no_of_leaves = 8
    pass

harry = Emlpoyee()
rohan = Emlpoyee()

harry.name = "Harry"
harry.salary = 455
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 4554
rohan.role = "Student"

print(Emlpoyee.no_of_leaves)
print(Emlpoyee.__dict__)
Emlpoyee.no_of_leaves = 9
print(Emlpoyee.__dict__)
print(Emlpoyee.no_of_leaves)