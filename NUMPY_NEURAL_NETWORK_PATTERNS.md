# NumPy Patterns Used in the XOR Neural Network

**Learning checkpoint: 18 October 2026.** These are the NumPy operations used while implementing [the 2 → 3 → 1 XOR network](https://github.com/Vaibh37/Neural-Network/blob/main/examples/xor_network.py), not a replacement for its mathematical derivations.

## 1. Array shapes: samples vs neurons

```python
X = np.array([[0.,0.],[0.,1.],[1.,0.],[1.,1.]])
y = np.array([[0.],[1.],[1.],[0.]])

assert X.shape == (4, 2)  # 4 examples, 2 features
assert y.shape == (4, 1)  # 4 target values, each kept as a column
```

For a 2 → 3 → 1 network:

| Parameter | Shape |
| --- | --- |
| `W_h` | `(2,3)` |
| `b_h` | `(3,)` |
| `W_o` | `(3,1)` |
| `b_o` | `(1,)` |

## 2. `@` versus `*`

- `@`: **matrix multiplication**, matches inner dimensions.
- `*`: **elementwise** multiplication (with broadcasting when shapes permit).

```python
z_h = X @ W_h + b_h        # (4,2) @ (2,3) -> (4,3)
h = np.maximum(0, z_h)     # elementwise ReLU
z_o = h @ W_o + b_o        # (4,3) @ (3,1) -> (4,1)
```

`b_h` is added to every row of `X @ W_h` through broadcasting. A common error is to add a bias of the wrong shape.

## 3. ReLU derivative with a Boolean mask

```python
dh_dhz = (z_h > 0).astype(float)
```

- `z_h > 0`: elementwise comparisons.
- `.astype(float)`: converts `True → 1.0` and `False → 0.0`.
- This uses derivative 0 at `z_h == 0`, where ReLU is mathematically nondifferentiable.
- `==` compares values; `=` assigns variables.

Do **not** write `if z_h > 0` for a whole NumPy array to create this mask; NumPy needs an elementwise operation.

## 4. Transpose and batch gradients

```python
dW_o = h.T @ dl_dz_o   # (3,4) @ (4,1) -> (3,1)
dl_dh = dl_dz_o @ W_o.T  # (4,1) @ (1,3) -> (4,3)
dW_h = X.T @ dl_dzh    # (2,4) @ (4,3) -> (2,3)
```

The transpose `.T` changes axis order; a matrix `(4,3)` becomes `(3,4)`.

**Critical detail:** use the **weights** `W_o.T` to backpropagate, not the **weight gradients** `dW_o.T`.

## 5. `np.sum(axis=0)` for bias gradients

```python
db_o = np.sum(dl_dz_o, axis=0)  # (1,)
db_h = np.sum(dl_dzh, axis=0)  # (3,)
```

`axis=0` sums **down the sample rows**, retaining one gradient for each output feature / neuron.

The MSE derivative already contains `2/len(X)`, so do not calculate another sample mean of these output gradients.

## 6. Sigmoid, loss, and classification

```python
a_o = 1 / (1 + np.exp(-z_o))       # Sigmoid
loss = np.mean((a_o - y) ** 2)    # Mean squared error
predictions = (a_o >= 0.5).astype(int)  # Threshold to classes 0/1
```

MSE = the **mean of the squared errors**, not the square of the mean error.

## 7. Seeded random initialization

```python
rng = np.random.default_rng(42)
W_h = rng.normal(0, 0.5, size=(2, 3))
b_h = np.zeros(3)
W_o = rng.normal(0, 0.5, size=(3, 1))
b_o = np.zeros(1)
```

- The correct method is **`np.random.default_rng()`**, not `np.random.default.rng()`.
- The normal-distribution method is **`rng.normal()`**, not `np.normal()`.
- A random seed allows reproducibility. Changing the seed can change convergence.

## 8. Epoch loop and printing

```python
epochs = 5000
for epoch in range(epochs):
    # Always do the forward pass, loss, backprop and update
    if epoch % 500 == 0:
        print(f"Epoch {epoch} | Loss: {loss:.6f}")
```

- `epoch` exists **inside** the `for` loop.
- `epochs` is the total number of training passes.
- `epoch % 500 == 0` controls printing, **not** whether training occurs.
- Initialize weights **before** the loop or they will reset every time.

## 9. After updating parameters, forward again

Changing `W_h`, `b_h`, `W_o`, and `b_o` does not automatically change the previously computed prediction array. To evaluate the final network, recalculate `z_h`, `h`, `z_o` and `a_o` with the new parameters.

### Related math and diagrams

- [Full XOR model implementation](https://github.com/Vaibh37/Neural-Network/blob/main/examples/xor_network.py)
- [Forward/backprop lessons 11–16](https://github.com/Vaibh37/Neural-Network/tree/main/notes)
- [12 high-resolution illustrated diagrams](https://github.com/Vaibh37/Neural-Network/tree/main/assets/xor)
- [Derivation of all multilayer gradients](https://github.com/Vaibh37/ML-MATH/blob/main/calculus/04-xor-backpropagation-chain-rule.md)
