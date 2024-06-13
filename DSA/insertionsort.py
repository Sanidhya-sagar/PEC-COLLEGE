# insertion sort

def insertionSort(arr):

	for i in range(1, len(arr)):

		key = arr[i]
		j = i-1
		while j >= 0 and key < arr[j] :
				arr[j + 1] = arr[j]
				j -= 1
		arr[j + 1] = key


arr=[45,15,6,8,201,13,503,69,1]

insertionSort(arr)
print("sorted list:",arr)

