import numpy as np

class CNN:
    def __init__(self, input_shape, num_classes, filters, filter_sizes, depths, dropout_rate=0.5, momentum=0.9, learning_rate=0.001):
        self.input_shape = input_shape  # (height, width, channels)
        self.num_classes = num_classes
        self.filters = filters  # list of the number of filters at each layer
        self.filter_sizes = filter_sizes  # list of filter sizes at each layer
        self.depths = depths  # list of the depth of each layer (1 for conv, 2 for conv + batch norm, etc)
        self.dropout_rate = dropout_rate
        self.momentum = momentum
        self.learning_rate = learning_rate

        self.weights = []
        self.biases = []
        self.moving_mean = []
        self.moving_var = []
        self.velocity_w = []
        self.velocity_b = []
        self.alpha = []  # for Leaky ReLU
        self.cache = {}  # Initialize cache to store intermediate layer outputs
        self.training = True
        self.build_network()

    def build_network(self):
        prev_depth = self.input_shape[2]
        prev_shape = self.input_shape[:2]  # (height, width)

        for i, depth in enumerate(self.depths):
            num_filters = self.filters[i]
            filter_size = self.filter_sizes[i]
            stride = 1  # Assuming stride=1 for simplicity
            padding = 0  # Assuming no padding (valid padding)

            # Calculate output dimensions after convolution
            out_h = (prev_shape[0] - filter_size + padding) // stride + 1
            out_w = (prev_shape[1] - filter_size + padding) // stride + 1

            self.weights.append(np.random.randn(filter_size, filter_size, prev_depth, num_filters) * 0.1)
            self.biases.append(np.zeros((1, 1, 1, num_filters)))
            self.velocity_w.append(np.zeros_like(self.weights[-1]))
            self.velocity_b.append(np.zeros_like(self.biases[-1]))

            if depth == 2:  # if it's a layer with batch normalization
                self.moving_mean.append(np.zeros((1, 1, 1, num_filters)))
                self.moving_var.append(np.ones((1, 1, 1, num_filters)))

            # Update prev_depth and prev_shape for next layer
            prev_depth = num_filters
            prev_shape = (out_h, out_w)  # Update height and width after conv/pool

    def leaky_relu(self, x, alpha=0.01):
        return np.where(x > 0, x, alpha * x)

    def softmax(self, x):
        exp_x = np.exp(x - np.max(x, axis=-1, keepdims=True))
        return exp_x / np.sum(exp_x, axis=-1, keepdims=True)

    def cross_entropy_loss(self, y_pred, y_true):
        m = y_true.shape[0]
        log_likelihood = -np.log(y_pred[np.arange(m), y_true.argmax(axis=-1)])
        loss = np.sum(log_likelihood) / m
        return loss

    def forward(self, x):
        self.cache = {}  # Reset cache at the start of each forward pass
        out = x
        for i, depth in enumerate(self.depths):
            W, b = self.weights[i], self.biases[i]
            out = self.conv2d(out, W, b)
            if depth == 2:
                out = self.batch_normalization(out, i)
            out = self.leaky_relu(out)
            self.cache[f'conv_{i}_out'] = out  # Save output of this layer to cache
            out = self.max_pooling(out)

            if i > 0:  # Residual connection logic
                prev_out = self.cache[f'conv_{i-1}_out']
                prev_out_h, prev_out_w = prev_out.shape[1:3]
                out_h, out_w = out.shape[1:3]
                if prev_out_h != out_h or prev_out_w != out_w or prev_out.shape[3] != out.shape[3]:
                    # Apply 1x1 convolution to match dimensions for residual connection
                    prev_out = self.conv2d(prev_out, self.weights[i], self.biases[i])  # 1x1 convolution for matching
                out += prev_out  # Add residual connection
        out = self.flatten(out)
        out = self.dropout(out)
        out = self.fc(out)
        return self.softmax(out)

    def conv2d(self, x, W, b):
        out_h = x.shape[1] - W.shape[0] + 1
        out_w = x.shape[2] - W.shape[1] + 1
        out = np.zeros((x.shape[0], out_h, out_w, W.shape[3]))
        
        for i in range(out_h):
            for j in range(out_w):
                out[:, i, j, :] = np.tensordot(x[:, i:i+W.shape[0], j:j+W.shape[1], :], W, axes=((1, 2, 3), (0, 1, 2))) + b
        return out

    def batch_normalization(self, x, layer_idx):
        gamma = np.ones_like(x[0, 0, 0, :])
        beta = np.zeros_like(x[0, 0, 0, :])

        if self.training:
            mean = np.mean(x, axis=(0, 1, 2), keepdims=True)
            var = np.var(x, axis=(0, 1, 2), keepdims=True)
            self.moving_mean[layer_idx] = self.moving_mean[layer_idx] * self.momentum + mean * (1 - self.momentum)
            self.moving_var[layer_idx] = self.moving_var[layer_idx] * self.momentum + var * (1 - self.momentum)
        else:
            mean, var = self.moving_mean[layer_idx], self.moving_var[layer_idx]
        
        x_hat = (x - mean) / np.sqrt(var + 1e-8)
        return gamma * x_hat + beta

    def max_pooling(self, x, pool_size=2, stride=2):
        out_h = (x.shape[1] - pool_size) // stride + 1
        out_w = (x.shape[2] - pool_size) // stride + 1
        out = np.zeros((x.shape[0], out_h, out_w, x.shape[3]))
        
        for i in range(out_h):
            for j in range(out_w):
                out[:, i, j, :] = np.max(x[:, i*stride:i*stride+pool_size, j*stride:j*stride+pool_size, :], axis=(1, 2))
        return out

    def flatten(self, x):
        return x.reshape(x.shape[0], -1)

    def dropout(self, x):
        if self.training:
            mask = (np.random.rand(*x.shape) > self.dropout_rate)
            return x * mask / (1 - self.dropout_rate)
        return x

    def fc(self, x):
        return np.dot(x, self.fc_weights) + self.fc_bias

    def backward(self, x, y):
        pass  # Backpropagation implementation goes here

    def update_parameters(self):
        pass  # Parameter updates (SGD + Momentum) goes here

    def train(self, X_train, y_train, epochs=10, batch_size=32, learning_rate=0.01, momentum=0.9):
        # Set the model to training mode
        self.training = True

        # Number of training samples
        num_samples = X_train.shape[0]

        for epoch in range(epochs):
            # Shuffle the training data for each epoch
            indices = np.random.permutation(num_samples)
            X_train_shuffled = X_train[indices]
            y_train_shuffled = y_train[indices]

            # Iterate over batches
            for i in range(0, num_samples, batch_size):
                # Create mini-batch
                X_batch = X_train_shuffled[i:i + batch_size]
                y_batch = y_train_shuffled[i:i + batch_size]

                # Forward pass: Compute the predictions
                out = self.forward(X_batch)

                # Compute loss (e.g., cross-entropy)
                loss = self.compute_loss(out, y_batch)
                
                # Backward pass: Compute gradients
                self.backward(X_batch, y_batch)

                # Update parameters (weights and biases) using gradient descent
                self.update_parameters(learning_rate, momentum)

                # Optionally print or log loss after every batch or epoch
                if i % (batch_size * 10) == 0:  # Print loss every 10 batches
                    print(f'Epoch {epoch+1}/{epochs}, Batch {i//batch_size+1}/{num_samples//batch_size}, Loss: {loss:.4f}')

            print(f'Epoch {epoch+1}/{epochs} complete.')

# Example synthetic data (random)
x_train = np.random.randn(50000, 32, 32, 3)  # 50,000 images of size 32x32 with 3 channels
y_train = np.random.randint(0, 10, size=(50000,))  # Random labels (0-9 for 10 classes)
# Convert labels to one-hot encoding
y_train = np.eye(10)[y_train]

# Example usage
input_shape = (32, 32, 3)  # Example input shape (height, width, channels)
num_classes = 10
filters = [32, 64, 128]
filter_sizes = [3, 3, 3]
depths = [1, 2, 1]  # 1 for conv, 2 for conv + batch norm
cnn = CNN(input_shape, num_classes, filters, filter_sizes, depths)
cnn.train(x_train, y_train, epochs=10, batch_size=32)
