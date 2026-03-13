num = 20
n=20
list = []
while n>0:
    print("loop running")
    if num%n==0:
        list.append(n)
    n=n-1
print(list)