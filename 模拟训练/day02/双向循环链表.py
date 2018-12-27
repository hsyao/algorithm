"""


"""


class Node(object):
    def __init__(self, item):
        self.item = item
        self.prev = None
        self.next = None


class SingleCycleLinkList(object):
    def __init__(self):
        self.__head = None

    def is_empty(self):
        """ 判断链表是否为空"""
        return self.__head is None

    def length(self):
        """返回链表的长度"""
        if self.is_empty():
            return 0
        elif self.__head.next == self.__head:
            return 1
        else:
            count = 1
            cur = self.__head
            while cur.next != self.__head:
                count += 1
                cur = cur.next
            return count

    def travel(self):
        """遍历"""
        if self.length() == 0:
            return
        elif self.length() == 1:
            print(self.__head.item)
        else:
            cur = self.__head
            while cur.next != self.__head:
                print(cur.item)
                cur = cur.next

    def add(self, item):
        """在头部添加一个节点"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            node.next = self.__head
            self.__head.prev = node
            if self.length() == 1:
                self.__head = node
            else:
                cur = self.__head
                while cur.next != self.__head:
                    cur = cur.next
                self.__head = node
                cur.next = self.__head

    def append(self, item):
        """在尾部添加一个节点"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            pass
