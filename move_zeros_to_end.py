# num = [1,2,3,0,0,0,4,0,5,6,0]
# def movezerotoend(num):
#     n=len(num)
#     temp = []
#     for i in range(0,n):
#         if num[i]!=0:
#             temp.append(num[i])
#     nm=len(temp)
#     for i in range(0,nm):
#         num[i]=temp[i]
#     for i in range(nm,n):
#         num[i]=0
# movezerotoend(num)
# print(num)
#more optimal solution
num = [1,2,3,0,0,0,4,0,5,6,0]
def movezerotoend(nums):
    if len(nums)==1:
        return
    i=0
    while i<len(nums):
        if nums[i]==0:
            break
        i+=1
    if i==len(nums):
        return
    j=i+1
    while j<len(nums):
        if num[j]!=0:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1    
        j+=1
        
movezerotoend(num)
print(num)