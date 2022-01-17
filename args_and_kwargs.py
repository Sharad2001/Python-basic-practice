# Order is normal then *args and then **kwargs
def funargs(normal, *args, **kwargs):
    print(normal)
    for item in args:
        print(item)
    for key, value in kw.items():
        print(key, value)

har = ["Harry", "Rohan", "Skillf", "Hammad"]
normal = "I am a normal argument and the student are: "
kw = {"Sharad" : "Engineer", "Ram" : "Artist", "Deepak" :
      "Doctor"}
funargs(normal, *har, **kw)