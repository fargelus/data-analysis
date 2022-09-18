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
