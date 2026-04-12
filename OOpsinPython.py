# class Student:
#     def __init__(self,name,sub1,sub2,sub3):
#         self.name=name
#         self.sub1=sub1
#         self.sub2=sub2
#         self.sub3=sub3
#     def ko(self):
#         print((self.sub1+self.sub2+self.sub3)/3)
# sub=Student("hoh",30,30,30)
# sub.ko()

class Account:
    def __init__(self,balance,accno):
        self.balance=balance
        self.accno=accno
    def debit(self,num):
        self.num=num
        self.balance=self.balance-self.num
    def credit(self,num):
        self.num=num
        self.balance=self.balance+self.num
    def print(self):
        print(self.balance)
        
san=Account(500,420)
san.print()   
san.debit(100)  
san.print()
san.credit(100)     
san.print()