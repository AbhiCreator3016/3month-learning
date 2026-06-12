import csv

# ── WRITE A CSV ───────────────────────────────────────────────
students = [
    ["name",  "cgpa", "problems", "placed"],
    ["Arjun", 7.8,    65,         1],
    ["Priya", 9.0,    80,         1],
    ["Ravi",  6.0,    20,         0],
    ["Sneha", 8.5,    75,         1],
]

with open("students.csv","w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)
print("CSV written")

# ── READ A CSV ───────────────────────────────────────────────

with open('students.csv','r') as file:
    reader = csv.DictReader(file)
    for line in reader:
        print(f"{line['name']} | CGPA: {line['cgpa']} | Placed: {line['placed']}")