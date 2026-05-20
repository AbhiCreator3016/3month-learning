
# Import NumPy
import numpy as np


# ======================================
# NEURAL NETWORK CLASS
# ======================================

class NeuralNetwork:

    # Constructor
    def __init__(self, rows, cols):

        # Set seed for reproducible random values
        np.random.seed(42)

        # Weight matrix
        self.w1 = np.random.randn(rows, cols)

        # Bias matrix
        self.b1 = np.zeros((1, cols))

    # Method to print matrices
    def printMatrix(self):

        print("Weight Matrix (w1):\n")
        print(self.w1)

        print("\nShape of w1:")
        print(self.w1.shape)

        print("\nBias Matrix (b1):\n")
        print(self.b1)

        print("\nShape of b1:")
        print(self.b1.shape)


# ======================================
# MAIN PROGRAM
# ======================================

# Create object
nn = NeuralNetwork(3, 4)

# Print matrices
nn.printMatrix()