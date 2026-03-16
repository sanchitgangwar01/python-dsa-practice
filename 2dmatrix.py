nums=[[1,2,3],[4,5,6],[7,8,9],[10,11,12,],[13,14,15]]
# def twod_matrix(nums):
#     for i in range(0,len(nums)):
#         for j in range(0,len(nums[0])):
#             print(nums[i][j],end=" ")
#         print()
        
# twod_matrix(nums)

# Print upper triangle
# def printUpperTriangle(nums):
#     for i in range(0,len(nums)):
#         for j in range(0,len(nums[0])):
#             if j>=i:
#                 print(nums[i][j],end=" ")
# printUpperTriangle(nums)


# def printlowerTriangle(nums):
#     for i in range(0,len(nums)):
#         for j in range(0,len(nums[0])):
#             if i>=j:
#                 print(nums[i][j],end=" ")
# printlowerTriangle(nums)

# def diagonal(nums):
#     for i in range(0,len(nums)):
#         for j in range(0,len(nums[0])):
#             if i==j:
#                 print(nums[i][j],end=" ")
# diagonal(nums)

def downward_diagonal(nums):
    row=0
    col=len(nums[0])-1
    while row<len(nums):
        while col>=0:
            print(nums[row][col])
            col-=1
            row+=1
downward_diagonal(nums)

