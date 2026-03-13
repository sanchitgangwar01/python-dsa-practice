# num = [1,0,3,4]
# n=4
# def findmissingnumber(num):
#     for i in range(0,n+1):
#         if i not in num:
#             return i 
        
# print(findmissingnumber(num))
''' num=[1,0,3,4]
n=4
def findmissingnumber(num):
    freq={}
    for i in range(0,n+1):
        freq[i]=0
    for j in num:
        freq[j]=1
    for u,v in freq.items():
        if v==0:
         return u 
     
print(findmissingnumber(num))

time complexity is O(m+n+k)=O(n)
space complexity is O(n)
'''

num=[1,0,3,4]
n=4
def findmissingnumber(num):
    sum=0
    for i in num:
        sum+=i
    return (n*(n+1))/2-sum

print(findmissingnumber(num))
        