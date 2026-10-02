# NUMPY PROGRAMS Practice
# ARRRAYS

# 1. 1-D ARRAYS

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)


# 2. 2-D ARRAYS

import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)


# 3. Write a python program to create a 3-D ARRAY with 2 2-D ARRAYS in it.

import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)



# 4. Write a python program to show the attribute of the array (no. of dimensions of array)

import numpy as np

a = np.array (42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


# 5. Write a python program to access the elements of a 1-D array

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr[3], arr[2])


# 6. Write a python program to get the result of two elements in an array using arithmentic operators

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr[3] - arr[2])


# 7. Write a python program to access the elements of a 2-D array

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

row = int(input("Enter row number: "))
element = int(input("Enter element number: "))

answer = arr[row - 1, element - 1]

print(element, "element on", row, "row:", answer)



# 8. Write a python program to slice elements from index 1 to index 5 from the following array.

import numpy as np
arr = np.array ([1, 2, 3, 4, 5, 6, 7])
print (arr[1:5])


# 9. Write a python program to slice elements from indexes in reverse.

import numpy as np
arr = np.array ([1, 2, 3, 4, 5, 6, 7])
print (arr[-3:-1])


# 10. Write a python program to print alternate elements in an array.

import numpy as np
arr = np.array ([1, 2, 3, 4, 5, 6, 7])
print (arr[::2])


# 11.
import numpy as np
arr = np.array ([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print (arr[1, 1:4])


# 12.
import numpy as np
arr = np.array ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
element = arr[1,2] # Selects the element at row index 1
# column index 2 (value 6)


#13.
import numpy as np
arr = np.array ([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
row_slice = arr[0:2, :]


# 14.
import numpy as np
arr = np.array ([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
col_slice = arr [:, 1:3]
