X = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# iterate through rows
for row in range(len(X)):
	# iterate through columns
	for column in range(len(X[0])):
		result[column][row] = X[row][column]

for r in result:
	print(r)
	
# # Python Program to Transpose a Matrix using the list comprehension

# rez = [[X[column][row] for column in range(len(X))] 
# for row in range(len(X[0]))]

# for row in rez:
#	 print(row)
