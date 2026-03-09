import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    x = np.asarray(x, dtype=float)
    return np.divide(
        1, 
        1 + np.exp(-x)
    )