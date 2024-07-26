def selection_sort_descending(arr):
    n = len(arr)
    
    for i in range(n):
      
        max_idx = i
        
        for j in range(i + 1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j
        
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr

numbers = [2, 3, 4, 5, 6]
sorted_numbers = selection_sort_descending(numbers)

print("Sorted list in descending order:", sorted_numbers)
