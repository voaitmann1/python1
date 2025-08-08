import numpy as np

class NeuralNetwork:
    def __init__(self, layer_sizes):
        self.num_layers = len(layer_sizes)
        self.layer_sizes = layer_sizes
        self.weights = [np.random.randn(layer_sizes[i+1], layer_sizes[i]) for i in range(self.num_layers-1)]
        self.biases = [np.random.randn(layer_sizes[i+1], 1) for i in range(self.num_layers-1)]

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def feed_forward(self, inputs):
        activations = inputs
        for i in range(self.num_layers-1):
            weighted_inputs = np.dot(self.weights[i], activations) + self.biases[i]
            activations = self.sigmoid(weighted_inputs)
        return activations

    def back_propagation(self, inputs, outputs, learning_rate):
        # прямой проход
        activations = [inputs]
        weighted_inputs = []
        for i in range(self.num_layers-1):
            weighted_input = np.dot(self.weights[i], activations[i]) + self.biases[i]
            weighted_inputs.append(weighted_input)
            activation = self.sigmoid(weighted_input)
            activations.append(activation)

        # вычисление ошибок на выходном слое
        output_errors = outputs - activations[-1]

        # обратный проход
        for i in range(self.num_layers-2, -1, -1):
            errors = np.dot(self.weights[i].T, output_errors)
            output_errors = errors * activations[i+1] * (1 - activations[i+1])
            delta = np.dot(output_errors, activations[i].T)
            self.weights[i] += learning_rate * delta
            self.biases[i] += learning_rate * output_errors

# пример использования класса NeuralNetwork
nn = NeuralNetwork([2, 3, 1]) # сеть с одним входным слоем (2 нейрона), одним скрытым слоем (3 нейрона) и одним выходным слоем (1 нейрон)
inputs = np.array([[0], [0]])
outputs = np.array([[0]])
for i in range(10000):
    nn.back_propagation(inputs, outputs, 0.1)
print(nn.feed_forward(np.array([[0], [1]]))) # должно быть близко к 0
print(nn.feed_forward(np.array([[1], [0]])))#) # должно быть близко к 0
print(nn.feed_forward(np.array([[1], [1]])))#) # должно быть близко к 1
