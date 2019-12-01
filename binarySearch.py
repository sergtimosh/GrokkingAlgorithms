def binary_search(list, item):
    low = 0
    high = len(list) - 1
    count = 0
    while low <= high:
        count += 1
        mid = (low + high) // 2
        guess = list[mid]
        print(count,"th try-",guess)
        if guess == item:
            print("tries=",count)
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    print("tries=",count, "\nNot Found")


my_list = [1, 3, 5, 7, 9, 24, 22, 34, 55, 345, 444]

print(binary_search(my_list, 9))
print(binary_search(my_list, 55555))
