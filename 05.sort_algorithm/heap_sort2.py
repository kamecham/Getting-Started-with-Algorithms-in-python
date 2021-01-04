def heapify(data, i):
    left = 2 * i + 1
    right = 2 * i + 2
    size = len(data) - 1
    min = i

    if left <= size and data[min] > data[left]:
        min = left
    if right <= size and data[min] > data[right]:
        min = right
    if min != i:
        data[i], data[min] = data[min], data[i]
        heapify(data, min)
data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
print("対象データ：")
print(data)

# ヒープを構成
for i in reversed(range(len(data) // 2)):
    heapify(data, i)
print("初期ヒープ構成：")
print(data)

# ソートを実行
sorted_data = []
print("ソート開始")
for i in range(len(data)):
    print(i + 1, "周目")
    data[0], data[-1] = data[-1], data[0]
    sorted_data.append(data.pop())
    heapify(data, 0)
    print("sorted_data[]:")
    print(sorted_data)
    print("data[]:")
    print(data)

print("ソート結果")
print(sorted_data)