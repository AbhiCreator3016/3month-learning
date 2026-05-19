# A List in Python is a collection used to store multiple items in a single variable.

# Lists are:

# Ordered
# Mutable (changeable)
# Allow duplicate values
# Can store different datatypes
scores = [88, 92, 76, 85, 91]

#============>  Accessing list element
print(scores[0]) # index start at 0
print(scores[2]) # element at index 2
print(scores[-1]) # last index
print(scores[1:4]) #slicing 
print(scores[::-1]) #list reverse

#============> Adding element to list
scores.append(84)
print(scores)

#============>  Update value
scores[2] = 86

#============> remove()
scores.remove(84)

#===========> min, max, sum
print(f"Min in score: {min(scores)}")
print(f"Max in score: {max(scores)}")
print(f"Sum in score: {sum(scores)}")

#============> Manual loop 
for x in scores:
    print(f"Score: {x}") 

#============>  List comprehensiaon
squared = [x**2 for x in scores]
print(squared) 


#============> Baic Filter 
above_84 = [x for x in scores if x>85]
print(above_84)