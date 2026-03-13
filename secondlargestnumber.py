# num = [7,6,5,9,1,7]
# def largestnumber(num):
#     largest= float("-inf")
#     s_largest = float("-inf")
#     n=len(num)
#     for i in range(0,n):
#         if num[i]>largest:
#             largest= num[i]
#     for i in range(0,n):
#         if num[i]>s_largest and num[i]<largest:
#             s_largest=num[i]
#     return s_largest

# print(largestnumber(num))


# optimal solution using single loop
num = [7,6,5,9,1,7]
def second_largest_number(num):
    largest = float("-inf")
    s_largest = float("-inf")
    n=len(num)
    for i in range(0,n):
        if num[i]>largest:
            s_largest=largest
            largest=num[i]
        elif num[i]>s_largest and num[i]!=largest:
            s_largest=num[i]
    return s_largest

print(second_largest_number(num))   