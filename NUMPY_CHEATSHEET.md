# NumPy Cheat Sheet — Quick Lookup

> Quick syntax reference for NumPy fundamentals and the first ML exercises. See [NumPy Fundamentals](numpy_basics.md) for explanations, practice, and the video chapter links.

## Imports and creation

```python
import numpy as np

a = np.array([1, 2, 3])          # 1D array
m = np.array([[1, 2], [3, 4]]) # 2D array
np.arange(5)                     # [0 1 2 3 4]
np.arange(2, 10, 2)              # [2 4 6 8]
np.zeros((2, 3))                 # 2 rows, 3 columns of zeros
np.ones((2, 3))                  # 2 rows, 3 columns of ones
np.eye(3)                        # 3x3 identity matrix
```

## Properties and selection

| Need | Syntax | Result / meaning |
|---|---|---|
| Dimensions | `m.ndim` | `2` |
| Shape | `m.shape` | `(2, 2)` |
| Number of elements | `m.size` | `4` |
| Type | `m.dtype` | Integer dtype for this `m` |
| First row | `m[0, :]` | `[1 2]` |
| Second column | `m[:, 1]` | `[2 4]` |
| One value | `m[1, 0]` | `3` |
| Last row | `m[-1, :]` | `[3 4]` |

**Index rule:** `arr[row, column]`; both start at **0**.

**Slice rule:** `start:stop:step`; the **stop is not included**.

```python
a = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print(a[0:2, 1:3])    # [[2 3], [6 7]]: two rows x two columns
print(a[1:3, 0:2])    # [[5 6], [9 10]]
print(a[:, 2])        # [ 3  7 11]
```

## Arithmetic and broadcasting

```python
a = np.array([2, 4, 6])
b = np.array([1, 2, 3])

a + b     # [3 6 9]
a - b     # [1 2 3]
a * b     # [ 2  8 18] elementwise, NOT matrix multiplication
a / 2     # [1. 2. 3.]
a ** 2    # [ 4 16 36]
a + 5     # [7 9 11] scalar broadcasting

m = np.array([[1, 2, 3], [4, 5, 6]])
m + np.array([10, 20, 30])
# [[11 22 33]
#  [14 25 36]]
```

**Broadcasting:** Compare shapes from the right. Dimensions must match or one must be 1. `(2, 3) + (3,)` works; `(2, 3) + (2,)` fails.

## Aggregates and axes

```python
m = np.array([[2, 4, 6], [8, 10, 12]])

m.sum()           # 42
m.mean()          # 7.0
m.min(), m.max()  # (2, 12)
m.sum(axis=0)     # [10 14 18] per COLUMN
m.sum(axis=1)     # [12 30]    per ROW
m.mean(axis=0)    # mean of each column
```

**Memory trick:** `axis=0` reduces rows, leaving columns; `axis=1` reduces columns, leaving rows.

## Boolean filtering

```python
a = np.array([5, 12, 18, 7, 24, 9, 30])
a > 10                        # a Boolean mask
a[a > 10]                     # [12 18 24 30]
a[(a > 10) & (a % 2 == 0)]   # [12 18 24 30]
a[(a < 10) | (a > 25)]       # [ 5  7  9 30]
```

`&` = AND, `|` = OR, `~` = NOT. Use parentheses around each comparison; don't use Python `and`/`or` for array masks. Boolean selection of matching entries from a 2D array often yields a 1D array.

## Reshape

```python
a = np.arange(12)       # 12 elements, shape (12,)
m = a.reshape(3, 4)     # 3 rows, 4 columns
m.shape                 # (3, 4)
m[2, 1]                 # 9 (third row, second column)
a.reshape(2, 6)         # also works
a.reshape(3, -1)        # infer 4 columns
# a.reshape(5, 3)       # ValueError: 12 != 15 elements
```

## Random numbers

```python
rng = np.random.default_rng(42)         # reusable seeded generator
rng.integers(1, 10, size=(2, 3))       # random ints 1..9; shape (2, 3)
rng.random((2, 3))                      # floats in [0, 1), shape (2, 3)

# Older code may use:
np.random.seed(42)
np.random.randint(1, 10, size=(2, 3))
```

The upper integer limit is **excluded**. Do not expect the modern and legacy APIs to output the same sequence for the same seed.

## ML bridge: matrix-vector multiplication

```python
X = np.array([[1., 2.], [3., 4.]])  # samples x features = (2, 2)
w = np.array([0.5, 2.0])           # two feature weights
b = 1.0

X @ w + b                           # [5.5 10.5]
X.T                                 # transpose; shape (2, 2)
np.dot(w, np.array([1., 2.]))       # 4.5
```

**Do not mix up:** `*` = elementwise multiply; `@` = matrix/vector multiplication. We will work through the mathematics next.

## Common mistakes from practice

| Mistake | Fix |
|---|---|
| Read `a[0:2, 1:3]` as selecting just one number | It selects rows `0,1` and columns `1,2`: 4 numbers |
| Count a row/column from 1 | Both indices start at 0 |
| Expect `a[a > 10]` to return only one number | It returns **all** matching values |
| Include the stop of a slice | Slice stop is excluded |
| Confuse `axis=0` and `axis=1` | Axis 0 → per column; axis 1 → per row |
| Use `and` for arrays | Use `&`, with parentheses |
| Expect `reshape` to change the element count | Product of new dimensions must match `size` |

## 30-second self-test

```python
a = np.arange(12).reshape(3, 4)
print(a[1:3, 1:3])
print(a.sum(axis=0))
print(a[a > 8])
```

Predicted results: `[[5 6], [9 10]]`, `[12 15 18 21]`, `[ 9 10 11]`. Try to predict them without running Python.

**Next:** vectors, dot products, matrix multiplication, a neuron forward pass. The goal is to use NumPy in ML, not only memorize commands.


## Practiced matrix operations (15 October 2026)

Read the [worked guide](NUMPY_MATRICES.md) for the step-by-step maths and the [run-ready checks](examples/matrix_operations.py). The [array shape diagram](assets/numpy-matrix-shapes.svg) shows why a 1D vector and a column vector have different NumPy shapes.

~~~python
import numpy as np
A = np.array([[1, 2, 3], [4, 5, 6]])  # (2, 3)
B = np.array([[7, 8], [9, 10], [11, 12]])  # (3, 2)
C = A @ B
print(C)        # [[58 64], [139 154]]
print(C.shape)  # (2, 2)
print(A.T.shape) # (3, 2)
~~~

**NumPy details that matter in neural networks:**
- x = np.array([2, -1]) has shape **(2,)**; x[:, None] has shape **(2,1)**.
- For samples stored in **columns**, W:(3,2) @ X:(2,s) + b:(3,1) produces **(3,s)**.
- Use b = np.array([[1], [2], [-3]]) instead of shape (3,) for this column-oriented convention.
- np.maximum(0, Z) applies ReLU **elementwise** and keeps Z's shape.

The full math derivation belongs to [ML-MATH](https://github.com/Vaibh37/ML-MATH/tree/main/linear-algebra/matrices); the forward-pass explanation belongs to [Neural-Network](https://github.com/Vaibh37/Neural-Network/blob/main/notes/04-hidden-layer-forward-pass.md).
