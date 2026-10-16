# Python Learning Roadmap

> Track what we have covered, what needs more practice, and what comes next.
>
> **Last updated:** 16 October 2026  
> **Current checkpoint:** NumPy basics and matrix drills practiced; a five-step **pure-Python** gradient descent loop for one training example was written and understood on 16 October. Continue practicing independent code and 2D slicing.  
> **Next lesson:** Convert the one-example training loop to NumPy arrays and work with multiple samples. Review [loop trace](../FOR_LOOP_TRACE.md), [NumPy notes](../numpy_basics.md), and [NumPy cheat sheet](../NUMPY_CHEATSHEET.md) when needed.

## ✅ Covered

These topics have come up in our lessons and practice. "Covered" does not mean "fully mastered."

- Lists and common list operations
- Strings and common string operations
- Dictionaries and `.get()`
- Sets
- `range()`
- `enumerate()`
- `zip()`
- Common built-in functions
- Frequency counting with dictionaries
- List comprehensions
- Dictionary comprehensions
- Sorting with `.sort()` and `sorted()`
- Ascending and descending sorting
- Custom sorting with `key`
- Lambda functions for sorting
- Sorting tuples by multiple conditions
- Basic loops and conditional logic through coding problems
- Five-iteration gradient descent loop with reassigned w/b, print placement, and updated values carried forward ([trace](../FOR_LOOP_TRACE.md))
- Functions: `def`, arguments, and `return` (quick review)
- Indexing and basic slicing (quick review)
- Nested lists and `matrix[row][column]` (quick review)
- NumPy arrays, shapes, dimensions, arithmetic, broadcasting, aggregates, Boolean masks, random number generation (studied + practice drills)
- Basic NumPy reshape and 2D indexing (introduced during practice)

## 🟡 Needs More Practice

- List methods
- String methods
- Sorting strings by length
- Stable sorting and tie handling
- Lambda expressions in more complex sorting tasks
- Functions and their arguments
- Slice stop boundaries: `nums[1:3]` excludes index 3
- Writing small functions without examples
- 2D indexing and row/column selection
- NumPy rectangular slicing: selecting **all** intersecting rows and columns, not just one cell
- NumPy indexing: counting both row and column indices from zero
- Applying NumPy operations independently without reference examples
- Backtracking fundamentals

## ⏳ Still to Cover

### 1. Python Collections

- [ ] `collections.Counter`
- [ ] `collections.defaultdict`
- [ ] `collections.deque`
- [ ] `collections.OrderedDict`
- [ ] `collections.namedtuple`

### 2. Data Structures

- [ ] Stacks
- [ ] Queues
- [ ] Heaps (`heapq`)
- [ ] Binary search (`bisect`)
- [ ] Sets and dictionaries in more depth

### 3. Iteration and Functional Tools

- [ ] Iterators
- [ ] Generators
- [ ] `yield`
- [ ] `map()`
- [ ] `filter()`
- [ ] `itertools`

### 4. Advanced Python

- [ ] Decorators
- [ ] Closures
- [ ] Scope: `global` and `nonlocal`
- [ ] `*args` and `**kwargs`
- [ ] Exception handling
- [ ] Context managers
- [ ] Type hints
- [ ] Dataclasses

### 5. Object-Oriented Programming

- [ ] Classes and objects
- [ ] Constructors
- [ ] Instance methods and class methods
- [ ] Inheritance
- [ ] Polymorphism
- [ ] Encapsulation
- [ ] Dunder methods

### 6. Python Internals

- [ ] Mutable vs. immutable objects
- [ ] References and object identity
- [ ] Shallow vs. deep copying
- [ ] Memory management
- [ ] Garbage collection
- [ ] Global Interpreter Lock (GIL)
- [ ] Python execution model

### 7. Practical Python

