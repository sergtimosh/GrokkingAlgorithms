def recurSumArr(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + recurSumArr(arr[1:])

print(recurSumArr([109, 650, 777]))