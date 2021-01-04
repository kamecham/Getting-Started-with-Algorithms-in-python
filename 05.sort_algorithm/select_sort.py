# 選択ソート
data = [5, 1, 2, 3, 4, 14, 10, 9, 7, 2, 3, 7, 1, 0]


def select_sort(list_data):
    """
    Perform a selection sort on the given list.
    """
    for i in range(len(list_data)):
        min = i
        for num in range(i+1, len(list_data)):
            if list_data[min] > list_data[num]:
                min = num
        buf = list_data[i]
        list_data[i] = list_data[min]
        list_data[min] = buf
    print(list_data)


select_sort(data)
