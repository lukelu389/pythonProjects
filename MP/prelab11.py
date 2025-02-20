"""
Xiao Lu
420-SN1 Programming, Section #21
Winter 2025
J. Gullifer, instructor
Pre Lab Assignment #11
"""

def selection_sort(arr):
    for i in range(len(arr)):
        min_j = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_j]:
                min_j = j
        if min_j != i:
            arr[i], arr[min_j] = arr[min_j], arr[i]
    return arr

# used recursion
def binary_search(target, source, lo, hi):
    mid = (hi+lo) // 2
    if source[mid] == target:
        return mid
    elif source[mid] < target:
        return binary_search(target, source, mid+1, hi)
    elif source[mid] > target:
        return binary_search(target, source, lo, mid)
    else:
        return -1
ls = [9, -1, 2, 4, 0, 11, -5]
ls = selection_sort(ls)
print(binary_search(11, ls, 0, len(ls)-1))





