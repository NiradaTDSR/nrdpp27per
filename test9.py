# Program to add two matrices using nested loop
X = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
Y = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# iterate through rows
for row in range(len(X)):

	# iterate through columns
	for column in range(len(X[0])):
		result[row][column] = X[row][column]+ Y[row][column]

for r in result:
	print(r)
 
Add_result = [[X[row][column] + Y[row][column]
			for column in range(len(X[0]))] 
			for row in range(len(X))]
Sub_result = [[X[row][column] - Y[row][column]
			for column in range(len(X[0]))] 
			for row in range(len(X))]

print("Matrix Addition")
for r in Add_result:
	print(r)

print("\nMatrix Subtraction")
for r in Sub_result:
	print(r)
 
rmatrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for row in range(len(X)):
	for column in range(len(X[0])):
		rmatrix[row][column] = X[row][column] * Y[row][column]
		
print("Matrix Multiplication",)
for r in rmatrix:
	print(r)
		
for i in range(len(X)):
	for j in range(len(X[0])):
		rmatrix[row][column] = X[row][column] // Y[row][column]

print("\nMatrix Division",) 
for r in rmatrix:
	print(r)


