#i = 0

#while (True):
#    print(i+1, end=' ')
#    if i == 44:
#        break # Stop the loop
#    i = i+1

# Quiz


while True:
    n = int(input("Enter a number: "))
    if n >= 100:
        print("Congrats! u have reached a "
              "number greater than 100.")
        break
    else:
        print("Try again")
        continue