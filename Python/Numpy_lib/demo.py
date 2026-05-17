import numpy as np
# 1. Initialize the modern random number generator with a seed for reproducibility
rng = np.random.default_rng(seed=42)


# print("=================== 1.Array Creation ========================== ")
# 1D Array (Vector)
# print("====== 1D Array (vector)======")
# my_list = [1, 2, 3, 4, 5]
# arr_1d = np.array(my_list)
# print(arr_1d)
# print("\n")

#2D Array (Matrix / Grid)
# print("====== 2D Array (Matrix / Grid)======")
# my_matrix = [[1, 2, 3], [4, 5, 6]]
# arr_2d = np.array(my_matrix)
# print(arr_2d)
# print("\n")

# array of zeros 
# print("====== Array of zeros ======")
# zeros_1D = np.zeros(5)
# print(zeros_1D)
# print("\n")


#3x3 matrix of zeros
# print("====== 3x3 matrix of zeros ======")
# zeros_2D = np.zeros((3,3))
# print(zeros_2D)
# print("\n")

# array of ones
# print("====== Array on ones ======")
# ones_1D = np.ones(5)
# print(ones_1D)
# print("\n")

#3x3 matrix of 1s
# print("====== 3x3 matrix of 1s ======")
# ones_2D = np.ones((3,3))
# print(ones_2D)
# print("\n")


#Identity matrix 3x3
# print("====== Identity matrix 3x3 ======")
# mat_id = np.identity(4)
# print(mat_id)
# print("\n")


# Evenly space numbers between 0 and 1
# print("======= Evenly space numbers between 0 and 1 ======")
# even_space = np.linspace(0, 1, 5)
# print(even_space)
# print("\n")

# # 3x3 Array of random floats
# print("====== 3x3 Array of random floats ======")
# print(rng.random((3,3)))

# print("=========================== 2. Operations ==========================")

# a = np.array([1,2,3,4,5])
# b = np.array([10,20,30,40,50])
# print("element-wise sum, difference, product, and division.")
# print(f"A : {a}")
# print(f"B : {b}")
# print(f"Sum of A and B : {a+b}")
# print(f"Subtract of A and B : {b-a}")
# print(f"Multiplication of A and B : {a*b}")
# print(f"Division of A and B : {b/a}")

# print("Broadcasting: add a scalar to every element")
# a100 = a+100
# print(a100)
# ax2 = a100*2
# print(ax2)

# print("Computing the square root of each element")
# arr = np.array([4,9,16,25,36,49])
# a_root = np.sqrt(arr)
# print(a_root)

# print("Reshape a 1D in 2D matrix:")
# arr2 = np.arange(1,13)
# arr2_matrix = arr2.reshape(3,4)
# print(arr2)
# print(arr2_matrix)
# print(arr2_matrix.shape)
# print(arr2_matrix.ndim)
# print(arr2_matrix.size)

# print("Create a 2×3 matrix and TRANSPOSE it into a 3×2 matrix.")

# m = np.array([[1,2,3],[4,5,6]])
# print(m.shape)
# t = m.T
# print(t.shape)

# print("Stack arrays vertically and horizontally")
# a = np.array([1,2,3])
# b = np.array([4,5,6])
# print(a,b)
# c = np.vstack([a,b])
# d = np.hstack([a,b])
# print(c)
# print(d)

# print("Slice rows and columns from a 2D array")
# m = np.arange(1,17).reshape(4,4)
# print(f"Complete 2D array: \n{m}")
# print(f"Slicing First 2 rows: \n{m[0:2]}")
# print(f"Slicing Last row: \n{m[:,-1]}")
# print(f"Slicing inner 2x2: \n{m[1:3,1:3]}")

# print("Boolean Masking: Filter element")
# arr = np.array([3,15,7,42,1,28,9])
# print(arr)
# print(arr[arr>10])
# arr[arr<10] = 0
# print(arr)

# print("Facny indexing - specific elements")
# arr = np.array([10,20,30,40,50,60])
# print(arr)
# print(arr[[0,2,5]])

# print("Compute mean, median, std, min, max")
# score = np.array([88,72,95,60,45,91,78])
# print(f"Mean: {np.mean(score)}")
# print(f"Median: {np.median(score)}")
# print(f"Max: {np.max(score)}")
# print(f"Min: {np.min(score)}")
# print(f"Standard Dev: {np.std(score)}")
# print(f"Argument Max: {np.argmax(score)}")

# print("Column-wise and row-wise sum on a 2D array")
# m = np.array([[1,2,3],
#               [4,5,6],
#               [7,8,9]])
# print(f"Sum of elements Column wise: {np.sum(m, axis=0)}")
# print(f"Sum of elements Row wise: {np.sum(m, axis=1)}")
# print(f"Total sum: {np.sum(m)}")

# print("Normalise an array to 0–1 range: ")
# data = np.array([10,20,30,40,50])
# dataMax = np.max(data)
# dataMin = np.min(data)
# Normalised = data-dataMin/dataMax-dataMin
# normalised = (data - data.min()) / (data.max() - data.min())
# print(Normalised)
# print(normalised).

# print("Find unique values and their count: ")
# arr = np.array([3,1,4,1,5,9,2,6,5,3,5])
# print(arr)
# vals, counts = np.unique(arr, return_counts=True)
# print(vals)
# print(counts)

# print("Matrix multiplication with dot product: ")
# A = np.array([[1,2,3],[4,5,6]]) #2x3
# B = np.array([[7,8],[9,10],[11,12]]) #3x2
# C = np.dot(A,B)
# print(C)

print("Solve a system of linear equations")

# 2x + y  = 8
# x  + 3y = 19

A = np.array([[2,1],[1,3]])
b = np.array([8,19])

xy = np.linalg.solve(A,b)
print("2x + y  = 8")
print("x  + 3y = 19")
print(f"[x, y]:{xy}")
print(f"[c1,c2]{np.dot(A,xy)}")