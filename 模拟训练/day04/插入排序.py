"""


"""


def insert_sort2(alist):
    n = len(alist)
    for i in range(1, n):
        for j in range(i):
            if alist[i] < alist[j]:
                insert_value = alist[i]
                alist[j+1:i + 1] = alist[j:i]
                alist[j] = insert_value


def insert_sort(alist):
    # 从第二个位置，即下标为1的元素开始向前插入
    for i in range(1, len(alist)):
        # 从第i个元素开始向前比较，如果小于前一个元素，交换位置
        for j in range(i, 0, -1):
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]


if __name__ == '__main__':
    li = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    insert_sort(li)
    print(li)
    alist = [54, 226, 93, 17, 77, 31, 44, 55, 20]
    insert_sort(alist)
    print(alist)
