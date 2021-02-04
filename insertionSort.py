


A = [1,6,2,8,3,4]

for i in range(1, (len(A)): #= 1 to (length of A)-1
	temp = A[i]
	j = i-1
	while(j >= 0 and A[j] > temp):
		A[j+1] = A[j]
		print('Swapping', A)
		j = j-1
	A[j+1] = temp
	print(A)