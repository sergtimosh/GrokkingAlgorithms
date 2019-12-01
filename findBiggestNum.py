def recursiveMax(arr):
    if len(arr) == 0:
        return "Empty list"
    if len(arr) == 1:
        return arr[0]
    if recursiveMax(arr[1:]) > arr[0]:
        return recursiveMax(arr[1:])
    return arr[0]

print(recursiveMax([]))


