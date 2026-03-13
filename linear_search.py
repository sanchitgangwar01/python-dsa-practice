num=[1,2,3,5,6]
find=4

def linearsearch(num):
    n=len(num)
    for i in range(0,n):
        if find ==num[i]:
            return i     
    return -1
        
print(linearsearch(num))
        