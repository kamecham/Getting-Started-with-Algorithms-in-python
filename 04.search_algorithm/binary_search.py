# 二分探索
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 11


def binary_search(list_data, target_num):
    left = 0
    right = len(list_data) - 1
    found_flag = False
    while left <= right:
        mid = (left + right)//2
        if list_data[mid] == target_num:
            print(mid + 1)
            found_flag = True
            break
        elif list_data[mid] < target_num:
            left = mid + 1
        else:
            right = mid - 1
    if not found_flag:
        print("not target number")


binary_search(data, target)
