def magic_index(array, floor, ceiling):
    mid = (floor + ceiling) // 2
    if array[mid] == mid:
        return mid
    if array[mid] < mid:
        return magic_index(array, mid+1, ceiling)
    if array[mid] > mid:
        return magic_index(array, floor, mid-1)
    
array = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]
ix = magic_index(array, 0, len(array)-1)
