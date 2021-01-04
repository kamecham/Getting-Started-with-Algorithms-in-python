# バブルソート
data = [5, 1, 2, 3, 4, 14, 10, 9, 7, 2, 3, 7, 1, 0, 9, 20, 40, 1]


def bubble_sort(list_data):
    """
    Perform a bubble sort on the given list.
    """
    for loop_num in range(len(list_data)-1):
        for i in range(len(list_data)-loop_num-1):
            if list_data[i] > list_data[i+1]:
                list_data[i], list_data[i+1] = list_data[i+1], list_data[i]
    print(data)


print(data)
bubble_sort(data)
