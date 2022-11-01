# 1. Import the numpy package under the name `np` (★☆☆)
import numpy as np

# 2. Print the numpy version and the configuration (★☆☆)
print("VERSION:", np.__version__)
print("CONFIG:")
print(np.show_config())

# 3. Create a null vector of size 10 (★☆☆)
vec = np.array([None] * 10)

# 4. How to find the memory size of any array (★☆☆)
print("TOTAL BYTES ALLOCATED:", vec.nbytes)

# 5. How to get the documentation of the numpy add function from the command line? (★☆☆)
# python3 -c "import numpy; help(numpy.add)"

# 6. Create a null vector of size 10 but the fifth value which is 1 (★☆☆)
vec1 = np.concatenate((vec[0:4], np.array([1]), vec[5:]))

# 7. Create a vector with values ranging from 10 to 49 (★☆☆)
np.arange(10, 50)

#### 8. Reverse a vector (first element becomes last) (★☆☆)
reversed = np.flip(np.arange(5))
print("REVERSED:", reversed)

#### 9. Create a 3x3 matrix with values ranging from 0 to 8 (★☆☆)
matrix = np.arange(9)
matrix.shape = (3, 3)
print(matrix)

#### 10. Find indices of non-zero elements from [1,2,0,0,4,0] (★☆☆)
arr = np.array([1, 2, 0, 0, 4, 0])
print("NONZERO:", np.flatnonzero(arr))

#### 11. Create a 3x3 identity matrix (★☆☆)
print(np.identity(3))

#### 12. Create a 3x3x3 array with random values (★☆☆)
rng = np.random.default_rng()
print(rng.integers(0, 10, size=(3, 3, 3)))

#### 13. Create a 10x10 array with random values and find the minimum and maximum values (★☆☆)
arr = rng.random(size=(10, 10))
print(arr)
print(arr.max())
print(arr.min())

#### 14. Create a random vector of size 30 and find the mean value (★☆☆)
print(rng.integers(100, size=(30)).mean())

#### 15. Create a 2d array with 1 on the border and 0 inside (★☆☆)
arr = rng.integers(100, size=(4, 4))
print("ORIG:\n", arr)

arr[0] = 1
arr[3] = 1
arr.T[0] = 1
arr.T[3] = 1
for i in range(1, 3):
    for j in range(1, 3):
        arr[i][j] = 0

print("MODIFIED:\n", arr)

#### 16. How to add a border (filled with 0's) around an existing array? (★☆☆)
a = np.array([[1, 2, 3], [2, 3, 4], [3, 5, 6]])
print(a * [np.zeros(3, dtype=int), [0, 1, 0], np.zeros(3, dtype=int)])

#### 17. What is the result of the following expression? (★☆☆)
```python
0 * np.nan # nan
np.nan == np.nan # False
np.inf > np.nan # False
np.nan - np.nan # nan
np.nan in set([np.nan]) # True
0.3 == 3 * 0.1 # False
```
