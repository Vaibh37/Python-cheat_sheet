"""NumPy matrix essentials, broadcasting and an untrained ReLU forward pass."""
import numpy as np


def main() -> None:
    A = np.array([[1, 2, 3], [4, 5, 6]])
    B = np.array([[7, 8], [9, 10], [11, 12]])
    C = A @ B
    assert C.shape == (2, 2)
    assert C.tolist() == [[58, 64], [139, 154]]
    assert A.T.shape == (3, 2)

    X = np.array([[5, 10], [15, 20], [25, 30]])
    row = np.array([[2, 3]])
    assert (X + row).tolist() == [[7, 13], [17, 23], [27, 33]]

    WX = np.array([[19, 22], [43, 50]])
    bias = np.array([[1], [2]])
    assert (WX + bias).tolist() == [[20, 23], [45, 52]]

    W = np.array([[2, 1], [-1, 3], [1, -2]])
    x = np.array([[2], [-1]])
    b = np.array([[1], [2], [-3]])
    Z = W @ x + b
    output = np.maximum(0, Z)
    assert output.tolist() == [[4], [0], [1]]
    assert output.shape == (3, 1)
    print("Matrix product:", C.tolist(), "shape:", C.shape)
    print("Dense ReLU forward pass:", output.ravel().tolist(), "shape:", output.shape)
    print("All checks passed. This code does not train a model.")


if __name__ == "__main__":
    main()
