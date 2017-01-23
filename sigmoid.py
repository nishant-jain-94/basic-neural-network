import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x, deriv=False):
	"""Maps any value to a value between 0 and 1 
	
	Inputs:
	x - value which is to be mapped between 0 and 1
	dervi - if true returns the derivative of the sigmoid function

	"""
	if(deriv == True):
		return x * (1-x)
	return 1 / (1 + np.exp(-x))

X = np.arange(-6, 6, 1)
y = sigmoid(X, deriv=True)
plt.plot(X, y)
plt.show();