# ── CREATING YOUR OWN MODULE ──────────────────────────────────────
# Imagine this is a separate file called "preprocessing.py":

def normalization(values):
    min_v, max_v = min(values), max(values)
    if max_v == min_v:
        return [0.0 for _ in values]
    return [(v - min_v) / (max_v - min_v) for v in values]

def clear_missing(data, fill_value=0):
    # Use 'is' to compare against None
    return [fill_value if v is None else v for v in data]

def main():
    """
    This block only runs if you execute this file directly.
    Great for testing your functions!
    """
    sample_data = [10, None, 30, 10]
    
    # Testing the logic
    cleaned = clear_missing(sample_data)
    normalized = normalization(cleaned)
    
    print(f"Original: {sample_data}")
    print(f"Normalized: {normalized}")

if __name__ == "__main__":
    main()