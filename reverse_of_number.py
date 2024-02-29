def reversed_number(num):
    reversed_num = 0
    while num !=0:
        print(num)
        digit = num%10 ##num = 123
        reversed_num = reversed_num*10+digit #123 
        num = num //10 #num = 123 = 12.3 = 12
    return reversed_num

original_number = 12345
reverse_result = reversed_number(original_number)
print("The reversed number is: ", reverse_result)


