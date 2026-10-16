# NumPy Fundamentals for AI/ML

> **Study status (14 October 2026):** Finished the eight chapters of the [NumPy tutorial](https://www.youtube.com/watch?v=VXU4LSAQDSc) and completed a short prediction-based revision. This records material studied, **not mastery**. Revisit 2D slices and indices because they caused errors during practice.
>
> **Use this page for explanation and worked examples.** For fast syntax lookup use [NUMPY_CHEATSHEET.md](NUMPY_CHEATSHEET.md). For basic Python syntax use [CHEATSHEET.md](CHEATSHEET.md).

## Learning outcomes

After this lesson, you should be able to create and inspect arrays, select rows and columns, perform elementwise operations, broadcast compatible shapes, reduce arrays with `axis`, filter by conditions, generate random values, and reshape a 1D array into a matrix.

## Setup

```powershell
python -m pip install numpy
```

```python
import numpy as np
print(np.__version__)  # installed version
```

Use a project virtual environment when practical.

## Tutorial chapters

The boxes mean **watched and revised**; harder topics still need independent practice.

| Studied | Chapter | Focus |
|---|---|---|
| [x] | [00:00 Introduction](https://www.youtube.com/watch?v=VXU4LSAQDSc&t=0s) | `ndarray` vs Python lists |
| [x] | [05:07 Multidimensional arrays](https://www.youtube.com/watch?v=VXU4LSAQDSc&t=307s) | `shape`, `ndim`, `size`, indexing |
| [x] | [12:54 Slicing](https://www.youtube.com/watch?v=VXU4LSAQDSc&t=774s) | Start inclusive, stop exclusive |
| [x] | [24:04 Arithmetic](https://www.youtube.com/watch?v=VXU4LSAQDSc&t=1444s) | Elementwise operations |
| [x] | [33:21 Broadcasting](https://www.youtube.com/watch?v=VXU4LSAQDSc&t=2001s) | Compatible shapes |
| [x] | [39:42 Aggregate functions](https://www.youtube.com/watch?v=VXU4LSAQDSc&t=2382s) | `axis=0` vs `axis=1` |
| [x] | [43:48 Filtering](https://www.youtube.com/watch?v=VXU4LSAQDSc&t=2628s) | Boolean masks |
| [x] | [52:03 Random numbers](https://www.youtube.com/watch?v=VXU4LSAQDSc&t=3123s) | Random generators and reproducibility |

---

## 1. Why NumPy?

A Python list is a general-purpose container. A NumPy `ndarray` stores data in a multidimensional array with a common data type and supports efficient vectorized numerical operations.

```python
values = [1, 2, 3]
print(values * 2)  # [1, 2, 3, 1, 2, 3] (list repeats)

arr = np.array([1, 2, 3])
print(arr * 2)     # [2 4 6] (each element doubles)
print(arr + 5)     # [6 7 8]
print(arr.dtype)   # usually int64 or int32, platform-dependent
```

Do not assume NumPy always runs faster for every tiny operation. It is especially useful for large numerical arrays and batch calculations.

## 2. Dimensions, shape, size and indexing

```python
vector = np.array([10, 20, 30])    # shape (3,), ndim 1
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])                                  # shape (2, 3), ndim 2

print(matrix.shape)  # (2, 3): rows, columns
print(matrix.ndim)   # 2: number of axes
print(matrix.size)   # 6: number of values
print(matrix[1, 2])  # 60: row index 1, column index 2
print(matrix[1])     # [40 50 60]: complete second row
```

**Zero-based indexing:** the first element is at index 0. For a 2D NumPy array, use `matrix[row, column]`. A nested Python list instead normally uses `items[row][column]`.

| Shape | Meaning |
|---|---|
| `(4,)` | 1D array with four elements |
| `(2, 3)` | 2D array with two rows and three columns |
| `(5, 2, 3)` | 3D array: five groups of 2-by-3 values |
| `(2, 3)` vs `(3, 2)` | Different shapes even though both have six elements |

## 3. Slicing: the crucial rule

`start:stop:step` **includes start but excludes stop**. In `matrix[rows, columns]`, both selections happen at the same time.

```python
a = np.array([
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12]
])

print(a[0:2, 1:3])
# [[2 3]
#  [6 7]]

print(a[1:3, 0:2])
# [[ 5  6]
#  [ 9 10]]

print(a[:, 1])    # [ 2  6 10]  all rows, column index 1
print(a[0, :])    # [1 2 3 4]   first row, all columns
print(a[::2, :])  # first and third row
```

### How to read `a[0:2, 1:3]`

1. `0:2` means row indices `0` and `1`.
2. `1:3` means column indices `1` and `2`.
3. Take the intersection: **four cells**, not just one cell.

**What went wrong in today's drill:** mentally focusing on the last value `12` ignored the other cells selected by the two slices. Trace **all selected row indices**, then **all selected column indices** before you calculate.

Many ordinary NumPy slices are **views** into the original data:

```python
a = np.array([10, 20, 30])
piece = a[0:2]
piece[0] = 99
print(a)                   # [99 20 30]

independent = a[0:2].copy()
independent[0] = 0
print(a)                   # [99 20 30]
```

## 4. Arithmetic is elementwise

```python
x = np.array([2, 4, 6])
y = np.array([1, 2, 3])

print(x + y)   # [3 6 9]
print(x - y)   # [1 2 3]
print(x * y)   # [ 2  8 18]
print(x / 2)   # [1. 2. 3.]
print(x ** 2)  # [ 4 16 36]
```

**Important:** `x * y` is elementwise multiplication, **not** matrix multiplication. Use `@` or `np.matmul` for matrix multiplication with compatible shapes; this is our next maths lesson.

## 5. Broadcasting

Broadcasting means NumPy can apply an operation between arrays with compatible shapes without manually repeating one array.

```python
scores = np.array([
    [1, 2, 3],
    [4, 5, 6]
])                               # shape (2, 3)
bonus = np.array([10, 20, 30])  # shape (3,)

print(scores + bonus)
# [[11 22 33]
#  [14 25 36]]
```

Compare shape dimensions **from the right**. Two dimensions are compatible if they match or if one is `1`. Missing leading dimensions behave like `1`.

- `(2, 3) + (3,)` works: `(3,)` acts like `(1, 3)`.
- `(2, 3) + (2, 1)` works: one value can be added per row.
- `(2, 3) + (2,)` fails: trailing dimensions `3` and `2` do not match.

```python
a = np.array([[1, 2, 3], [4, 5, 6]])
row_offsets = np.array([[10], [20]])  # shape (2, 1)
print(a + row_offsets)
# [[11 12 13]
#  [24 25 26]]
```

A scalar such as `a + 5` broadcasts to every element.

## 6. Aggregates and axes

An aggregation reduces many values into summaries.

```python
a = np.array([
    [2, 4, 6],
    [8, 10, 12]
])

print(a.sum())         # 42
print(a.mean())        # 7.0
print(a.min())         # 2
print(a.max())         # 12
print(a.sum(axis=0))   # [10 14 18] -> one sum per column
print(a.sum(axis=1))   # [12 30] -> one sum per row
```

**Remember the shape:** for a matrix of shape `(2, 3)`, `sum(axis=0)` produces shape `(3,)`, while `sum(axis=1)` produces shape `(2,)`. The axis specified is the one **reduced**.

For ML data `X` with shape `(samples, features)`, `X.mean(axis=0)` computes the mean of each feature across the samples.

## 7. Boolean masks and filtering

Comparisons produce Boolean arrays. Index with a mask to keep **every** matching element.

```python
a = np.array([5, 12, 18, 7, 24, 9, 30])

mask = (a > 10) & (a % 2 == 0)
print(mask)     # [False  True  True False  True False  True]
print(a[mask])  # [12 18 24 30]
```

- `&` = elementwise AND; `|` = OR; `~` = NOT.
- Put **each comparison in parentheses**: `(a > 10) & (a < 20)`.
- Do **not** use Python's `and` or `or` for elementwise array masks.

### Today's combined challenge, correctly traced

```python
a = np.array([
    [2, 4, 6],
    [8, 10, 12],
    [14, 16, 18]
])

selected = a[0:2, 1:3]  # [[ 4  6], [10 12]]
plus_five = selected + 5
# [[ 9 11]
#  [15 17]]

result = plus_five[plus_five > 10]
print(result)            # [11 15 17]
print(result.shape)      # (3,)
```

In this example, Boolean indexing extracts the matching entries as a **1D array**, even though the original input was 2D. It is not restricted to the last value or last row.

## 8. Random numbers and reproducibility

Use the modern generator API for new code:

```python
rng = np.random.default_rng(42)   # seed for reproducible experiments
ids = rng.integers(1, 10, size=(2, 3))
print(ids.shape)                  # (2, 3)
# All sampled values are integers from 1 to 9 (10 is excluded).
```

You may also encounter the older global random API:

```python
np.random.seed(42)
old_style = np.random.randint(1, 10, size=(2, 3))
```

The two random APIs do **not** necessarily generate identical sequences from the same seed. A seed makes a chosen generator reproducible for a fixed environment; it does not make random values predictable by hand.

## 9. Extra lesson from today's practice: reshape

`reshape` changes the arrangement but **does not add or remove elements**.

```python
a = np.arange(12)      # [0 1 2 ... 11], shape (12,)
b = a.reshape(3, 4)    # 3 rows, 4 columns

print(b)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(b.shape)         # (3, 4)
print(b[2, 1])         # 9
print(b[1, 3])         # 7
```

For `b[2, 1]`: third row is `[8, 9, 10, 11]`, second column is `9`. **Count both indices from zero.**

- `a.reshape(2, 6)` also works (12 elements).
- `a.reshape(5, 3)` fails (requires 15 elements).
- `a.reshape(3, -1)` infers 4 columns here.

A reshape may return a view or a copy depending on layout. Do not assume it always creates an independent array.

## 10. Where NumPy meets machine learning

Usually an ML feature matrix is `X` with shape `(number_of_samples, number_of_features)`. Weights `w` have one entry per feature.

```python
X = np.array([
    [1.0, 2.0],
    [3.0, 4.0],
    [5.0, 6.0]
])                           # 3 samples, 2 features

w = np.array([0.5, 2.0])    # one weight per feature
b = 1.0

predictions = X @ w + b
print(predictions)          # [ 5.5 10.5 15.5]
print(predictions.shape)    # (3,)
```

This demonstrates **matrix-vector multiplication plus a bias**, a core calculation in a linear model and in neural networks. We will study the maths behind `@` in the vectors/matrices lessons.

## 11. Common mistakes and fixes

| Mistake | Correct mental model |
|---|---|
| Think `0:2` includes index 2 | Stop index is excluded: indices 0, 1 |
| Treat `a[0:2, 1:3]` as one cell | Rows 0–1 **and** columns 1–2 form a 2-by-2 block |
| Read `a[2, 1]` as second row, first column | Both indices are zero-based: third row, second column |
| Assume Boolean filtering returns one value | It returns all matching values |
| Confuse `axis=0` and `axis=1` | Axis 0 reduces rows; axis 1 reduces columns |
| Assume `a * b` is matrix multiplication | `*` is elementwise; `@` handles matmul |
| Reshape into an incompatible number of cells | Total element count must stay unchanged |
| Use `and` for array filters | Use `&` with parenthesized comparisons |
| Assume random upper bound is included | `integers(low, high)` excludes `high` |

## 12. Practice tasks (try before checking answers)

1. Create a `2 x 3` array of integers and print `shape`, `ndim`, and `size`.
2. For `a = np.arange(12).reshape(3, 4)`, predict `a[1:3, 1:3]` and `a[2, 1]`.
3. Add `[10, 20, 30]` to each row of `[[1, 2, 3], [4, 5, 6]]`.
4. For the same 2D array, calculate `sum(axis=0)` and `sum(axis=1)`.
5. Create `np.arange(1, 11)`. Keep only the values that are greater than 4 and even.
6. Create six reproducible random integers between 0 and 9 inclusive using `default_rng`, then reshape the result to `(2, 3)`.

<details>
<summary>Check answers only after attempting</summary>

```python
import numpy as np

# 1
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape, a.ndim, a.size)       # (2, 3) 2 6

# 2
a = np.arange(12).reshape(3, 4)
print(a[1:3, 1:3])                  # [[ 5  6], [ 9 10]]
print(a[2, 1])                     # 9

# 3
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a + np.array([10, 20, 30]))
# [[11 22 33], [14 25 36]]

# 4
print(a.sum(axis=0))               # [5 7 9]
print(a.sum(axis=1))               # [6 15]

# 5
a = np.arange(1, 11)
print(a[(a > 4) & (a % 2 == 0)])  # [ 6  8 10]

# 6
rng = np.random.default_rng(42)
a = rng.integers(0, 10, size=6).reshape(2, 3)
print(a.shape)                     # (2, 3)
```
</details>

## Next learning checkpoint

- [x] Watch/revise the eight NumPy video chapters
- [x] Practise array properties, aggregates, filtering and random range questions
- [x] Learn basic `reshape` after the revision surfaced the gap
- [ ] Independently solve two mixed slicing/indexing problems without counting slips
- [ ] Independently write a vector dot product and matrix multiplication in NumPy
- [x] Apply NumPy arrays to a single-neuron forward pass and vectorize four predictions

**Learning rule:** Predict the result on paper → run the code → explain the shape → fix your own mistake. Studied is not the same as mastered.


## 13. Practiced 16 October: vectorized batches, mean and Boolean masks

Four independent sample inputs can be stored in a 1D NumPy array. One shared linear neuron predicts all four without a loop, because scalar multiplication and addition broadcast over every element.

~~~python
x = np.array([1., 2., 3., 4.])
y = np.array([5., 10., 15., 20.])
pred = 3.0 * x + 1.0       # [4., 7., 10., 13.]
mse = np.mean((pred-y)**2)  # 21.0
dw = 2 * np.mean((pred-y)*x)  # -25.0
db = 2 * np.mean(pred-y)     # -8.0
~~~

**Mistakes encountered and corrected:**
- Average errors **after squaring** to obtain MSE.
- Average each sample's **error times its input** to get dw; averaging errors first is not equivalent.
- Gradients dw and db are **information used to update parameters**, not another neuron's weight.
- Each epoch recomputes fresh predictions and fresh gradients from updated parameters.

**New method, with explanation:**

~~~python
z = np.array([-3., 2., 0., 5.])
comparison = z > 0          # Boolean array
derivative = comparison.astype(float)   # True -> 1.0, False -> 0.0
~~~

The **.astype(float)** method converts the array dtype and elements into floats. Here it gives [0.,1.,0.,1.]. A standard Python if cannot directly test an entire multi-element Boolean array as a single condition.

The complete five-epoch parameter update implementation belongs to [Neural-Network/examples/train_batch_neuron_numpy.py](https://github.com/Vaibh37/Neural-Network/blob/main/examples/train_batch_neuron_numpy.py). This Python file records syntax, not separate ML theory.
