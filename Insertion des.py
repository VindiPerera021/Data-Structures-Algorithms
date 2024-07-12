def insertion_sort_descending(arr):
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = insertion_sort_descending(numbers)
print("Sorted array in descending order is:", sorted_numbers)
