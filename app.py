a = int(input("Enter the measurement for a: "))
b = int(input("Enter the measurement for b: "))
c = int(input("Enter the measurement for c: "))

if (a + b)> c and (a + c)> b and (b + c)> a:
    print ("Valid")
else: 
    print ("Invalid")
