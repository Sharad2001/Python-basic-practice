# Method 1:
s = input("Enter text: ")
low = 0
high = len(s)-1
while low < high:
    if s[low] != s[high]:
        print("Sorry! Given text is not palindrome.")
        break
    low = low+1
    high = high-1
else:
    print("Yes the given text is palindrome.")

# Method 2:
# s = input("Enter the string: ")
# if s == s[::-1]:
#     print("Yes the given string is palindrome.")
# else:
#     print("Sorry!! Given string is not a palindrome.")