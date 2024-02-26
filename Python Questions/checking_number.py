# num = float(input("Enter a Number: "))
# if num>0:
#     print("Number is positive")
# elif num==0:
#     print("Number is zero")
# else:
#     print("Number is negative")

'''2nd method using function'''

def check_num(num):
    if num>0:
        return "Positive Number"
    elif num<0:
        return "Negative Number"
    else:
        return "Zero"

num = float(input("Enter a Number: "))
result = check_num(num)
print("The number is: ", result)

# num = -7
# result = check_num(num)
# print("The number is: ", result)