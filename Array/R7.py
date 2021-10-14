def minmax(arr):
    min = max = arr[0]
    for i in arr:
        if min > i:
            min = i
        if max < i:
            max = i
    print(min)
    print(max)

print(minmax([1,2,3,4]))
