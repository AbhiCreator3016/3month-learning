import numpy as np
import pandas as pd

#============ create a DataFrame ============
data = {
    "name"  : ["Arjun", "Priya", "Ravi", "Sneha", "Dev"],
    "age"   : [21, 23, 22, None, 24],      # None = missing value
    "score" :   [88, 94, 71, 85, 90],
    "domain":  ["ML", "CV", "NLP", "ML", "NLP"]
}

df = pd.DataFrame(data)
# print(df)
# print("\nShape:", df.shape)          # (5, 4)
# print("\nInfo:")
# print(df.info())                     # column types + non-null counts
# print("\nStats:")
# print(df.describe())                # mean, std, min, max, 25%tile etc

#============ Handling missing values ============

#----------> df.fillna(0, inplace=True) 
# inplace=true will make change in the orignal data

# print("\nMissing Values : \n",df.isnull().sum()) #Tell us total missing values by column
# df["age"] = df["age"].fillna(df["age"].mean())
# print("\nFixed the missing values:\n")
# print(df)


#============  Filtering rows ============

# high_scorers = df[df["score"]>90]
# print("High Scorers: ")
# print(high_scorers)

# ml_team = df[df["domain"] == "ML"]
# print("ML team : ")
# print(ml_team)


#============  Selecting Columns ============

# print(df[["name","score"]])   


#============  GroupBy - aggregation category  ============

# domain_stats = df.groupby("domain")["score"].agg(["mean","max","count"])
# print("\nDomain stats:\n", domain_stats)


#=============  Creating new column (feature Engineering) ============

df["grade"] = df["score"].apply(lambda x: "A" if x>=85 else "B") #.map() can also be used
print(df)
