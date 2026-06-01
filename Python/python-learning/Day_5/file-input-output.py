# ── THE 4 MODES YOU NEED ──────────────────────────────────────
# 'r'  → read   (file must exist)
# 'w'  → write  (creates new file OR overwrites existing)
# 'a'  → append (adds to end, never overwrites)
# 'r+' → read + write

# ── WRITING A FILE ────────────────────────────────────────────
# Always use 'with' — it closes the file automatically
# even if an error occurs halfway through

with open("results.txt","w") as f:
    f.write("Experiment: ResNet51\n")
    f.write("Accuracy  : 0.94\n")
    f.write("F1 Score  : 0.91\n")
print("File written.")

# ── READING A FILE ────────────────────────────────────────────

with open("results.txt","r") as f:
    content = f.read()
print(f"File: results.txt:\n{content}")

# Read line by line - for large files....

with open("results.txt","r") as f:
    for line in f:
        print(">",line.strip())

# ── READING A FILE ────────────────────────────────────────────