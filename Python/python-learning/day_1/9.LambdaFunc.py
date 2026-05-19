#====================================================
#                   NORMAL FUNCTION 
#====================================================
print("====== Normal Function ======")
def square(num):

    return num*num

print(f"Square of 4 is :{square(4)}")

#====================================================
#                   LAMBDA FUNCTION 
#====================================================

#---------->   lambda arguments: expression

square = lambda x: x*x
print(f"Square of 4 is :{square(4)}")


#====================================================
#                   LAMBDA with MAP 
#====================================================
print("="*40)
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Orignal Numbers : {nums}")
double = list(map(lambda x: x*2, nums))
print(f"Double Numbers : {double}")
print("="*40)




#====================================================
#                   LAMBDA with FILTER
#====================================================
print("="*40)
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# filter() check karega ki kaunsa number lambda ki condition (x % 2 == 0) 
# satisfy karta hai
print(f"Orignal Numbers : {nums}")
even_nums = list(filter(lambda x: x%2==0,nums))
print(f"Even Numbers : {even_nums}")
print("="*40)



#====================================================
#                   LAMBDA with SORT
#====================================================

#Jab normal sorting se kaam na chale, toh key=lambda ... ka use karo.
# lambda x: x[0] -> Pehle element ke basis par sort karega.
# lambda x: x[1] -> Doosre element ke basis par sort karega.
# lambda x: len(x) -> Size/Length ke basis par sort karega.


#--------------> Sort Dictionary 

print("="*40)
products = [
    {"name": "Laptop", "price": 50000},
    {"name": "Mobile", "price": 15000},
    {"name": "Earphones", "price": 2000}
]

products.sort(key=lambda x: x["price"])
for x in products:
    print(x)

products.sort(key=lambda x: x["price"], reverse=True)
for x in products:
    print(x)
print("="*40)
#-------------> Sort on basis of element length
print("="*40)
words = ["Banana", "Apple", "Kiwi", "Watermelon"]
print(words)
sorted_words = sorted(words, key=lambda x: len(x))
print(f"Sorted on basis of length:")
print(sorted_words)
print("="*40)