- [ ] Modules and packages
- [ ] Virtual environments
- [ ] File handling
- [ ] JSON and CSV
- [ ] Logging
- [ ] Unit testing
- [ ] Dependency management

### 8. Concurrency and Performance

- [ ] Threading
- [ ] Multiprocessing
- [ ] `asyncio`
- [ ] `async` / `await`
- [ ] Profiling
- [ ] Performance optimization

### 9. Python for AI/ML

- [x] NumPy fundamentals (tutorial watched and revised; see [detailed notes](../numpy_basics.md) and [quick cheat sheet](../NUMPY_CHEATSHEET.md))
- [x] NumPy matrix multiplication, transpose and broadcasting drills (review remains useful)
- [x] NumPy vectorized forward prediction, dataset MSE, averaged gradients and five-epoch full-batch training over four samples (16 Oct)
- [ ] NumPy multi-feature and multi-neuron gradient practice
- [ ] Pandas
- [ ] Matplotlib
- [x] Vectorized elementwise operations, scalar broadcasting and np.mean aggregation (four-example training)
- [ ] PyTorch
- [ ] Efficient ML data pipelines

## NumPy tutorial (watched and revised on 14 October 2026)

Video: [NumPy tutorial](https://www.youtube.com/watch?v=VXU4LSAQDSc). The boxes below track study progress, not just reference material added to the repo.

- [x] [00:00:00 — Introduction](https://www.youtube.com/watch?v=VXU4LSAQDSc&t=0s)
- [x] [00:05:07 — Multidimensional arrays](https://www.youtube.com/watch?v=VXU4LSAQDSc&t=307s)
- [x] [00:12:54 — Slicing](https://www.youtube.com/watch?v=VXU4LSAQDSc&t=774s)
- [x] [00:24:04 — Arithmetic](https://www.youtube.com/watch?v=VXU4LSAQDSc&t=1444s)
- [x] [00:33:21 — Broadcasting](https://www.youtube.com/watch?v=VXU4LSAQDSc&t=2001s)
- [x] [00:39:42 — Aggregate functions](https://www.youtube.com/watch?v=VXU4LSAQDSc&t=2382s)
- [x] [00:43:48 — Filtering](https://www.youtube.com/watch?v=VXU4LSAQDSc&t=2628s)
- [x] [00:52:03 — Random numbers](https://www.youtube.com/watch?v=VXU4LSAQDSc&t=3123s)

## Next Steps

- [x] Explain `np.array` versus a Python list
- [x] Practise `ndim`, `shape`, `size`, aggregates and filtering in the revision quiz
- [x] Watch all eight tutorial chapters and learn basic `reshape`
- [ ] Solve mixed 2D slicing and zero-based indexing examples independently (still error-prone)
- [x] Study vectors, dot products and matrix multiplication; practice matrix multiplication in NumPy
- [x] Code a one-example prediction, squared loss, manual gradients and five weight/bias updates in pure Python
- [x] Extend the training loop to NumPy arrays and four training examples; MSE 21→approximately 0.325768
- [ ] Keep Python sorting, function arguments, and slicing in occasional review
- [ ] Return to DSA collections (`Counter`, `defaultdict`, `deque`) when relevant

---

**Learning rule:** Understand the idea, try a small example, then solve a problem without copying the answer. Update this roadmap as we progress.


## 16 October syntax checkpoint

- [x] Use NumPy arithmetic on all four inputs without a Python loop.
- [x] Compute MSE by squaring **before** np.mean().
- [x] Apply np.mean() to elementwise contributions before updating one shared parameter.
- [x] Use z > 0 to form a Boolean mask.
- [x] Learn .astype(float) to convert the mask to 0.0/1.0 for a ReLU derivative.
- [ ] Next: gradient arrays and shape reasoning for several neurons; keep mathematical derivations in ML-MATH/Neural-Network.

Runnable syntax check: [numpy_vectorization_and_masks.py](../examples/numpy_vectorization_and_masks.py).
