# Function returning sum

def add(a, b):
    return a + b

result = add(10, 20)

print(result)

# Keyword Arguments

def student(name, age):
    print(f"Welcome {name}, age {age}")


student(age = 22, name = "abhi")


# Arbitrary Arguments (*args)
def total(*numbers):

    print(numbers)

    print(sum(numbers))


total(10, 20, 30)

#  Keyword Variable Arguments (**kwargs)
def details(**data):

    print(data)


details(name1="Abhishek", age1=21, name2= "Tika", age2=22, name3="Malkhan", age3=22)


