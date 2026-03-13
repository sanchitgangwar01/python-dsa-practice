def factorial(n):
    print("loop running")
    if n<1: 
     return 1
    return n*factorial(n-1)
print(factorial(5))