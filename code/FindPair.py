def findPair(arr, x):

    n = len(arr)
    l, r = 0, n - 1

    while r > l:
        if arr[l] + arr[r] == x :
            print('pair is: {} and {}'
                  .format(arr[l], arr[r]))
            return 1

        if arr[l] + arr[r] > x:
            r -= 1

        else:
            l += 1

    return -1

def bubbleSort(arr):
    n = len(arr)

    for i in range(n):

        swapped = False

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if swapped == False:
            break

arr = [22, 40, 28, 10, 30, 29,34, 26]
bubbleSort(arr)

x = 68
findPair(arr, x)

