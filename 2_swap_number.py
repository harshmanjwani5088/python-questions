def swap_without_third(a,b):
    a,b=b,a
    print(a,b)
def swap_with_third(a,b):
    temp = a
    a = b
    b = temp
    print(a,b)
def swap_with_formula(a,b):
    a = a + b  
    b = a - b  
    a = a - b 
    print(a,b)

a, b = 5, 10
swap_without_third(a,b);
swap_with_third(a,b);
swap_with_formula(a,b);

