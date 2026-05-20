import numpy as np

# ===  ACTIVATION FUNCTION  =============================================
# --> Add non-Linearity to the model

def sigmoid(x):
    """Squashes any number to range (0, 1). Used in output layer for binary classification."""
    return 1/(1+np.exp(-x))

def sigmoid_derivative(x):
    """Rate of change of sigmoid - needed for backpropagation."""
    s = sigmoid(x)
    return s * (1 - s)

def relu(x):
    """Most common hidden layer activation. Simple: max(0, x)."""
    return np.maximum(0,x)

def relu_derivative(x):
    return (x > 0).astype(float)
    
#--> Testing the functions 
x = np.array([-2,-1,0,1,2])
print("Sigmoid: ", sigmoid(x))
print("ReLu: ", relu(x))


#===  LOSS FUNCTION  ===================================================

def mse_loss(y_actual, y_pred):
    """Mean Squared Error — how wrong our predictions are on average."""
    """ pred = (y_pred - y_actual)^2 """
    return np.mean((y_pred - y_actual)**2)

def mse_derivative(y_actual, y_pred):
    """Gradient of MSE w.r.t. predictions."""
    return 2*(y_pred-y_actual) / len(y_actual)


#=== THE NEURAL NETWORK ================================================
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        """
        Architecture: input → hidden layer (ReLU) → output layer (Sigmoid)
        
        Xavier initialization: weights scaled by sqrt(2/n_inputs)
        This prevents vanishing/exploding gradients at initialization."""
        

        np.random.seed(42)

        #Layer 1: input -> hidden 
        self.w1 = np.random.randn(input_size, hidden_size) * np.sqrt(2/input_size)
        self.b1 = np.zeros((1,hidden_size))

        #Layer 2: hidden -> output
        self.w2 = np.random.randn(hidden_size,output_size) * np.sqrt(2/hidden_size)
        self.b2 = np.zeros((1,output_size))
    
    def forward(self, X):
        """
        Forward pass: data flow INPUT -> HIDDEN -> OUTPUT
        We store intermediate values for backprop.
        """
        # Layer 1
        self.z1 = X @ self.w1 + self.b1             # linear combination
        self.a1 = relu(self.z1)                     # activation function
        
        # Layer 2
        self.z2 = self.a1 @ self.w2 + self.b2
        self.a2 = sigmoid(self.z2)                  # output: probability 0-1

        return self.a2
    
    def backward(self, X, y_actual, learning_rate=0.01):
        """
        Backward pass: Gradients flow OUTPUT -> HIDDEN -> INPUT
        This is the 'chain rule' from calculus applied layer by layer.
        """

        m = len(X) #number of samples

        # --- Output layer gradients -------------------------------------

        dL_da2 = mse_derivative(y_actual, self.a2)  # loss -> output
        da2_dz2 = sigmoid_derivative(self.z2)       # output activation gradinet
        delta2 = dL_da2 * da2_dz2                   # combined: shape (m, output_size)

        dw2 = self.a1.T @ delta2/m                  # weight gradient
        db2 = np.mean(delta2, axis=0, keepdims=True)#bias gradient

        # ── Hidden layer gradients ──
        delta1 = (delta2 @ self.w2.T) * relu_derivative(self.z1)
        dw1 = X.T @ delta1 / m
        db1 = np.mean(delta1, axis=0, keepdims=True)


        # ── Update weights (gradient descent step) ──
        self.w2 -= learning_rate * dw2
        self.b2 -= learning_rate * db2
        self.w1 -= learning_rate * dw1
        self.b1 -= learning_rate * db1

    def train(self, X, y, epochs=1000, learning_rate=0.01):
        """Full training loop."""
        losses = []
        for epoch in range(epochs):
            predictions = self.forward(X)
            loss = mse_loss(y, predictions)
            self.backward(X, y, learning_rate)
            
            if epoch % 100 == 0:
                print(f"Epoch {epoch:4d} | Loss: {loss:.6f}")
            losses.append(loss)
        return losses
    
    def predict(self, X, threshold=0.5):
        probs = self.forward(X)
        return (probs >= threshold).astype(int)


# ── TRAIN ON XOR PROBLEM ──────────────────────────────────────
# XOR cannot be solved by a straight line — needs a hidden layer
# This is the classic proof that neural networks go beyond linear models

X = np.array([[0,0], [0,1], [1,0], [1,1]])   # inputs
y = np.array([[0],   [1],   [1],   [0]])      # XOR labels

nn = NeuralNetwork(input_size=2, hidden_size=4, output_size=1)
losses = nn.train(X, y, epochs=5000, learning_rate=0.1)

print("\n── Final Predictions ──")
preds = nn.forward(X)
for i in range(len(X)):
    print(f"  {X[i]} → predicted: {preds[i][0]:.4f} | actual: {y[i][0]}")