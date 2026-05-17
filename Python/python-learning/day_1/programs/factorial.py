

def fact(num):
    fact = 1
    while(num>1):
        fact = fact* num
        num = num-1
    return fact

num = int(input("Enter the number for it's factorial:"))
print("wah !, wha !. Good choice of number....")
print(fact(num))