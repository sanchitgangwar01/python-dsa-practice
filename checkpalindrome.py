initial = 686
old_num = initial
new_num=0
while old_num>0:
    new_num=new_num*10+(old_num%10) 
    old_num = old_num//10
    
if new_num== initial:
    print("number is palindrome")