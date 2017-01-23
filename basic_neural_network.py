import numpy as np

class Neural_Network(object):
	def __init__(self):
		# Define HyperParameters
		self.inputLayerSize = 2
		self.outputLayerSize = 1
		self.hiddenLayerSize = 3
		#Weights Parameters
		self.W1 = np.random.randn(self.inputLayerSize, self.hiddenLayerSize)
		self.W2 = np.random.randn(self.hiddenLayerSize, self.outputLayerSize)

	def forward(self, X):
		self.z2 = np.dot(X, self.W1)
		self.a2 = self.sigmoid(self.z2)
		self.z3 = np.dot(self.a2, self.W2)
		yHat = self.sigmoid(self.z3)
		return yHat

	def sigmoid(self, z):
		# Apply sigmoid activation function
		return 1/(1+np.exp(-z))


X = np.array([[3, 5],
	 [5, 1],
	 [10, 2]], dtype=float)
y = np.array([[75], [82], [93]], dtype=float)

X = X / np.amax(X, axis=0)
y = y / np.amax(y)

NN = Neural_Network()
yHat = NN.forward(X)
print(yHat)