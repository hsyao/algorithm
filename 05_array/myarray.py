"""
#
# 1) Insertion, deletion and random access of array
# 2) Assumes int for element type
#
# Author: Wenru
#

"""
from typing import Optional


class MyArray(object):
    """A simple wrapper around List.
    You cannot have -1 in the array.
    """

    def __init__(self, capacity: int):
        self._data = []
        self._count = 0
        self._capacity = capacity

    def __getitem__(self, index: int) -> int:
        return self._data[index]

    def find(self, index: int) -> Optional[int]:
        if index >= self._count or index < -self._count:
            return None
        return self._data[index]

    def delete(self, index: int) -> bool:
        if index >= self._count or index < -self._count:
            return False
        # self._data[index:self._count - 1] = self._data[index + 1:]
        self._data[index:-1] = self._data[index + 1:]

        self._count -= 1
        # 真正将数据删除并覆盖原来的数据 ，这个需要增加
        self._data = self._data[:self._count]
        # print(self._data)

        return self._data[index]

    def insert(self, index: int, value: int) -> bool:
        """
        支持任意位置插入
        :param index:
        :param value:
        :return:
        """
        # 如果还有空间，那么插入位置大于当前的元素个数，可以插入最后的位置
        if self._capacity == self._count:
            return False
        if index >= self._count:
            self._data.append(value)
        elif index <= 0:
            self._data.insert(0,value)
        else:
            self._data.insert(index, value)
        self._count += 1
        return True

    def insert_to_tail(self, value: int) -> bool:
        if self._capacity == self._count:
            return False
        self._data.append(value)
        self._count += 1
        return True

    def __str__(self):
        return " ".join(str(num) for num in self._data)

    def print_all(self):

        for num in self._data[:self._count]:
            print(f"{num}", end=" ")
        print("\n", flush=True)


def test_myarray():
    array_a = MyArray(6)
    for num in range(6):
        array_a.insert_to_tail(num)
    assert array_a.find(0) == 0
    assert array_a[0] == 0
    array_a.delete(0)
    assert array_a[0] == 1


if __name__ == "__main__":
    a = MyArray(6)
    for i in range(6):
        a.insert_to_tail(i)
    print(a)
    a.delete(2)
    print(a)
    a.insert_to_tail(7)
    print(a)
    print('origin', a)
    a.delete(4)
    print('delete ', a)

    a.insert(100, 10000)
    print(a)
