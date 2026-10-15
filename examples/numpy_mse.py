"""NumPy loss arithmetic cheat sheet: predictions supplied, no model training.

Run: python examples/numpy_mse.py
Requires: numpy
"""

import numpy as np

# The independently implemented 15 Oct practice problem:
y_true = np.array([10, 20, 30, 40])
y_pred = np.array([12, 18, 33, 37])

error = y_true - y_pred
squared = error ** 2
mse = np.mean(squared)

print("error:", error)      # [-2  2 -3  3]
print("squared:", squared)  # [4 4 9 9]
print("MSE:", mse)          # 6.5

assert error.shape == (4,)
assert np.array_equal(squared, [4, 4, 9, 9])
assert np.isclose(mse, 6.5)

# Subtraction direction does not change MSE (because the errors are squared).
assert np.isclose(np.mean((y_pred - y_true) ** 2), mse)
