def maxArea(arr):
    arr.sort()
    area = 0
    i = 0
    j = len(arr) - 1
    while i < len(arr) and i < j:
        height = min(arr[i], arr[j])
        base = arr[j] - arr[i]
        a = base * height
        if a >= area:
            area = a
            i += 1
        else:
            j -= 1
    return area

print(maxArea([1, 5, 4, 3,6,8,9]))