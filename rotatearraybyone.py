# num = [2,3,4,2,3,6,7,8,4]
# n= len(num)
# num[:]= [num[n-1]]+num[0:n-1]
# print(num)


# above is not optimal solution best solution can we if we dont use slicing in python

num = [2,3,4,3,2,3,4,6,7,76,5,4]

n=len(num)
temp = num[-1]
for i in range(n-2,-1,-1):
    num[i+1]=num[i]
num[0]=temp
print(num)