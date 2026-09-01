import numpy as np

X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

Y = np.array([
    [0],
    [1],
    [1],
    [0]
])


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

np.random.seed(1)

input_neurons = 2
hidden_neurons = 4
output_neurons = 1

W1 = np.random.rand(input_neurons, hidden_neurons)
b1 = np.zeros((1, hidden_neurons))

W2 = np.random.rand(hidden_neurons, output_neurons)
b2 = np.zeros((1, output_neurons))



learning_rate = 0.5

for epoch in range(10000):

    
    hidden_input = np.dot(X, W1) + b1
    hidden_output = sigmoid(hidden_input)

    output_input = np.dot(hidden_output, W2) + b2
    output = sigmoid(output_input)

    
    error = Y - output

    
    output_delta = error * sigmoid_derivative(output)

    hidden_error = np.dot(output_delta, W2.T)
    hidden_delta = hidden_error * sigmoid_derivative(hidden_output)

    W2 += np.dot(hidden_output.T, output_delta) * learning_rate
    b2 += np.sum(output_delta, axis=0, keepdims=True) * learning_rate

    W1 += np.dot(X.T, hidden_delta) * learning_rate
    b1 += np.sum(hidden_delta, axis=0, keepdims=True) * learning_rate

print("Feed Forward Neural Network Output:")
print("------------------------------------")

for i in range(len(X)):

    hidden_output = sigmoid(np.dot(X[i], W1) + b1)
    output = sigmoid(np.dot(hidden_output, W2) + b2)

    print(
        "Input:", X[i],
        "Predicted Output:", round(float(output[0][0]), 3)
    )