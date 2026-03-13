# num=[5,9,1,2,4,15,6,3]
# sum=13
# def twosum(num):
#     n=len(num)
#     for i in range(0,n-1):
#         for j in range(i+1,n):
#             if num[i]+num[j]==sum:
#                 return i,j

# print(twosum(num))  


num =[5,9,1,2,4,15,6,3]
target=13
def twosum(nums):
    hash_map={}
    n=len(nums)
    for i in range(0,n):
        remaining=target-nums[i]
        if remaining in hash_map:
            return hash_map[remaining],i
        else:
            hash_map[nums[i]]=i
print(twosum(num))
# this is optimal solution time complexity is O(n) and space complexity is O(n)







