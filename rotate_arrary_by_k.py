num=[1,2,3]
n=len(num)
k=12
for j in range(0,k):
    temp =num[n-1]
    for i in range(n-2,-1,-1):
        num[i+1]=num[i]
    num[0]=temp
print(num)