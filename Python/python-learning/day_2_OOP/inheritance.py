# ── PARENT CLASS (general) ────────────────────────────────────
class BaseModel:
    """
    Every AI model shares these behaviors.
    This is the parent — the general version.
    """
    def __init__(self, name, learning_rate=0.01):
        self.name          = name
        self.learning_rate = learning_rate
        self.is_trained    = False
        self.history       = []          # stores loss per epoch

    def train(self, X, y, epochs=100):
        """Simulate training — child classes will override this."""
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
        return f"<{self.name} | trained={self.is_trained} | lr={self.learning_rate}>"


# ── CHILD CLASS 1 — inherits everything, adds its own stuff ───
class LinearModel(BaseModel):
    """
    Specialized model for linear problems.
    Inherits all BaseModel behavior, adds weights.
    """
    def __init__(self, name, n_features, learning_rate=0.01):
        # super() calls the parent's __init__
        # — always call this first in child __init__
        super().__init__(name, learning_rate)
        self.weights = [0.0] * n_features
        self.bias    = 0.0

    # OVERRIDE parent's train method with specific behavior
    def train(self, X, y, epochs=100):
        print(f"[LinearModel] Training with gradient descent...")
        print(f"  Features : {len(self.weights)}")
        print(f"  Epochs   : {epochs}")
        print(f"  LR       : {self.learning_rate}")
        self.is_trained = True
        print(f"  Done. Weights updated.")

    def predict(self, x):
        """Dot product of input and weights + bias."""
        return sum(w * xi for w, xi in zip(self.weights, x)) + self.bias


# ── CHILD CLASS 2 — different specialization ──────────────────
class TreeModel(BaseModel):
    """
    Specialized model for tree-based problems.
    Inherits all BaseModel behavior, adds tree-specific params.
    """
    def __init__(self, name, max_depth=5, learning_rate=0.01):
        super().__init__(name, learning_rate)
        self.max_depth = max_depth
        self.n_trees   = 0

    def train(self, X, y, epochs=100):
        print(f"[TreeModel] Growing {epochs} trees up to depth {self.max_depth}...")
        self.n_trees    = epochs
        self.is_trained = True
        print(f"  Done. {self.n_trees} trees grown.")

    def feature_importance(self):
        if not self.is_trained:
            print("Train first!")
            return
        print("Feature importance: [0.45, 0.30, 0.25]")


# ── USING INHERITANCE ─────────────────────────────────────────
lm = LinearModel("RegressionModel", n_features=3, learning_rate=0.05)
tm = TreeModel("RandomForest", max_depth=10)

# Both have BaseModel methods (save, evaluate, __str__)
print(lm)
print(tm)

# Each calls its OWN version of train()
lm.train(X=None, y=None, epochs=200)
tm.train(X=None, y=None, epochs=50)

lm.evaluate()    # inherited from BaseModel — no need to rewrite
lm.save("models/linear_v1.pkl")

tm.feature_importance()   # only TreeModel has this

# isinstance() — check if object belongs to a class
print(f"\nIs lm a BaseModel? {isinstance(lm, BaseModel)}")   # True
print(f"Is lm a TreeModel? {isinstance(lm, TreeModel)}")    # False
print(f"Is tm a BaseModel? {isinstance(tm, BaseModel)}")    # True