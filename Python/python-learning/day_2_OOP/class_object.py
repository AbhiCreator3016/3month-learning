
class AIModel:
    """Class for AI Models"""

    def __init__(self,name,version):
        self.name = name
        self.version = version
        self.accuracy = 0.0
        self.trained = False

    def describe(self):
        status = "Trained" if self.trained else "Untrained"

        print(f"Model name : {self.name} v{self.version}")
        print(f"Status : {status}")
        print(f"Accuracy  : {self.accuracy:.2%}")


model1 = AIModel(name="PlacementPredictor", version='1.0')
model2 = AIModel(name="SentimentAnalysis", version='2.1')

model1.accuracy = 0.94
model2.accuracy = 0.0
model1.trained = True

model1.describe()

model2.describe()

print(f"\nModel name: {model1.name}")
print(f"Modle accuracy: {model1.accuracy}")
