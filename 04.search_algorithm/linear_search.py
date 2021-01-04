# 線形探索
data = [1, 2, 3, 4, 5, 6, 7]
target_num = 10
found = False


def linear_search(list_data, target_num, found_flag):
    """
    Performs a linear search on the list given as an argument.
    If the target number is included, the element number of the list is displayed.
    If the list does not contain the target number, not target number will be displayed.
    """
    for i in range(len(list_data)):
        if list_data[i] == target_num:
            found_flag = True
            print(i+1)
            break
    if not found_flag:
        print("not target number")


linear_search(data, target_num, found)
