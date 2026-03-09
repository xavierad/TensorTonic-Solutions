import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    x = np.array(x)
    return np.divide(
        1, 
        1 + np.exp(-x)
    )