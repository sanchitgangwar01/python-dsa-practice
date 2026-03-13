num = [1,2,3,4,5,1]
def sorte_array(num):
    large = num[0]
    for i in num:
        if i>large:
            large = i
        else:
            return False
    return True

print(sorte_array(num))