str = input("Enter a string: ") 
str = str.lower() 
rev = str[::-1]

if str == rev:
    print("It is a palindrome")
else:
    print("Not a Palindrome")