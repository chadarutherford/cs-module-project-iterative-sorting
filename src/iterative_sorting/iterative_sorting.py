# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[j] <= arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap

        # swapping with temp variable
        # temp_item = arr[smallest_index]
        # arr[smallest_index] = arr[cur_index]
        # arr[cur_index] = temp_item

        # swapping with python swap syntax
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(0, len(arr) - 1 - i, 1):
            if arr[j] > arr[j + 1]:
                
                # swapping with temp variable
                # temp_item = arr[j]
                # arr[j] = arr[j + 1]
                # arr[j + 1] = temp_item

                # swapping with python swap syntax
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# requires us to know the "max" value that we'll be sorting
# the maximum arg was so that  we could specify the max value
# The total range of data we'll be sorting sits between 0 and maximum
def count_sort(arr, maximum=-1):
    if len(arr) == 0:
        return arr

    # if maximum is not given, we will take the max value from the input array
    if maximum == -1:
        maximum = max(arr)

    # make a bunch of buckets
    buckets = [0 for _ in range(maximum + 1)]

    for x in arr:
        if x < 0:
            return "Error, negative numbers not allowed in Count Sort"
        buckets[x] += 1

    # we now have a count of every value in the array
    # loop through the buckets starting at the smallest index
    j = 0
    for i in range(len(buckets)):
        while buckets[i] > 0:
            arr[j] = i
            j += 1
            buckets[i] -= 1
    return arr


array = [1, 2, 3, 4, 6, 3, 4, 2, 4, 3, 1, 0, 6 ,0]
print(f"Array before sort: {array}")
count_sort(array)
print(f"Array after sort: {array}")