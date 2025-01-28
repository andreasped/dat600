import time

def insertion_sort(arr):
    n = len(arr)

    if n <= 1:
        return
    
    # Iterate over the array starting from the second element
    for i in range(1, n):
        # Store the current element as the key to be inserted in the right position
        key = arr[i]
        j = i-1
        # Move elements greater than key one position ahead
        while j >= 0 and key < arr[j]:
            # Shift elements to the right
            arr[j+1] = arr[j]
            j -= 1
        # Insert the key in the right position
        arr[j+1] = key

    # Return the number of steps and the length of the array
    return 

arr1000 = [i for i in range(1000, 0, -1)]
arr100 = [i for i in range(100, 0, -1)]
arr10 = [i for i in range(10, 0, -1)]

array_list = [arr10, arr100, arr1000]   

times = []

for arr in array_list:
    start_time = time.time()
    insertion_sort(arr)
    end_time = time.time()
    elapsed_time_ms = (end_time - start_time) * 1000 # Convert to milliseconds
    times.append(elapsed_time_ms)


print(f"Time taken for array of length 10: {times[0]} ms")
print(f"Time taken for array of length 100: {times[1]} ms")
print(f"Time taken for array of length 1000: {times[2]} ms")

