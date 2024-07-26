def bubble_sort_descending(arr):
    n = len(arr)

    for i in range(n):
     
        for j in range(0, n-i-1):
           
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


numbers = [2, 3, 4, 5, 6]
sorted_numbers = bubble_sort_descending(numbers)

print("Sorted list in descending order:", sorted_numbers)
