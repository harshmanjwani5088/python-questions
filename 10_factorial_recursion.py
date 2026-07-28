def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fact(num-1)

num = int(input("enter the number"))

if num < 0:
    print("for negavtive values factorial does not exist")
else:
    print("factorial is" ,fact(num))