class BaseModel:
    def __init__(self,name,learning_rate=0.1):
        self.name = name
        self.learning_rate = learning_rate
        self.is_trained = False
        self.history = []


    def train(self, X=0, Y=0, epochs=100):
        print(f"Training {self.name} for {epochs} epochs...")
        self.is_trained = True

    def evaluate(self):
        if not self.is_trained:
            print("Model not trained yet!")
            return
        print(f"{self.name} evaluated successfully.")
    def save(self, path):
        print(f"Model saved to {path}")

    def __str__(self):
        return f"<{self.name} | trained={self.is_trained} | Learning R={self.learning_rate}>"


mod1 = BaseModel("neural network")
mod1.train()
mod1.evaluate()
mod1.save("./model")

        