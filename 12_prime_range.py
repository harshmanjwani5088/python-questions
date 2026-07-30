start = int(input("enter the start number: "))
end = int(input("enter the start number: "))
lst = []
for i in range(start,end+1):
    if i < 2:
        continue
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        lst.append(i)
print(lst)
