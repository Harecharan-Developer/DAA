def count_students_out_of_order_n2(n, heights):
    count = 0  # Initialize the count of students out of order

    for i in range(n):
        for j in range(i + 1, n):
            if i < j and heights[i] > heights[j]:
                count += 1

    return count

def merge(arr, left, mid, right):
    inversions = 0
    left_subarray = arr[left:mid + 1]
    right_subarray = arr[mid + 1:right + 1]

    i = 0
    j = 0
    k = left

    while i < len(left_subarray) and j < len(right_subarray):
        if left_subarray[i] > right_subarray[j]:
            inversions += len(left_subarray) - i
            arr[k] = right_subarray[j]
            j += 1
        else:
            arr[k] = left_subarray[i]
            i += 1
        k += 1

    while i < len(left_subarray):
        arr[k] = left_subarray[i]
        i += 1
        k += 1

    while j < len(right_subarray):
        arr[k] = right_subarray[j]
        j += 1
        k += 1

    return inversions

def merge_sort_and_count_inversions(arr, left, right):
    inversions = 0

    if left < right:
        mid = (left + right) // 2
        inversions += merge_sort_and_count_inversions(arr, left, mid)
        inversions += merge_sort_and_count_inversions(arr, mid + 1, right)
        inversions += merge(arr, left, mid, right)

    return inversions

def count_students_out_of_order_nlogn(n, heights):
    heights_copy = heights.copy()
    inversions = merge_sort_and_count_inversions(heights_copy, 0, n - 1)
    return inversions

if __name__ == "__main__":
    n = int(input())
    heights = list(map(int, input().split()))

    # Calculate the number of students out of order using the O(n^2) algorithm
    result_n2 = count_students_out_of_order_n2(n, heights)

    # Calculate the number of students out of order using the O(n log n) algorithm
    result_nlogn = count_students_out_of_order_nlogn(n, heights)

    print(result_n2)
    print(result_nlogn)
