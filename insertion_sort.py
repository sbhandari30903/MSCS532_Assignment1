def insertion_sort(arr):
    for i in range(len(arr)-1):
        key = arr[i+1]
        j = i
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


if __name__ == "__main__":
    a = [2,445,2434,123345435,564,13]
    print("Original array:", a)
    insertion_sort(a)
    print("Sorted array:", a)