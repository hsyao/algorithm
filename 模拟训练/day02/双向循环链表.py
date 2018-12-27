"""


"""


class Node(object):
    def __init__(self, item):
        self.item = item
        self.prev = None
        self.next = None


class DCycleLinkList(object):
    def __init__(self):
        self.__head = None

    def is_empty(self):
        """ 判断链表是否为空"""
        return self.__head is None

    def length(self):
        """返回链表的长度"""
        # 链表为空
        if self.is_empty():
            return 0
        else:
            count = 1
            cur = self.__head
            # 移动到最后一个节点
            while cur.next != self.__head:
                count += 1
                cur = cur.next
            return count

    def travel(self):
        """遍历"""
        # 链表为空
        if self.is_empty():
            return
        else:
            cur = self.__head
            # 先遍历第一个节点
            print(cur.item)
            while cur.next != self.__head:
                cur = cur.next
                print(cur.item)

    def add(self, item):
        """在头部添加一个节点"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            # 添加的节点指向头节点
            node.next = self.__head
            # 头节点的指向添加的节点
            self.__head.prev = node
            # 查找尾节点
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            # 尾节点指向头节点
            self.__head = node
            cur.next = node
            # cur.next = self.__head

    def append(self, item):
        """在尾部添加一个节点"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            # 找到尾节点
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.prev = cur
            node.next = self.__head

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos < (self.length() - 1):
            self.append(item)
        else:
            count = 0
            cur = self.__head
            node = Node(item)
            # 找到插入位置的前一个节点
            while count < (pos - 1):
                cur = cur.next
                count += 1

            node.next = cur.next
            node.prev = cur
            cur.next.prev = node
            cur.next = node

    def remove(self, item):
        if self.is_empty():
            return

        cur = self.__head

        while cur.next != self.__head:
            if cur.item == item:
                # 判断是否为头节点
                if cur == self.__head:
                    cur.next.prev = None
                    self.__head = cur.next
                else:
                    # 中间节点
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                return
            cur = cur.next

        # 退出循环，cur指向尾节点
        if cur.item == item:
            # 仅有一个节点的情况
            if cur == self.__head:
                self.__head = None
            # 尾节点的情况
            else:
                cur.prev.next = self.__head

    def search(self, item):
        """查找节点是否存在"""
        if self.is_empty():
            return False
        cur = self.__head
        # 第一个节点判断是否满足条件
        if cur.item == item:
            return True
        # 判断是否为尾节点
        while cur.next != self.__head:
            cur = cur.next
            if cur.item == item:
                return True
        return False


if __name__ == '__main__':
    ll = DCycleLinkList()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2, 4)
    ll.insert(4, 5)
    ll.insert(0, 6)
    print("length:", ll.length())
    ll.travel()
    print(ll.search(3))
    print(ll.search(7))
    ll.remove(1)
    print("length:", ll.length())
    ll.travel()
