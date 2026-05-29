class Dataset:
    # CLASS VARIABLE: Sabhi objects ke liye common (shared state)
    total_datasets_created = 0 

    def __init__(self, name, data, labels):
        # INSTANCE VARIABLES: Har object ka apna alag data
        self.name = name
        self.data = data
        self.labels = labels
        # Class variable ko update karne ke liye Class ka naam use karo
        Dataset.total_datasets_created += 1
    
    # INSTANCE METHOD: Object ke 'self' data par operations karta hai
    def summery(self):
        print(f"Dataset : {self.name}")
        print(f"Samples : {len(self.data)}")
        print(f"Features : {len(self.data[0])}")
        print(f"Classes : {set(self.labels)}")

    # INSTANCE METHOD: 'self' access hai, toh object specific data nikalo
    def get_sample(self, index=0):
        print(f"Sample Data : {self.data[index]}")
        print(f"Sample output : {self.labels[index]}")

    # INSTANCE METHOD: Data slice karke train/test splits return karta hai
    def train_test_split(self, test_ratio=0.2):
        # 'self.data' use karo kyunki data object ke andar hai
        split = int(len(self.data) * (1 - test_ratio)) 
        X_train = self.data[:split]
        X_test = self.data[split:]
        Y_train = self.labels[:split]
        Y_test = self.labels[split:]
        return X_train, X_test, Y_train, Y_test
    
    # CLASS METHOD: Sirf class-level data (total_datasets_created) ke liye
    @classmethod
    def dataset_downloads(cls):
        print(f"Total dataset created so far : {cls.total_datasets_created}")

    # CLASS METHOD (Factory): Naya object create karne ka alag tarika
    @classmethod
    def from_csv(cls, filepath):
        print(f"Loading dataset from {filepath}...")
        # 'cls' se naya object banta hai (constructor call)
        return cls(name=filepath, data=[[1,2],[3,4]], labels=[0,1])

    # STATIC METHOD: Independent helper, na 'self' ki zaroorat, na 'cls' ki
    @staticmethod
    def normalization(data):
        min_v = min(data)
        max_v = max(data)
        # List Comprehension: Pure list par math ek line mein
        return [((value - min_v) / (max_v - min_v)) for value in data]

# --- USAGE ---
data = [[7.8, 65], [6.0, 20], [9.0, 80], [5.5, 15], [8.5, 75]]
labels = [1, 0, 1, 0, 1]

# Object creation (calls __init__)
ds = Dataset("Placement", data, labels)
ds.summery()
ds.get_sample(2)

# Logic testing
X_train, X_test, Y_train, Y_test = ds.train_test_split(0.3)
print(f"X_train : {X_train}")

# Class method call (tracks total count)
ds.dataset_downloads()

# Factory method call (creates another object)
ds2 = Dataset.from_csv("filename.csv")
ds.dataset_downloads()

# Static method call (math helper)
normalized = Dataset.normalization(labels)
print(f"Normalized : {normalized}")
