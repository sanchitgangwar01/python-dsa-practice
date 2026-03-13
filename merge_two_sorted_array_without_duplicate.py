num1=[1,2,4,5,3,6,4,3,3]
num2=[3,4,5,4,3,3,2,3,4]
result=[]
def merge_two_sorted_arrary(num1,num2):
    n=len(num1)
    m=len(num2)
    i=0
    j=0
    while i<n and j<m:
        if num1[i]<=num2[j]:
            if len(result)==0 or result[-1]!=num1[i]:
                result.append(num1[i])
            i+=1
        else:
            if len(result)==0 or result[-1]!=num2[i]:
                result.append(num2[i])
            j+=1
    while i<n:
            if len(result)==0 or result[-1]!=num1[i]:
                result.append(num1[i])
            i+=1
    while j<m:
            if len(result)==0 or result[-1]!=num2[i]:
                result.append(num2[i])
            j+=1
    return result
print(merge_two_sorted_arrary(num1,num2))

                