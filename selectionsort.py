num = [7,4,3,6,4,3,1,2]
def selectionsort(num):
    n = len(num)
    for i in range(0,n):
        min_index =i
        for j in range(i+1, n):
            if num[j]<num[min_index]:
                min_index=j
        num[i],num[min_index]=num[min_index],num[i]
selectionsort(num)   
print(num)