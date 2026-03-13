num1= [2,5,3,5,6]
def merge_sort(num1):
        print("loop runninng")
        if len(num1)<=1:
            return num1
        mid = len(num1)//2
        left_arr = num1[:mid]
        right_arr = num1[mid:]
        left= merge_sort(left_arr)
        right=merge_sort(right_arr)
        return merge_array(left,right)

def merge_array(left,right):
        n=len(left)
        m=len(right)
        i,j=0,0
        emp = []
        while i<n and j<m:
            if left[i]<=right[j]:
                emp.append(left[i])
                i+=1
            else:
                emp.append(right[j])
                j+=1
        if i<n:
            while i<n:
                emp.append(left[i])
                i+=1
        if j<n:
            while j<m:
                emp.append(right[j])
                j+=1
        return emp
print(merge_sort(num1))