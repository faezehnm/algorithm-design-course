def bubbleSort(arr, k):
    n = len(arr)

    for i in range(k):

        swapped = False

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if swapped == False:
            break


arr = [64, 11, 25, 12, 22, 11, 11]
k=3

bubbleSort(arr, k)

print("kth largest :")

print("%d" % arr[len(arr)-k])
