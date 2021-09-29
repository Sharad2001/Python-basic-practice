def add_object(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        return "Input is not an integer!"
    return a + b

print(add_object(6, 6))