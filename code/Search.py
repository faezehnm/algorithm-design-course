def search(arr, key):
    n = len(arr)
    found = False

    for i in range(n):
        if arr[i] == key:
            found = True
            return i

    if found == False:
        return -1

arr = [64, 11, 25, 12, 22, 11, 11]
key=12

res = search(arr, key)
if( res == -1):
    print("not found")

else:
    print("found in index :")
    print("%d" % res)