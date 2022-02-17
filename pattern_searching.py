txt = input("Enter text: ")
patt = input("Enter pattern: ")
pos = txt.find(patt)

while pos>=0:
    print(pos)
    pos = txt.find(patt, pos+1)