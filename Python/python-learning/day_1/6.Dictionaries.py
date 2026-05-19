# =========================================
# PYTHON DICTIONARY COMPLETE EXAMPLE
# =========================================

# Creating a dictionary
student = {
    "name": "Abhishek",
    "age": 21,
    "course": "Machine Learning",
    "skills": ["Python", "ML", "SQL"],
    "marks": 92
}

# -----------------------------------------
# Print complete dictionary
# -----------------------------------------
print("Complete Dictionary:")
print(student)

# =========================================
# ACCESSING VALUES
# =========================================

# Access value using key
print("\nStudent Name:")
print(student["name"])

# Access using get() method
print("\nStudent Course:")
print(student.get("course"))

# Access list inside dictionary
print("\nStudent Skills:")
print(student.get("skills"))

# Access single item from list
print("\nFirst Skill:")
print(student.get("skills")[0])

# =========================================
# ADDING NEW DATA
# =========================================

# Add new key-value pair
student["city"] = "Jaipur"

print("\nAfter Adding City:")
print(student)

# =========================================
# UPDATING DATA
# =========================================

# Update existing value
student["marks"] = 95

print("\nAfter Updating Marks:")
print(student)

# =========================================
# REMOVE DATA
# =========================================

# Remove item using pop()
student.pop("age")

print("\nAfter Removing Age:")
print(student)

# =========================================
# DICTIONARY METHODS
# =========================================

# Get all keys
print("\nAll Keys:")
print(student.keys())

# Get all values
print("\nAll Values:")
print(student.values())

# Get all key-value pairs
print("\nAll Items:")
print(student.items())

# =========================================
# LOOP THROUGH DICTIONARY
# =========================================

print("\nLooping Through Dictionary:")

for key, value in student.items():
    print(key, ":", value)

# =========================================
# LOOP THROUGH SKILLS LIST
# =========================================

print("\nStudent Skills:")

for skill in student.get("skills"):
    print(skill)

# =========================================
# CHECK IF KEY EXISTS
# =========================================

if "name" in student:
    print("\n'name' key exists")

# =========================================
# LENGTH OF DICTIONARY
# =========================================

print("\nTotal Number of Keys:")
print(len(student))

# =========================================
# COPY DICTIONARY
# =========================================

student_copy = student.copy()

print("\nCopied Dictionary:")
print(student_copy)

# =========================================
# UPDATE METHOD
# =========================================

student.update({
    "phone": 9876543210,
    "course": "AI & ML"
})

print("\nAfter update() Method:")
print(student)

# =========================================
# NESTED DICTIONARY
# =========================================

company = {
    "employee1": {
        "name": "Rahul",
        "skills": ["Python", "Django"]
    },

    "employee2": {
        "name": "Priya",
        "skills": ["Java", "SQL"]
    }
}

print("\nNested Dictionary:")
print(company)

# Access nested dictionary data
print("\nEmployee2 Name:")
print(company["employee2"]["name"])

# Access nested list item
print("\nEmployee1 First Skill:")
print(company["employee1"]["skills"][0])

# =========================================
# CLEAR METHOD
# =========================================

temp = {
    "a": 1,
    "b": 2
}

print("\nBefore clear():")
print(temp)

# Remove all items
temp.clear()

print("\nAfter clear():")
print(temp)

# =========================================
# SAFE get() EXAMPLE
# =========================================

print("\nUsing get() with Missing Key:")

print(student.get("salary"))   # Returns None

print(student.get("salary", "Not Found"))

# =========================================
# END OF PROGRAM
# =========================================