"""


"""


def binary_search(alist, item):
    """非递归实现"""
    first = 0
    last = len(alist) - 1

    while first <= last:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            return True
        elif alist[midpoint] > item:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return False


alist = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
print(binary_search(alist, 17))
print(binary_search(alist, 13))
print(binary_search(alist, 55))


def recursive_search(alist, item):
    """递归实现"""

    if len(alist) == 0:
        return False

    else:
        midpoint = len(alist) // 2

        if alist[midpoint] == item:
            return True
        elif item < alist[midpoint]:
            return recursive_search(alist[:midpoint], item)
        else:
            return recursive_search(alist[midpoint + 1:], item)


alist = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
print(recursive_search(alist, 17))
print(recursive_search(alist, 13))
print(recursive_search(alist, 55))
print(recursive_search(alist, 0))
