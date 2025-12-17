# Merge sort

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left_sort = merge_sort(left)
    right_sort = merge_sort(right)

    return merge(left_sort,right_sort)

def merge(left,right):
    sort_arr = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sort_arr.append(left[i])
            i+=1
        else:
            sort_arr.append(right[j])
            j+=1

        sort_arr.extend(left[i:])
        sort_arr.extend(right[j:])

        return sort_arr
    


# QUick sort O(n log n)

def quick_sort(arr):
    if len(arr) < 1:
        return arr
    
    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    mid = [z for z in arr if z == pivot]
    right = [y for y in arr if y < pivot]

    return quick_sort(left) + mid + quick_sort(right)


# Buble sort

def buble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped=True

        if not swapped:
            break

    return arr

# Insertion sort

def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -=1
        arr[j + 1] = key
        
    return arr