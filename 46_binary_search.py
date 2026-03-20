nums=[2,3,4,5,7,9]
tar=0
def binarySearch(nums,tar):
    n=len(nums)
    low=0
    high=n-1
    while low<high:
        mid=(low+high)//2
        if nums[mid]==tar:
            return tar
        elif tar<nums[mid]:
            high=mid-1
        else:
            low=mid+1
    return -1

print(binarySearch(nums,tar))
