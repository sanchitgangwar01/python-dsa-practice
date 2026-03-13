original = 153
n = original
new = 0
ld = len(str(original))
while n>0:
    temp = n%10
    new =new + (temp**ld)
    n=n//10
print(new)
