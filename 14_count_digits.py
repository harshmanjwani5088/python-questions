digit = int(input("enter the digit "))
count = 0
while digit > 0:
    count += 1
    digit //= 10 
print(count)