# Python3 implementation of QuickSort


# Function to find the partition position
def partition(array, low, high):

	# Choose the rightmost element as pivot
	pivot = array[high]

	# Pointer for greater element
	i = low - 1

	# Traverse through all elements
	# compare each element with pivot
	for j in range(low, high):
		if array[j] <= pivot:

			# If element smaller than pivot is found
			# swap it with the greater element pointed by i
			i = i + 1

			# Swapping element at i with element at j
			(array[i], array[j]) = (array[j], array[i])
			print(array)

	(array[i + 1], array[high]) = (array[high], array[i + 1])

	return i + 1


def quicksort(array, low, high):
	if low < high:

		pi = partition(array, low, high)

		quicksort(array, low, pi - 1)


		quicksort(array, pi + 1, high)



if __name__ == '__main__':
	array = [2,8,7,1,3,5,6,4]
	N = len(array)


	quicksort(array, 0, N - 1)
	print('Sorted array:')
	for x in array:
		print(x, end=" ")

