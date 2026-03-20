# nums=[2,3,4,5,7,9]
# tar=0
# def binarySearch(nums,tar):
#     n=len(nums)
#     low=0
#     high=n-1
#     while low<high:
#         mid=(low+high)//2
#         if nums[mid]==tar:
#             return tar
#         elif tar<nums[mid]:
#             high=mid-1
#         else:
#             low=mid+1
#     return -1

# print(binarySearch(nums,tar))


# Recursion Method 
nums= [2,3,4,5,7,9]
target=7
def binarySerch(nums,low,high):
    if low>high:
        return -1
    mid=(low+high)//2
    if nums[mid]==target:
        return mid
    elif nums[mid]<target:
        return binarySerch(nums,mid+1,high)
    else:
       return binarySerch(nums,low,mid-1)

print(binarySerch(nums,0,5))
