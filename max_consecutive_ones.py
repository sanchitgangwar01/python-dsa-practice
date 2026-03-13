# nums= [1,1,0,1,0,1,1,1,1,0,1,1]
# def max_consecutive_ones(nums):
#     ones=[]
#     n=len(nums)
#     temp=0
#     for i in range(0,n):
#         if nums[i]==1:
#             temp+=1    
#         elif nums[i]==0:
#              ones.append(temp)
#              temp=0
#         ones.append(temp)
#     return max(ones)

# print(max_consecutive_ones(nums))   


#best optmial solution
nums =  [1,1,0,1,0,1,1,1,1,0,1,1,1,1,1]
def max_consecutive_ones(nums):
    count=0
    max_count=0
    for i in range(0,len(nums)):
        if nums[i]==1:
            count+=1
        else:
            max_count = max(count,max_count)
            count=0
    return max(max_count,count)
    
max_consecutive_ones(nums)