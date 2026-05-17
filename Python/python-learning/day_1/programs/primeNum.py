
def checkPrime(num):
    limit = num // 2
    for i in range(2, limit + 1):
        if num % i == 0:
            return False
    
    return True

num = int(input("Enter the number: "))
print(checkPrime(num))


