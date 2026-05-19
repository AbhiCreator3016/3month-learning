

#============>  Loops are used to execute a block of code repeatedly.

# FOR LOOP

for x in range(1,6):
    print(x,end=",")

fruits = ["apple", "banana", "mango"]

print("\nFruits: ",end="")
for fruit in fruits:
    print(fruit,end=",")


student = {
    "name": "Abhishek",
    "age": 21
}

for key, value in student.items():
    print(key, value)


name = "Python"

for ch in name:
    print(ch)

# While Loop

marks = [85, 90, 78, 92]

count = 0

while count < len(marks):
    print("Index:", count, "Value:", marks[count])
    count += 1