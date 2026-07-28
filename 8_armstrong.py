num = int(input("enter the number"))
temp = num
power = len(str(num))
result = 0

while temp > 0:
    digit = temp % 10
    result += digit**power
    temp = temp // 10

if num == result:
    print(f"armstrong {result}")
else:
    print(f"not amstrong {result}")