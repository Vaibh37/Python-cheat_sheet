"""Practice NumPy vectorization, mean and Boolean-to-float conversion.

Run: python examples/numpy_vectorization_and_masks.py
This is NumPy syntax practice; the training loop lives in Neural-Network.
"""
import numpy as np

x = np.array([1.0, 2.0, 3.0, 4.0])
y = np.array([5.0, 10.0, 15.0, 20.0])

w = 3.0
b = 1.0
pred_y = w * x + b                 # [4., 7., 10., 13.]
errors = pred_y - y                # [-1., -3., -5., -7.]
squared_errors = errors ** 2       # [1., 9., 25., 49.]
mse = np.mean(squared_errors)      # 21.0

# Multiply elementwise FIRST, then take the mean:
dw = 2 * np.mean(errors * x)       # -25.0
db = 2 * np.mean(errors)           # -8.0

# ReLU derivative as a NumPy mask.
z = np.array([-3.0, 2.0, 0.0, 5.0])
positive_mask = z > 0              # [False, True, False, True]
relu_prime = positive_mask.astype(float)  # [0., 1., 0., 1.]

assert pred_y.shape == (4,)
assert np.isclose(mse, 21.0)
assert np.isclose(dw, -25.0)
assert np.isclose(db, -8.0)
assert np.array_equal(relu_prime, [0., 1., 0., 1.])
print("Predictions:", pred_y)
print("MSE:", mse, "dw:", dw, "db:", db)
print("Boolean mask:", positive_mask)
print("ReLU derivative:", relu_prime)
print("Checks passed.")
