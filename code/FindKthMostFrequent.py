def bubbleSort(dic, k):

    n = len(dic)
    arr = list(dic.items())

    for i in range(k):

        swapped = False

        for j in range(0, n - i - 1):

            if arr[j][1] > arr[j + 1][1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if swapped == False:
            break

    print("kth frequent :")
    print("%d" % arr[len(arr) - k][0])


def kth_mostFrequentNumber(arr, k):

    dic = {}
    n = len(arr)

    for i in range(n):
        if arr[i] in dic:
            dic[arr[i]] += 1
        else:
            dic[arr[i]] = 1
    bubbleSort(dic, k)



arr = [3, 1, 4, 4, 5, 2, 6, 1,1]
k = 1
kth_mostFrequentNumber(arr, k)