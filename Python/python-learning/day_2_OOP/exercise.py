
#-- Todo 1:-------------------------------------------------------------
class Experiment:
    def __init__(self, name, dataset_name):
        self.name = name
        self.dataset_name = dataset_name
        self.results = {}

    def log_result(self, metric_name, value):
        self.results[metric_name] = value
        setattr(self, metric_name, value)

    def summary(self):
        print(f"Model name   :{self.name}")
        print(f"Dataset name :{self.dataset_name}")
        print(f"Results:")
        for matric, value in self.results.items():
            print(f"{matric}:{value}")


    def __str__(self):
        return(f"Experiment: {self.name} on {self.dataset_name}")
    
# exp = Experiment("Test1", "PlacementData")
# exp.log_result("accuracy", 0.91)
# exp.log_result("f1_score", 0.89)
# exp.summary()
# print(str(exp))   # triggers __str__

# -- Todo 2: --------------------------------------------------------- 
class ClassificationExperiment(Experiment):
    def __init__(self, name, dataset_name,n_classes):
        super().__init__(name,dataset_name)
        self.n_classes = n_classes

    def summary(self):
        super().summary()
        print(f"Classes :{self.n_classes}")
    
    def is_good(self):
        if 'accuracy' in self.results and self.results['accuracy'] > 0.85:
            return True
        return False
    
# ce = ClassificationExperiment("ResNet50", "CIFAR10", n_classes=10)
# ce.log_result("accuracy", 0.91)
# ce.log_result("f1_score", 0.88)
# ce.summary()
# print(f"Is good? {ce.is_good()}")   # True
# print(str(ce))                      # triggers __str__ from grandparent

#-- Todo 3: --------------------------------------------------------------

class RegressionExperiment(Experiment):
    def __init__(self, name, dataset_name):
        super().__init__(name, dataset_name)

    def summary(self):                          # ✓ correct spelling
        print("── Regression Experiment ──")    # ✓ labels it as regression
        super().summary()   

    def is_good(self):
        if 'mse' in self.results and self.results['mse'] < 0.05:
            return True
        return False

    
# re = RegressionExperiment("LinearReg", "HousingData")
# re.log_result("mse",  0.032)
# re.log_result("rmse", 0.179)
# re.summary()
# print(f"Is good? {re.is_good()}")
# print(str(re))

#-- Todo 4: ----------------------------------------------------------------

c_obj1 = ClassificationExperiment("ResNet51","CIFAR11",n_classes=10)
c_obj2 = ClassificationExperiment("ResNet52","CIFAR12",n_classes=10)
r_obj3 = RegressionExperiment("LinearReg","HousingData")

# ── Object 1 ─────────────────────────────────────────────────

# c_obj1.log_result("accuracy",0.92)
# c_obj1.log_result("f1_score",0.88)
# c_obj1.summary()
# print(f"is Good? {c_obj1.is_good()}")

# ── Object 2 ─────────────────────────────────────────────────

# c_obj2.log_result("accuracy",0.87)
# c_obj2.log_result("f1_score",0.89)
# c_obj2.summary()
# print(f"is Good? {c_obj2.is_good()}")

# ── Object 3 ─────────────────────────────────────────────────

# r_obj3 = RegressionExperiment("LinearReg", "HousingData")
# r_obj3.log_result("mse",  0.032)       # ✓ below 0.05 — is_good() = True
# r_obj3.log_result("rmse", 0.179)
# r_obj3.summary()
# print(f"Is good? {r_obj3.is_good()}")


#-- Todo 5 -------------------------------------------------------------

experiments  = [c_obj1,c_obj2,r_obj3]

for obj in experiments:
    print(obj)

    if isinstance(obj,ClassificationExperiment):
        print("Type : Classification Experiment")
    elif isinstance(obj,RegressionExperiment):
        print("Type : Regression Experiment")

