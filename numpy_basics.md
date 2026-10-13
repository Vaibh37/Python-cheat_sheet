# NumPy for AI/ML — video companion

> **Status:** Starting. This is a reference and progress tracker, not a claim that the video chapters are complete.
>
> Video: [NumPy tutorial](https://www.youtube.com/watch?v=VXU4LSAQDSc)
>
> Refresh first: [functions, slicing, and 2D lists](CHEATSHEET.md#14-pre-numpy-refresh--functions-slicing-2d-lists).

## Setup

```powershell
python -m pip install numpy
```

```python
import numpy as np
print(np.__version__)
```

## Chapters and checkpoints

Work through the chapters in this order. Tick a box only after you can write a small example without copying.

| Done | Start | Topic | Main goal |
|---|---|---|---|
| [ ] | [00:00:00](https://www.youtube.com/watch?v=VXU4LSAQDSc&t=0s) | Introduction | Create a NumPy array; compare it to a Python list |
| [ ] | [00:05:07](https://www.youtube.com/watch?v=VXU4LSAQDSc&t=307s) | Multidimensional arrays | Understand `ndim`, `shape`, `size`, and row/column indices |
| [ ] | [00:12:54](https://www.youtube.com/watch?v=VXU4LSAQDSc&t=774s) | Slicing | Select elements, rows, and columns |
| [ ] | [00:24:04](https://www.youtube.com/watch?v=VXU4LSAQDSc&t=1444s) | Arithmetic | Use elementwise operations |
| [ ] | [00:33:21](https://www.youtube.com/watch?v=VXU4LSAQDSc&t=2001s) | Broadcasting | Combine compatible shapes |
| [ ] | [00:39:42](https://www.youtube.com/watch?v=VXU4LSAQDSc&t=2382s) | Aggregate functions | Use `sum`, `mean`, and axes |
| [ ] | [00:43:48](https://www.youtube.com/watch?v=VXU4LSAQDSc&t=2628s) | Filtering | Build boolean masks |
| [ ] | [00:52:03](https://www.youtube.com/watch?v=VXU4LSAQDSc&t=3123s) | Random numbers | Use `np.random.default_rng()` |

## 1. Arrays vs Python lists

```python
import numpy as np

values = [1, 2, 3]
print(values * 2)                  # [1, 2, 3, 1, 2, 3]

arr = np.array([1, 2, 3])
print(arr * 2)                     # [2 4 6]
print(arr + 3)                     # [4 5 6]
```

NumPy applies these operations **element by element**. Ordinary Python list multiplication by an integer **repeats** the list.

## 2. Multidimensional arrays

```python
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

print(matrix.ndim)                 # 2 dimensions
print(matrix.shape)                # (2, 3): 2 rows, 3 columns
print(matrix.size)                 # 6 elements
print(matrix[1, 2])                # 6
```

Python nested lists use `matrix[1][2]`; NumPy arrays also support `matrix[1, 2]`.

## 3. Slicing

Format: `start:stop:step`. **Stop is excluded.** Indices start at 0.

```python
arr = np.array([10, 20, 30, 40, 50])
print(arr[1:3])                    # [20 30]
print(arr[::2])                    # [10 30 50]
print(arr[::-1])                   # [50 40 30 20 10]

matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])
print(matrix[:, 1])                # [2 5]: all rows, column 1
print(matrix[0, :])                # [1 2 3]: row 0
```

Unlike a list slice, many NumPy slices are **views**: changing them can change the original array. Use `.copy()` for an independent copy when needed.

## 4. Arithmetic

```python
a = np.array([2, 4, 6])
b = np.array([1, 2, 3])
print(a + b)                       # [3 6 9]
print(a * b)                       # [2 8 18] (elementwise)
print(a / 2)                       # [1. 2. 3.]
```

`a * b` is not matrix multiplication. Use `a @ b` for an appropriate dot/matrix product.

## 5. Broadcasting

```python
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])
offset = np.array([10, 20, 30])
print(matrix + offset)
# [[11 22 33]
#  [14 25 36]]
```

The shape `(3,)` can broadcast across rows of shape `(2, 3)`. Not all different shapes are compatible.

## 6. Aggregates

```python
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])
print(matrix.sum())                # 21
print(matrix.mean())               # 3.5
print(matrix.sum(axis=0))          # [5 7 9] (down rows, per column)
print(matrix.sum(axis=1))          # [6 15] (across columns, per row)
```

## 7. Filtering

```python
arr = np.array([3, 8, 12, 5])
mask = arr > 6
print(mask)                        # [False  True  True False]
print(arr[mask])                   # [ 8 12]
```

## 8. Random numbers

```python
rng = np.random.default_rng(42)    # Seed for reproducible practice
sample = rng.integers(0, 10, size=3)
print(sample)                      # 3 random integers, each from 0 to 9
```

## Tiny checks before moving on

- [ ] Explain why `[1, 2, 3] * 2` differs from `np.array([1, 2, 3]) * 2`
- [ ] Create a `2 x 3` array and report its `ndim`, `shape`, and `size`
- [ ] Extract the second column from a 2D array
- [ ] Explain `axis=0` versus `axis=1` for `sum`
- [ ] Filter an array for values above a threshold

**Note for ML:** NumPy makes it easier to work with vectors, matrices, batches, and numerical data. Learn the array shapes before rushing into ML models.
