num = [2,8,9,2,6,1,3,4,5,7,8,7]
def largets_number(num):
    largest= num[0]
    for i in num:
        if largest < i:
            largest=i
    return largest

print(largets_number(num))