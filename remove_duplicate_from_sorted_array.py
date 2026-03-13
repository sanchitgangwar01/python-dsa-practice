# nums = [1,1,4,4,5,5,3,3,6,4,3,2,5,6,]
# def remove_duplicate(nums):
#     n = len(nums)
#     dict = {}
#     for i in range(0,n):
#         dict[nums[i]]=0
#     j=0
#     for i in dict:
#         nums[j]=i
#         j+=1
#     return j
# print(remove_duplicate(nums))
# above solution have O(n) time complexity and O(n) space complexity
# optimal solution

nums = [1,1,2,3,3,3,4,4,4,4,5,5,5]
def remove_duplicate(nums):
    n=len(nums)
    if n==1:
        return 1
    i=0
    j=i+1
    while j<n:
        if nums[j]!=nums[i]:
            i+=1
            nums[i],nums[j]=nums[j],nums[i]
        j+=1
    return i+1

print(remove_duplicate(nums))