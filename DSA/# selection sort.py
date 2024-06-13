# selection sort

import sys
A =[45,15,6,8,201,13,503,69,1]

for i in range(len(A)):
	min_idx = i
	for j in range(i+1, len(A)):
		if A[min_idx] > A[j]:
			min_idx = j
				 
	A[i], A[min_idx] = A[min_idx], A[i]


print ("Sorted array:",A)
