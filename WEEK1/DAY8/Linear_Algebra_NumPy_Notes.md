# 📐 Linear Algebra with NumPy
### From Basics to Advanced — A Complete Reference for AI/ML Students

> **Target Audience:** B.Tech CS/AI students · Data Science learners · ML/AI practitioners  
> **Prerequisites:** Basic Python knowledge  
> **Goal:** Build strong mathematical intuition backed by NumPy implementation and real-world ML relevance

---

## 📚 Table of Contents

### Part 1: Vectors with NumPy
1. [Introduction to Vectors](#1--introduction-to-vectors)
2. [Creating Vectors](#2--creating-vectors)
3. [Vector Properties](#3--vector-properties)
4. [Vector Operations](#4--vector-operations)
5. [Dot Product](#5--dot-product)
6. [Vector Magnitude & Norms](#6--vector-magnitude--norms)
7. [Unit Vectors & Normalization](#7--unit-vectors--normalization)
8. [Angle Between Vectors](#8--angle-between-vectors)
9. [Broadcasting with Vectors](#9--broadcasting-with-vectors)

### Part 2: Matrices with NumPy
10. [Introduction to Matrices](#10--introduction-to-matrices)
11. [Creating Matrices](#11--creating-matrices)
12. [Matrix Properties](#12--matrix-properties)
13. [Matrix Operations](#13--matrix-operations)
14. [Matrix Multiplication](#14--matrix-multiplication)
15. [Special Matrix Operations](#15--special-matrix-operations)
16. [Determinant, Inverse & Rank](#16--determinant-inverse--rank)
17. [Linear Systems of Equations](#17--linear-systems-of-equations)
18. [Eigenvalues & Eigenvectors](#18--eigenvalues--eigenvectors)

### Part 3: Linear Algebra in ML & AI
19. [Vectors & Matrices in ML](#19--vectors--matrices-in-ml)
20. [Common Errors & Pitfalls](#20--common-errors--pitfalls)
21. [Best Practices](#21--best-practices)
22. [Quick Revision Cheat Sheet](#22--quick-revision-cheat-sheet)

---

# PART 1: VECTORS WITH NUMPY

---

## 1. 📌 Introduction to Vectors

### What is a Vector?

**Mathematically**, a vector is an ordered list of numbers that has both **magnitude** (size) and **direction**. It lives in an n-dimensional space.

```
v = [3, 4]        → 2D vector (lives on a plane)
v = [1, 2, 3]     → 3D vector (lives in space)
v = [x₁, x₂, ..., xₙ]  → n-dimensional vector
```

**In programming**, a vector is simply a 1D array.

### Scalars vs Vectors

| Concept | Description | Example |
|---------|-------------|---------|
| **Scalar** | A single number — no direction | Temperature = 37°C |
| **Vector** | An ordered list of numbers — has direction | Velocity = [3 m/s East, 4 m/s North] |
| **In NumPy** | Scalar = 0D array / plain number | Vector = 1D array |

### Role of Vectors in AI/ML

- **Feature Vectors:** Each data sample is represented as a vector. A house with 3 features → `[area, bedrooms, price]`
- **Word Embeddings:** Words represented as dense vectors (Word2Vec, GloVe)
- **Model Parameters:** Weights in a neural network layer stored as vectors
- **Distances & Similarity:** Vectors let us compute how similar two data points are

```
User 1 preferences: [0.9, 0.1, 0.7]   (action, romance, sci-fi)
User 2 preferences: [0.8, 0.2, 0.6]
→ These users have similar taste (vectors are close together)
```

---

## 2. 🔢 Creating Vectors

```python
import numpy as np
```

### From a Python List

```python
# 1D array — the standard vector
v = np.array([1, 2, 3, 4])
print(v)        # [1 2 3 4]
print(type(v))  # <class 'numpy.ndarray'>
```

### Row Vector vs Column Vector

```python
# Row vector — shape (1, n)
row = np.array([[1, 2, 3]])
print(row.shape)   # (1, 3)

# Column vector — shape (n, 1)
col = np.array([[1],
                [2],
                [3]])
print(col.shape)   # (3, 1)
```

> ⚠️ **Critical Distinction:** A 1D array `shape (3,)` is neither a row nor a column vector — it is ambiguous. In ML, always be explicit about shape.

### Utility Functions for Creating Vectors

```python
# All zeros
zeros = np.zeros(5)
print(zeros)   # [0. 0. 0. 0. 0.]

# All ones
ones = np.ones(4)
print(ones)    # [1. 1. 1. 1.]

# Range of values (like Python's range)
r = np.arange(0, 10, 2)    # start=0, stop=10, step=2
print(r)       # [0 2 4 6 8]

# Evenly spaced values between two points
ls = np.linspace(0, 1, 5)  # 5 points from 0 to 1
print(ls)      # [0.   0.25 0.5  0.75 1.  ]
```

> **ML Relevance:** `np.linspace` is used to create learning rate schedules. `np.arange` is used for indexing and iteration over epochs.

### Comparison: arange vs linspace

| Function | Input | Output |
|----------|-------|--------|
| `np.arange(0, 1, 0.2)` | step size | values at each step |
| `np.linspace(0, 1, 5)` | number of points | equally spaced values |

---

## 3. 📐 Vector Properties

```python
v = np.array([10, 20, 30, 40, 50])

print(v.shape)   # (5,)   → 1D with 5 elements
print(v.size)    # 5      → total number of elements
print(v.ndim)    # 1      → number of dimensions
print(v.dtype)   # int64  → data type of elements
```

### Reshaping Vectors

Reshaping changes the **shape** (structure) without changing the **data** (values).

```python
v = np.array([1, 2, 3, 4, 5, 6])

# Convert 1D vector to column vector
col = v.reshape(6, 1)
print(col.shape)   # (6, 1)

# Convert 1D to row vector
row = v.reshape(1, 6)
print(row.shape)   # (1, 6)

# Use -1 to let NumPy infer one dimension
col2 = v.reshape(-1, 1)   # same as (6, 1)
row2 = v.reshape(1, -1)   # same as (1, 6)
```

> **Best Practice:** Use `reshape(-1, 1)` to convert a 1D feature array into a column vector before feeding into sklearn models — a very common operation.

### Flattening

```python
matrix = np.array([[1, 2], [3, 4], [5, 6]])
flat = matrix.flatten()     # Always returns a copy
print(flat)  # [1 2 3 4 5 6]

flat2 = matrix.ravel()      # Returns a view when possible (more memory efficient)
```

---

## 4. ➕ Vector Operations

### Addition and Subtraction

**Mathematically:** Add corresponding elements.

```
a = [1, 2, 3]
b = [4, 5, 6]
a + b = [5, 7, 9]
```

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)   # [5 7 9]
print(a - b)   # [-3 -3 -3]
```

> ⚠️ **Pitfall:** Vectors must have the **same shape** for addition/subtraction (unless broadcasting applies).

### Scalar Multiplication

**Mathematically:** Multiply every element by the scalar.

```
2 × [1, 2, 3] = [2, 4, 6]
```

```python
v = np.array([1, 2, 3])
print(2 * v)     # [2 4 6]
print(v / 2)     # [0.5 1.  1.5]
print(v ** 2)    # [1 4 9]   (element-wise square)
```

### Element-wise Operations

All standard arithmetic operators work **element-wise** in NumPy.

```python
a = np.array([2, 4, 6])
b = np.array([1, 2, 3])

print(a * b)     # [ 2  8 18]  ← element-wise multiply (NOT dot product)
print(a / b)     # [2. 2. 2.]
print(a % b)     # [0 0 0]
print(np.sqrt(a))# [1.414 2.    2.449]
```

> **ML Relevance:** Element-wise operations are the backbone of loss function computations.  
> `errors = predictions - targets` → element-wise subtraction on thousands of samples simultaneously.

---

## 5. 🔵 Dot Product

### Mathematical Meaning

The dot product of two vectors is a **scalar** that measures how much they point in the same direction.

```
a · b = a₁b₁ + a₂b₂ + ... + aₙbₙ
```

```
a = [1, 2, 3],  b = [4, 5, 6]
a · b = (1×4) + (2×5) + (3×6) = 4 + 10 + 18 = 32
```

**Geometric interpretation:**
```
a · b = |a| × |b| × cos(θ)
```
- If `a · b = 0` → vectors are **perpendicular** (orthogonal)
- If `a · b > 0` → vectors point in **similar directions**
- If `a · b < 0` → vectors point in **opposite directions**

### NumPy Implementation

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Method 1: np.dot()
result1 = np.dot(a, b)
print(result1)   # 32

# Method 2: @ operator (preferred in modern Python)
result2 = a @ b
print(result2)   # 32

# Method 3: manual (slow — never use in practice)
result3 = np.sum(a * b)
print(result3)   # 32
```

> **Prefer `@` over `np.dot()`** for readability. PEP 465 introduced `@` specifically for matrix/vector multiplication.

### Use Cases in ML

```python
# Linear regression prediction: y = w · x + b
weights = np.array([0.5, 1.2, -0.3])
features = np.array([2.0, 3.0, 1.0])
bias = 0.8

prediction = np.dot(weights, features) + bias
print(f"Prediction: {prediction:.2f}")   # Prediction: 4.10

# Similarity check
user_a = np.array([5, 3, 0, 1])   # ratings for 4 movies
user_b = np.array([4, 0, 4, 1])
similarity = np.dot(user_a, user_b)
print(f"Raw similarity: {similarity}")   # 22
```

---

## 6. 📏 Vector Magnitude & Norms

### What is a Norm?

A **norm** is a function that assigns a non-negative length (magnitude) to a vector. Different norms measure "length" differently.

### L1 Norm (Manhattan Norm)

```
||v||₁ = |v₁| + |v₂| + ... + |vₙ|
```

```python
v = np.array([3, -4, 0, 2])

l1 = np.linalg.norm(v, ord=1)
print(l1)   # 9.0  →  |3| + |-4| + |0| + |2| = 9
```

> **ML Use:** L1 norm is used in **Lasso regularization** to encourage sparse weights (many weights become exactly 0).

### L2 Norm (Euclidean Norm)

```
||v||₂ = √(v₁² + v₂² + ... + vₙ²)
```

```python
v = np.array([3, 4])

l2 = np.linalg.norm(v)       # Default is L2
print(l2)   # 5.0  →  √(9 + 16) = √25 = 5

# Manual verification
manual = np.sqrt(np.sum(v**2))
print(manual)   # 5.0
```

> **ML Use:** L2 norm is used in **Ridge regularization**, computing Euclidean distances, and normalizing vectors.

### L∞ Norm (Max Norm)

```
||v||∞ = max(|v₁|, |v₂|, ..., |vₙ|)
```

```python
v = np.array([3, -7, 2])
linf = np.linalg.norm(v, ord=np.inf)
print(linf)   # 7.0
```

### Summary of Norms

```python
v = np.array([1, -2, 3, -4])

print(f"L0 norm (non-zeros): {np.linalg.norm(v, ord=0)}")    # 4.0
print(f"L1 norm:             {np.linalg.norm(v, ord=1)}")    # 10.0
print(f"L2 norm:             {np.linalg.norm(v, ord=2):.4f}")# 5.4772
print(f"L∞ norm:             {np.linalg.norm(v, ord=np.inf)}")# 4.0
```

---

## 7. 📐 Unit Vectors & Normalization

### What is a Unit Vector?

A **unit vector** has a magnitude (L2 norm) of exactly **1**. It preserves direction but discards magnitude.

```
û = v / ||v||₂
```

### Why Normalization Matters

- **Removes scale bias:** A feature with values [0–1000] would dominate one with values [0–1]
- **Enables cosine similarity:** Comparing directions rather than magnitudes
- **Faster convergence:** Gradient descent behaves better with normalized inputs

### Implementation

```python
v = np.array([3.0, 4.0])

# Normalize to unit vector
unit_v = v / np.linalg.norm(v)
print(unit_v)                       # [0.6 0.8]
print(np.linalg.norm(unit_v))       # 1.0  ← confirmed unit vector

# General normalization function
def normalize(vector):
    norm = np.linalg.norm(vector)
    if norm == 0:
        raise ValueError("Cannot normalize a zero vector!")
    return vector / norm

v = np.array([1.0, 2.0, 2.0])
print(normalize(v))   # [0.333 0.667 0.667]
```

> ⚠️ **Common Error:** Normalizing a zero vector causes division by zero. Always check `norm != 0`.

### ML Example: Normalizing a Feature Column

```python
# Raw feature data (house sizes in sqft)
sizes = np.array([500.0, 1500.0, 3000.0, 800.0])

# Min-Max normalization (scale to [0, 1])
normalized = (sizes - sizes.min()) / (sizes.max() - sizes.min())
print(normalized)   # [0.    0.4   1.    0.12]

# L2 normalization (unit vector)
l2_norm = sizes / np.linalg.norm(sizes)
print(l2_norm)
```

---

## 8. 📊 Angle Between Vectors

### Mathematical Formula

Using the geometric interpretation of the dot product:

```
cos(θ) = (a · b) / (||a|| × ||b||)
θ = arccos(a · b / ||a|| × ||b||)
```

### Cosine Similarity

Cosine similarity is just `cos(θ)` — it ranges from -1 to 1:

| cos(θ) | Meaning |
|--------|---------|
| 1.0 | Identical direction (0°) |
| 0.0 | Perpendicular (90°) |
| -1.0 | Opposite direction (180°) |

```python
a = np.array([1.0, 0.0, 1.0])
b = np.array([1.0, 1.0, 0.0])

# Cosine similarity
cos_sim = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
print(f"Cosine Similarity: {cos_sim:.4f}")   # 0.5000

# Angle in degrees
angle_rad = np.arccos(np.clip(cos_sim, -1.0, 1.0))  # clip for numerical safety
angle_deg = np.degrees(angle_rad)
print(f"Angle: {angle_deg:.2f}°")            # 60.00°
```

> ⚠️ **Numerical Safety:** Due to floating-point errors, `cos_sim` might be slightly outside `[-1, 1]`. Use `np.clip(cos_sim, -1.0, 1.0)` before `np.arccos`.

### ML Use: Document Similarity

```python
# Two documents represented as word frequency vectors
doc1 = np.array([1, 1, 0, 1, 0])   # words: [python, data, java, science, cpp]
doc2 = np.array([1, 1, 1, 0, 0])

cos_sim = np.dot(doc1, doc2) / (np.linalg.norm(doc1) * np.linalg.norm(doc2))
print(f"Document similarity: {cos_sim:.4f}")   # 0.6667

# High similarity → documents discuss similar topics
```

---

## 9. 🔁 Broadcasting with Vectors

### How Broadcasting Works

Broadcasting is NumPy's ability to perform operations on arrays of **different shapes** by automatically "stretching" the smaller array.

**Rules (applied dimension by dimension, right to left):**
1. If arrays differ in number of dimensions, prepend 1s to the smaller shape
2. Dimensions of size 1 are stretched to match the other
3. Shapes must be compatible (equal or one of them is 1)

```python
# Scalar broadcast to vector
v = np.array([1, 2, 3])
print(v + 10)    # [11 12 13]  ← 10 is broadcast to [10, 10, 10]

# 1D broadcast with 2D
A = np.array([[1, 2, 3],
              [4, 5, 6]])   # shape (2, 3)
b = np.array([10, 20, 30])  # shape (3,)  → broadcast as (1, 3) → (2, 3)

print(A + b)
# [[11 22 33]
#  [14 25 36]]
```

### Visualizing Broadcasting

```
A: (2, 3)       b: (3,) → treated as (1, 3) → stretched to (2, 3)
[[1, 2, 3]      [10, 20, 30]
 [4, 5, 6]]  +  [10, 20, 30]   ← b is "broadcast" across rows

= [[11, 22, 33]
   [14, 25, 36]]
```

### Column vs Row Broadcasting

```python
col = np.array([[1],   # shape (3, 1)
                [2],
                [3]])
row = np.array([10, 20, 30])  # shape (3,) → (1, 3)

result = col + row
print(result)
# [[11, 21, 31],
#  [12, 22, 32],
#  [13, 23, 33]]
# shape: (3, 3)  ← outer sum!
```

### Common Broadcasting Mistakes

```python
a = np.array([1, 2, 3])      # shape (3,)
b = np.array([1, 2])         # shape (2,)

# ❌ Error: incompatible shapes
# a + b  → ValueError: operands could not be broadcast together with shapes (3,) (2,)

# ✅ Fix: make shapes compatible
b_col = b.reshape(2, 1)     # shape (2, 1)
a_row = a.reshape(1, 3)     # shape (1, 3)
result = b_col + a_row      # shape (2, 3) — valid outer sum
```

> **ML Relevance:** Broadcasting is essential for adding biases to layer outputs.  
> `output = weights @ inputs + bias` — bias is broadcast across all samples in the batch.

---

# PART 2: MATRICES WITH NUMPY

---

## 10. 🧩 Introduction to Matrices

### What is a Matrix?

A **matrix** is a 2D rectangular array of numbers arranged in rows and columns.

```
A = [[a₁₁, a₁₂, a₁₃],     → shape: (m, n)
     [a₂₁, a₂₂, a₂₃]]       m = rows, n = columns
```

### Matrix vs Vector

| | Vector | Matrix |
|--|--------|--------|
| Dimensions | 1D | 2D |
| Shape | (n,) or (n,1) | (m, n) |
| Represents | Single data point | Dataset or transformation |
| NumPy | `np.array([1,2,3])` | `np.array([[1,2],[3,4]])` |

### Why Matrices Matter in AI/ML

- **Dataset Representation:** 1000 samples × 10 features → matrix of shape (1000, 10)
- **Linear Transformations:** Rotation, scaling, projection
- **Neural Network Layers:** Input → hidden layer = matrix multiplication
- **Covariance Matrix:** Captures feature relationships (PCA)
- **Image Data:** A grayscale image is literally a matrix of pixel values

---

## 11. 🔢 Creating Matrices

### From Python Lists

```python
import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print(A)
print(A.shape)   # (3, 3)
```

### Utility Functions

```python
# Zero matrix
Z = np.zeros((3, 4))       # 3 rows, 4 columns, all zeros
print(Z)

# Ones matrix
O = np.ones((2, 3))        # all ones
print(O)

# Identity matrix (square matrix, diagonal = 1)
I = np.eye(4)              # 4×4 identity
print(I)

# Diagonal matrix from a vector
d = np.diag([1, 2, 3, 4])  # puts values on the diagonal
print(d)
```

### Random Matrices

```python
# Uniform distribution [0, 1)
R1 = np.random.rand(3, 3)

# Standard normal distribution (mean=0, std=1)
R2 = np.random.randn(3, 3)

# Random integers
R3 = np.random.randint(0, 10, size=(3, 3))   # values in [0, 10)

# For reproducibility — always set seed in ML experiments
np.random.seed(42)
W = np.random.randn(3, 4)   # Weight matrix for a layer
print(W)
```

> **Best Practice:** Always use `np.random.seed(42)` at the start of ML experiments for reproducibility.

---

## 12. 📐 Matrix Properties

```python
A = np.array([[1, 2, 3],
              [4, 5, 6]])

print(A.shape)   # (2, 3)  → 2 rows, 3 columns
print(A.size)    # 6       → total elements
print(A.ndim)    # 2       → 2 dimensions
print(A.dtype)   # int64

# Accessing rows and columns
print(A[0])      # [1 2 3]  → first row
print(A[:, 1])   # [2 5]    → second column
print(A[1, 2])   # 6        → element at row 1, col 2
```

### Transpose of a Matrix

**Mathematically:** Flip along the main diagonal. Rows become columns.

```
A = [[1, 2, 3],      Aᵀ = [[1, 4],
     [4, 5, 6]]             [2, 5],
                             [3, 6]]
```

```python
A = np.array([[1, 2, 3],
              [4, 5, 6]])

print(A.shape)     # (2, 3)
print(A.T.shape)   # (3, 2)
print(A.T)
# [[1 4]
#  [2 5]
#  [3 6]]

# Equivalent
print(np.transpose(A))
```

> **ML Relevance:** Transpose is critical in the backpropagation algorithm.  
> Forward: `Y = W @ X` → Gradient: `dW = dY @ Xᵀ`

---

## 13. ➕ Matrix Operations

### Addition and Subtraction

**Rule:** Matrices must have the **same shape**.

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(A + B)
# [[ 6  8]
#  [10 12]]

print(A - B)
# [[-4 -4]
#  [-4 -4]]
```

### Scalar Multiplication

```python
A = np.array([[1, 2], [3, 4]])

print(3 * A)
# [[ 3  6]
#  [ 9 12]]

print(A / 2)
# [[0.5 1. ]
#  [1.5 2. ]]
```

### Element-wise Multiplication (Hadamard Product)

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Element-wise (NOT matrix multiplication)
C = A * B
print(C)
# [[ 5 12]
#  [21 32]]
```

> ⚠️ **Critical:** `A * B` is **element-wise**. `A @ B` is **matrix multiplication**. These are completely different operations!

---

## 14. ✖️ Matrix Multiplication

### Mathematical Condition

To multiply A × B:
- A has shape **(m × k)**
- B has shape **(k × n)**
- Result has shape **(m × n)**

The **inner dimensions must match** (both equal to k).

```
A: (3, 4) × B: (4, 2) → C: (3, 2)   ✅ Valid
A: (3, 4) × B: (3, 2) → Error        ❌ Invalid (4 ≠ 3)
```

### Implementation

```python
A = np.array([[1, 2],
              [3, 4],
              [5, 6]])   # shape (3, 2)

B = np.array([[7, 8, 9],
              [10, 11, 12]])  # shape (2, 3)

# Method 1: np.dot()
C = np.dot(A, B)
print(C)
# [[ 27  30  33]
#  [ 61  68  75]
#  [ 95 106 117]]
print(C.shape)   # (3, 3)

# Method 2: @ operator (preferred)
C2 = A @ B
print(np.array_equal(C, C2))   # True
```

### Manual Verification

```python
# C[0, 0] = row 0 of A · col 0 of B
# = [1, 2] · [7, 10] = 1*7 + 2*10 = 27 ✓
```

### Element-wise vs Matrix Multiplication

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 0], [1, 3]])

print("Element-wise (A * B):\n", A * B)
# [[ 2  0]
#  [ 3 12]]

print("Matrix multiply (A @ B):\n", A @ B)
# [[ 4  6]
#  [10 12]]
```

> **ML Relevance:** Forward pass of a neural network layer:
> ```
> output = activation(W @ input + b)
> ```
> This is a matrix multiplication — the core of deep learning.

---

## 15. 🔄 Special Matrix Operations

### Transpose

```python
A = np.array([[1, 2, 3], [4, 5, 6]])
print(A.T)       # or np.transpose(A)
```

### Identity Matrix

The identity matrix `I` is the matrix equivalent of the number 1: `A × I = A`

```python
I = np.eye(3)
print(I)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

A = np.array([[2, 3], [1, 4]])
print(A @ np.eye(2))   # Returns A unchanged
```

### Diagonal Matrices

```python
# Extract diagonal from a matrix
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

diag_vals = np.diag(A)
print(diag_vals)   # [1 5 9]  ← main diagonal

# Create a diagonal matrix from values
D = np.diag([3, 7, 2])
print(D)
# [[3 0 0]
#  [0 7 0]
#  [0 0 2]]

# Trace: sum of diagonal elements
print(np.trace(A))   # 15  (= 1 + 5 + 9)
```

### Symmetric Matrix

A matrix where `A = Aᵀ` (symmetric about the main diagonal).

```python
A = np.array([[1, 2, 3],
              [2, 5, 6],
              [3, 6, 9]])

is_symmetric = np.array_equal(A, A.T)
print(is_symmetric)   # True
```

> **ML Relevance:** Covariance matrices are always symmetric — crucial for PCA and Gaussian distributions.

---

## 16. 🧮 Determinant, Inverse & Rank

### Determinant

The **determinant** is a scalar value computed from a square matrix that encodes geometric information (volume scaling, orientation).

```
For 2×2: det([[a,b],[c,d]]) = ad - bc
```

```python
A = np.array([[3, 1],
              [2, 4]])

det = np.linalg.det(A)
print(f"det(A) = {det:.2f}")   # det(A) = 10.00

# 3×3 example
B = np.array([[1, 2, 3],
              [0, 1, 4],
              [5, 6, 0]])
print(f"det(B) = {np.linalg.det(B):.2f}")   # det(B) = 1.00
```

**Key Insight:**
- `det(A) ≠ 0` → Matrix is **invertible** (non-singular)
- `det(A) = 0` → Matrix is **singular** (not invertible, rows are linearly dependent)

### Matrix Inverse

If `A × A⁻¹ = I`, then `A⁻¹` is the inverse.

```python
A = np.array([[3.0, 1.0],
              [2.0, 4.0]])

A_inv = np.linalg.inv(A)
print("Inverse:\n", A_inv)

# Verify: A × A⁻¹ should be Identity
product = A @ A_inv
print("A × A_inv:\n", np.round(product, 10))
# [[1. 0.]
#  [0. 1.]]  ← Identity matrix ✓
```

> ⚠️ **Important:** Never compute `A_inv @ b` to solve `Ax = b` in production — it's numerically unstable and slow. Use `np.linalg.solve(A, b)` instead.

### Matrix Rank

The **rank** is the number of linearly independent rows (or columns) — tells you the "effective dimensions" of the matrix.

```python
# Full rank matrix
A = np.array([[1, 0], [0, 1]])
print(np.linalg.matrix_rank(A))   # 2 (full rank)

# Rank-deficient matrix (rows are dependent)
B = np.array([[1, 2, 3],
              [2, 4, 6],   # ← 2 × row 0
              [0, 1, 2]])
print(np.linalg.matrix_rank(B))   # 2 (not 3, because row 1 = 2 × row 0)
```

> **ML Relevance:** Low-rank matrices appear in recommender systems (matrix factorization). A rank-deficient feature matrix indicates **multicollinearity** — some features are redundant.

---

## 17. 🧠 Linear Systems of Equations

### The Problem

Solve for `x` in the system `Ax = b`:

```
3x + y = 9
2x + 4y = 22
```

In matrix form:
```
A = [[3, 1],    x = [x],    b = [9]
     [2, 4]]        [y]         [22]
```

### Using np.linalg.solve()

```python
A = np.array([[3.0, 1.0],
              [2.0, 4.0]])
b = np.array([9.0, 22.0])

x = np.linalg.solve(A, b)
print(x)   # [2. 3.]  → x=2, y=3

# Verify: Ax should equal b
print(np.allclose(A @ x, b))   # True
```

### When the System Has No Unique Solution

```python
# Singular matrix (det = 0) → no unique solution
A_singular = np.array([[1.0, 2.0],
                        [2.0, 4.0]])   # row 2 = 2 × row 1
b = np.array([3.0, 6.0])

try:
    x = np.linalg.solve(A_singular, b)
except np.linalg.LinAlgError as e:
    print(f"Error: {e}")   # Singular matrix
```

### Least Squares Solution (Overdetermined Systems)

When you have more equations than unknowns (common in ML regression):

```python
# More data points than parameters
A = np.array([[1, 1],
              [1, 2],
              [1, 3],
              [1, 4]])  # shape (4, 2)  → 4 equations, 2 unknowns
b = np.array([2.1, 3.9, 6.1, 7.9])

# Least squares solution (minimizes ||Ax - b||²)
x, residuals, rank, sv = np.linalg.lstsq(A, b, rcond=None)
print(x)   # approximately [0.2, 1.94]  (intercept ≈ 0.2, slope ≈ 2)
```

> **ML Relevance:** Linear regression is exactly solving `Xw = y` in the least-squares sense. `np.linalg.lstsq` is what `LinearRegression` does internally.

---

## 18. 📊 Eigenvalues & Eigenvectors

### Conceptual Understanding

For a square matrix `A`, an **eigenvector** `v` satisfies:
```
A × v = λ × v
```
Where `λ` (lambda) is the **eigenvalue**.

**Meaning:** When `A` multiplies `v`, the result is just `v` scaled by `λ` — the direction doesn't change, only the magnitude.

**Physical intuition:** Eigenvectors are the "natural axes" of a transformation. A scaling matrix stretches space — eigenvectors point along the stretch directions.

### NumPy Implementation

```python
A = np.array([[4.0, 1.0],
              [2.0, 3.0]])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
# [5. 2.]

print("Eigenvectors (columns):\n", eigenvectors)
# Each COLUMN is an eigenvector
# [[ 0.707  -0.447]
#  [ 0.707   0.894]]

# Verify: A @ v = λ × v
v1 = eigenvectors[:, 0]   # first eigenvector
lambda1 = eigenvalues[0]  # first eigenvalue
print(np.allclose(A @ v1, lambda1 * v1))   # True ✓
```

### Why Eigenvalues Matter in ML

```python
# Covariance matrix — symmetric, so eigenvalues are real
data = np.array([[2.0, 0.0],
                 [0.0, 0.5],
                 [2.2, 0.1],
                 [1.9, 0.0]])

cov = np.cov(data.T)   # Covariance matrix
eigenvalues, eigenvectors = np.linalg.eig(cov)

print("Variance explained by each component:")
total = np.sum(eigenvalues)
for i, ev in enumerate(eigenvalues):
    print(f"  PC{i+1}: {ev/total*100:.1f}%")
```

> **Key ML Applications:**
> - **PCA (Principal Component Analysis):** Eigenvectors of the covariance matrix define the principal components; eigenvalues tell you how much variance each component explains
> - **Graph Neural Networks:** Spectral graph convolutions use eigenvalues of the graph Laplacian
> - **Stability Analysis:** Eigenvalues determine whether iterative algorithms converge

---

# PART 3: LINEAR ALGEBRA IN ML & AI

---

## 19. 🚀 Vectors & Matrices in ML

### Feature Matrix

In ML, an entire dataset is a matrix:
- **Rows** = data samples
- **Columns** = features

```python
# Dataset: 5 students, 3 features (math, science, english scores)
X = np.array([[85, 92, 78],
              [70, 65, 80],
              [90, 88, 95],
              [60, 72, 68],
              [75, 80, 85]])
# Shape: (5, 3) — 5 samples, 3 features

print(f"Samples: {X.shape[0]}, Features: {X.shape[1]}")
```

### Weight Matrix (Neural Network)

```python
# Input layer: 3 features → Hidden layer: 4 neurons
np.random.seed(0)
W1 = np.random.randn(4, 3)   # shape (neurons_out, features_in)
b1 = np.zeros((4, 1))         # bias for each neuron

# Forward pass for one sample
x = np.array([[85], [92], [78]])  # shape (3, 1)
z = W1 @ x + b1                   # shape (4, 1)
print("Layer output shape:", z.shape)

# ReLU activation
output = np.maximum(0, z)
print("After ReLU:\n", output)
```

### Full Forward Pass Example

```python
def relu(x):
    return np.maximum(0, x)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Simple 2-layer network
np.random.seed(42)

# Architecture: 3 input → 4 hidden → 1 output
W1 = np.random.randn(4, 3) * 0.1
b1 = np.zeros((4, 1))
W2 = np.random.randn(1, 4) * 0.1
b2 = np.zeros((1, 1))

# Input: 5 samples, 3 features → shape (3, 5) (transposed)
X = np.array([[85, 92, 78],
              [70, 65, 80],
              [90, 88, 95],
              [60, 72, 68],
              [75, 80, 85]]).T   # shape (3, 5)

# Forward pass
Z1 = W1 @ X + b1          # (4, 5)
A1 = relu(Z1)              # (4, 5)
Z2 = W2 @ A1 + b2          # (1, 5)
A2 = sigmoid(Z2)           # (1, 5) — probabilities

print("Predictions shape:", A2.shape)
print("Predictions:\n", np.round(A2, 3))
```

### Linear Regression via Matrix Operations

```python
# Closed-form solution: w = (XᵀX)⁻¹ Xᵀy
np.random.seed(0)
n = 100

# Generate synthetic data: y = 2x + 1 + noise
X_raw = np.random.randn(n)
y = 2 * X_raw + 1 + 0.3 * np.random.randn(n)

# Add bias column (column of ones)
X = np.column_stack([np.ones(n), X_raw])   # shape (100, 2)

# Normal equation
w = np.linalg.inv(X.T @ X) @ X.T @ y
print(f"Intercept: {w[0]:.3f}")   # ≈ 1.0
print(f"Slope:     {w[1]:.3f}")   # ≈ 2.0
```

---

## 20. ⚠️ Common Errors & Pitfalls

### 1. Shape Mismatch in Matrix Multiplication

```python
A = np.array([[1, 2, 3]])     # shape (1, 3)
B = np.array([[4, 5, 6]])     # shape (1, 3)

# ❌ Wrong: inner dimensions don't match (3 ≠ 1)
# A @ B  → ValueError

# ✅ Fix: transpose B
result = A @ B.T    # (1, 3) @ (3, 1) → (1, 1)
print(result)       # [[32]]
```

### 2. Confusing 1D and 2D Arrays

```python
v1 = np.array([1, 2, 3])       # shape (3,)   — 1D
v2 = np.array([[1, 2, 3]])     # shape (1, 3) — 2D row vector
v3 = np.array([[1], [2], [3]]) # shape (3, 1) — 2D column vector

# These behave DIFFERENTLY in matrix operations!
A = np.random.randn(3, 3)

print((A @ v1).shape)   # (3,)
print((A @ v3).shape)   # (3, 1)

# Use reshape(-1, 1) to be explicit
v1_col = v1.reshape(-1, 1)
print((A @ v1_col).shape)   # (3, 1)
```

### 3. Broadcasting Confusion

```python
a = np.array([1, 2, 3])    # shape (3,)
b = np.array([[1], [2]])   # shape (2, 1)

# Unexpected result:
result = a + b
print(result.shape)   # (2, 3) — not (3,) or (2, 1)!
print(result)
# [[2 3 4]
#  [3 4 5]]

# Debug: always check shapes before operations
print(f"a.shape = {a.shape}, b.shape = {b.shape}")
```

### 4. In-place Operations Changing Original Data

```python
A = np.array([[1.0, 2.0], [3.0, 4.0]])
B = A            # ⚠️ B is a VIEW of A, not a copy!
B[0, 0] = 999

print(A[0, 0])   # 999 — A was also changed!

# ✅ Fix: use .copy()
A = np.array([[1.0, 2.0], [3.0, 4.0]])
B = A.copy()     # independent copy
B[0, 0] = 999
print(A[0, 0])   # 1.0 — A is unchanged ✓
```

### 5. Integer Division Issues

```python
a = np.array([1, 2, 3])   # int dtype

print(a / 2)   # [0.5 1.  1.5]  ✅ — Python 3 float division
print(a // 2)  # [0 1 1]        — integer floor division

# Always specify float when needed
a_float = np.array([1.0, 2.0, 3.0])
# or
a_float = a.astype(float)
```

---

## 21. ✅ Best Practices

### 1. Always Vectorize — Never Loop

```python
# ❌ Slow: Python loop
import time
a = np.random.randn(1_000_000)
b = np.random.randn(1_000_000)

start = time.time()
result = [a[i] * b[i] for i in range(len(a))]
print(f"Loop: {time.time() - start:.3f}s")

# ✅ Fast: NumPy vectorization
start = time.time()
result = a * b
print(f"NumPy: {time.time() - start:.4f}s")
# NumPy is typically 100-1000x faster
```

### 2. Print Shapes at Every Step

```python
def debug_shape(name, arr):
    print(f"{name}: shape={arr.shape}, dtype={arr.dtype}")

X = np.random.randn(100, 5)
debug_shape("X", X)

W = np.random.randn(3, 5)
debug_shape("W", W)

# Predict the output shape before running:
# W @ X.T → (3, 5) @ (5, 100) → (3, 100)
output = W @ X.T
debug_shape("output", output)
```

### 3. Use np.allclose Instead of == for Floats

```python
a = np.array([0.1 + 0.2])
b = np.array([0.3])

print(a == b)              # [False]  — floating-point error
print(np.allclose(a, b))  # True     — checks within tolerance
```

### 4. Prefer @ Over np.dot for Matrices

```python
# Both work, but @ is cleaner for matrices
A = np.random.randn(3, 4)
B = np.random.randn(4, 2)

result1 = np.dot(A, B)    # OK but verbose for matrices
result2 = A @ B            # Preferred — more readable

print(np.allclose(result1, result2))   # True
```

### 5. Set Random Seeds for Reproducibility

```python
# At the very top of every ML script/notebook
np.random.seed(42)

# Generate weights — same every run
W = np.random.randn(10, 5)
```

### 6. Reshape Deliberately, Not Accidentally

```python
data = np.array([1, 2, 3, 4, 5, 6])

# ❌ Magic: what does shape (2, -1) give?
reshaped = data.reshape(2, -1)

# ✅ Better: be explicit
rows, cols = 2, 3
reshaped = data.reshape(rows, cols)
print(f"Shape: {reshaped.shape}")   # (2, 3) — clear intent
```

---

## 22. 📘 Quick Revision Cheat Sheet

### Creating Arrays

| Function | Description | Example |
|----------|-------------|---------|
| `np.array([1,2,3])` | From list | 1D vector |
| `np.zeros((m, n))` | All zeros | Weight init |
| `np.ones((m, n))` | All ones | Bias init |
| `np.eye(n)` | Identity matrix | Verification |
| `np.arange(a, b, step)` | Evenly spaced (step) | Indexing |
| `np.linspace(a, b, n)` | Evenly spaced (count) | Schedules |
| `np.random.randn(m, n)` | Standard normal | Weight init |
| `np.random.randint(a, b, (m,n))` | Random integers | Simulation |
| `np.diag([a, b, c])` | Diagonal matrix | Scaling |

### Array Properties

| Property | Description |
|----------|-------------|
| `.shape` | Tuple of dimensions |
| `.size` | Total number of elements |
| `.ndim` | Number of dimensions |
| `.dtype` | Data type |
| `.T` | Transpose |

### Vector Operations

| Operation | Code | Notes |
|-----------|------|-------|
| Addition | `a + b` | Same shape |
| Scalar multiply | `k * v` | Broadcasts |
| Dot product | `a @ b` or `np.dot(a, b)` | Returns scalar |
| L2 norm | `np.linalg.norm(v)` | Default L2 |
| L1 norm | `np.linalg.norm(v, ord=1)` | Sum of abs |
| Normalize | `v / np.linalg.norm(v)` | Unit vector |
| Cosine sim | `(a @ b) / (norm(a) * norm(b))` | [-1, 1] |

### Matrix Operations

| Operation | Code | Notes |
|-----------|------|-------|
| Matrix multiply | `A @ B` | Shapes: (m,k) @ (k,n) → (m,n) |
| Element-wise | `A * B` | Same shape required |
| Transpose | `A.T` | Rows ↔ columns |
| Inverse | `np.linalg.inv(A)` | Square, det ≠ 0 |
| Determinant | `np.linalg.det(A)` | Square matrix only |
| Rank | `np.linalg.matrix_rank(A)` | Independent rows |
| Trace | `np.trace(A)` | Sum of diagonal |
| Solve Ax=b | `np.linalg.solve(A, b)` | Square A only |
| Least squares | `np.linalg.lstsq(A, b)` | Overdetermined |
| Eigenvalues | `np.linalg.eig(A)` | Returns (λ, v) |

### Shape Rules

```
# Matrix multiplication
(m, k) @ (k, n) → (m, n)   ✅
(m, k) @ (m, n) → ERROR     ❌

# Broadcasting
(3,) + (3,) → (3,)
(3,) + scalar → (3,)
(3,1) + (1,3) → (3,3)
(2,3) + (3,) → (2,3)

# Common reshapes
v.reshape(-1, 1)   # 1D → column vector
v.reshape(1, -1)   # 1D → row vector
A.flatten()        # 2D → 1D
```

---

## 🎯 Summary of Key Concepts

### Part 1 — Vectors
- A **vector** is a 1D array with magnitude and direction
- **Dot product** measures alignment between vectors; returns a scalar
- **L2 norm** gives Euclidean length; **L1 norm** is used in Lasso regularization
- **Unit vectors** have magnitude 1; normalization is crucial before similarity computation
- **Cosine similarity** measures angle between vectors, ignoring magnitude
- **Broadcasting** allows operations on different-shaped arrays following clear rules

### Part 2 — Matrices
- A **matrix** is a 2D array; rows = samples, cols = features in ML
- Matrix multiplication `@` requires matching inner dimensions
- **Transpose** flips rows and columns — essential in backpropagation
- **Determinant** tells you if a matrix is invertible
- **`np.linalg.solve()`** is the correct way to solve linear systems
- **Eigenvalues/vectors** reveal the natural axes of a transformation — fundamental for PCA

### Part 3 — ML Application
- Every ML dataset is a **feature matrix** `X` of shape (samples, features)
- Neural network forward passes are **chains of matrix multiplications**
- **Vectorization** is non-negotiable for performance — eliminate Python loops
- **Shape debugging** is the most important skill — print shapes at every step

---

## 💡 Learning Tips

1. **Code every formula yourself** — don't just read. Open a notebook and verify each result manually
2. **Draw the shapes** — before every `@` operation, write the shapes on paper and verify compatibility
3. **Build intuition visually** — use `matplotlib` to visualize vectors, transformations, and PCA
4. **Connect to ML** — after each concept, ask "where does this appear in a neural network or algorithm?"
5. **Use assertions** — add `assert X.shape == (100, 5)` statements throughout your ML code
6. **Master broadcasting** — it's confusing at first but becomes intuitive with practice

---

## 📝 Practice Recommendations

### Beginner
- [ ] Implement dot product manually and verify with `np.dot`
- [ ] Create a feature matrix for a toy dataset and slice rows/columns
- [ ] Normalize a dataset using L2 norm and verify unit vectors

### Intermediate
- [ ] Implement linear regression using the normal equation `w = (XᵀX)⁻¹Xᵀy`
- [ ] Build a from-scratch neural network forward pass using only NumPy
- [ ] Implement cosine similarity for a simple document retrieval system

### Advanced
- [ ] Implement PCA from scratch using `np.linalg.eig` on the covariance matrix
- [ ] Solve a system of linear equations and verify with `np.allclose`
- [ ] Implement gradient descent for linear regression using only matrix operations
- [ ] Explore SVD with `np.linalg.svd` and reconstruct a matrix using the top-k components

---

## 📦 Setup & Imports

```python
# Standard imports for all code in this guide
import numpy as np
import matplotlib.pyplot as plt  # for visualization

# Check version
print(f"NumPy version: {np.__version__}")

# Global settings
np.random.seed(42)              # Reproducibility
np.set_printoptions(precision=4, suppress=True)  # Clean output
```

---

*Made with 💙 for AI/ML learners | Feel free to fork, contribute, and share*

> **Next Steps:** After mastering this guide, explore:
> - `scipy.linalg` for advanced decompositions (LU, QR, SVD)
> - `sklearn.preprocessing` for production-ready normalization
> - `torch.linalg` or `tf.linalg` for GPU-accelerated linear algebra
