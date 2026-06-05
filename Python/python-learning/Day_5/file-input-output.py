# ── THE 4 MODES YOU NEED ──────────────────────────────────────
# 'r'  → read   (file must exist)
# 'w'  → write  (creates new file OR overwrites existing)
# 'a'  → append (adds to end, never overwrites)
# 'r+' → read + write

# ── WRITING A FILE ────────────────────────────────────────────
# Always use 'with' — it closes the file automatically
# even if an error occurs halfway through
with open("result.txt",'w') as file:
    file.write("List of Items:\n")
    file.write("1. Toothpaste\n")
    file.write("2. Shower Gel\n")
    file.write("3. Shampoo\n")
print("result.txt file created and data added.\n")

# ── READING A FILE ────────────────────────────────────────────

with open("result.txt","r") as file:
    content = file.read()
    print(content)

# Read line by line - for large files....

with open("result.txt","r") as file:
    for line in file:
        print(line.strip())



# ── APPENDING - add without overwriting ────────────────────────────────────────────

with open("result.txt","a") as file:
    file.write("4. Tooth brush.\n")

# ── Reading all the lines into a list ────────────────────────────────────

with open("result.txt","r") as file:
    lines = file.readlines()
print(lines)
