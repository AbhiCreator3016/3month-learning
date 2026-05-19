# EXERCISE: Candidate Screening Pipeline
# Your task: complete the functions marked with TODO

import numpy as np
import pandas as pd

# Dataset: 8 internship candidates
candidates = pd.DataFrame({
    "name":       ["Arjun","Priya","Ravi","Sneha","Dev","Meera","Karan","Zara"],
    "python":     [8, 9, 6, 7, 9, None, 8, 7],   # skill score out of 10
    "ml":         [7, 8, 5, 9, 6, 8, None, 8],
    "sql":        [9, 6, 8, 7, 5, 9, 7, None],
    "domain":     ["ML","CV","NLP","ML","CV","NLP","ML","CV"]
})

df = pd.DataFrame(candidates)


# TODO 1: Print the shape of the dataframe

# print(f"Shape:{df.shape}")



# TODO 2: Count missing values in each column

# print(df.isnull().sum())



# TODO 3: Fill all missing values with the column mean
cols_to_fix = ["python","ml","sql"]
df[cols_to_fix] = df[cols_to_fix].fillna(df[cols_to_fix].mean())

# df = df.fillna(df.mean(numeric_only=True))        # fix all numerical cols
# df["ml"] = df["ml"].fillna(df["ml"].mean())       # manual one col fix

print(df)

# TODO 4: Create a new column "total_score" = average of python + ml + sql

# df["total_score"] = df[["python","ml","sql"]].mean(axis=1)
# print(df)

# TODO 5: Print the top 3 candidates sorted by total_score (descending)

# sorted_cand = df.sort_values(by="total_score", ascending=False)
# print(sorted_cand)


# TODO 6: Print average total_score per domain using groupby

# grouped_data = df.groupby("domain")["total_score"].agg(["mean"])
# print(grouped_data)
