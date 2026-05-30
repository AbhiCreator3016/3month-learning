class myModule:
    # Base class initialization: internal dictionary to store parameters
    def __init__(self):
        self._parameters = {}

    # Method to track parameters for management and enable 'dot' access (e.g., net.weights)
    def register_parameter(self, name, value):
        self._parameters[name] = value
        setattr(self, name, value)

    # Returns the count of parameter groups registered in the module
    def parameters(self):
        return len(self._parameters.values())
    
    # Placeholder method; forces children to define their own math logic
    def forward(self,X):
        raise NotImplementedError("Subclass must implement forward()")
    
    # Magic method: Allows calling the object like a function: net(input_data)
    def __call__(self, X):
        """Makes model(x) work instead of model.forward(x)."""
        return self.forward(X)


class TinyLinearNet(myModule):
    # Initialize the network with specific feature dimensions
    def __init__(self, out_features, in_features):
        super().__init__() # Call the base class setup
        import random
        # Create random weights using Gaussian distribution (mean=0, std=0.1)
        weights = [random.gauss(0,0.1) for _ in range(in_features*out_features)]
        # Initialize biases as zeros
        bias = [0.0] * out_features
        # Register them so the framework knows they exist
        self.register_parameter("weights",weights)
        self.register_parameter("bias",bias)
        # Store dimensions for use during the forward pass
        self.in_features = in_features
        self.out_features = out_features
    
    # The math engine: Performs y = Wx + b
    def forward(self, X):
        # simple linear transformation : y = mx + C
        output = []
        # Outer loop: Iterate through each output neuron
        for j in range(self.out_features):
            val = self.bias[j] # Start with the neuron's bias
            # Inner loop: Iterate through each input feature
            for i in range(self.in_features):
                # Multiply input by weight and accumulate to bias
                val += self.weights[(j * self.in_features) + i] * X[i]
            output.append(val) # Store final result for this neuron
        return output

# --- Execution Phase ---

# Instantiate the network (mimicking PyTorch's nn.Linear)
net = TinyLinearNet(in_features=2, out_features=1)
# Define input features (e.g., normalized data)
input_data = [0.78, 0.68]
# Run the forward pass (triggering __call__ -> forward)
output = net(input_data)
# Display the network's prediction
print(f"Network output:{output[0]:.4f}")
# Display total registered parameter groups
print(f"Parameters: {net.parameters()} groups")