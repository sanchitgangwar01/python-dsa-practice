# nums=[-2,1,-3,4,-1,2,1,-5,4]
# def maximum_subarray_sum(nums):
#     n=len(nums)
#     maxi =float("-inf")
#     for i in range(0,n):
#         total=0
#         for j in range(i,n):
#             total=total+nums[j]
#             maxi= max(maxi,total)
#     return maxi 

# print(maximum_subarray_sum(nums))
# above solution is not optimal best solution can be kadan algo below is the good solution

nums =[-2,1,-3,4,-1,2,1,-5,4]
n=len(nums)

def maximum_subarray_sum(nums):
    maxi=float("-inf")
    total=0
    for i in range(0,n):
        total= total+nums[i]
        maxi = max(maxi,total)
        if total<0:
            total=0
    return maxi

print(maximum_subarray_sum(nums))

