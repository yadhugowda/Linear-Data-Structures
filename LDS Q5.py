def findDuplicates(arr, Len):
    ifPresent = False

    a1 = []
    for i in range(Len - 1):
        for j in range(i + 1, Len):
            
            if (arr[i] == arr[j]):
                if arr[i] in a1:
                    break
                else:
                    a1.append(arr[i])
                    ifPresent = True

    if (ifPresent):
        print(a1, end = " ")
    else:
        print("No duplicates present in arrays")
arr = [ 12, 11, 40, 12, 5, 6, 5, 12, 11 ]
n = len(arr)
 
findDuplicates(arr, n)