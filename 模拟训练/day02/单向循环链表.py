"""


"""


class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleCycleLinkList(object):
    def __init__(self):
        self.__head = None

    def is_empty(self):
        """ 判断链表是否为空"""
        return self.__head is None

    def length(self):
        """返回链表的长度"""
        # 如果链表为空，返回长度0
        if self.is_empty():
            return 0
        else:
            count = 1
            cur = self.__head
            while cur.next != self.__head:
                count += 1
                cur = cur.next
            return count

    def travel(self):
        """遍历"""
        if self.is_empty():
            return
        cur = self.__head
        print(cur.item)
        while cur.next != self.__head:
            cur = cur.next
            print(cur.item)
        print("")

    def add(self, item):
        """在头部添加一个节点"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            # 添加的节点指向_head
            node.next = self.__head
            # 移到链表尾部，将尾部节点的next指向node
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            # _head指向添加node的
            self.__head = node

    def append(self, item):
        """在尾部添加一个节点"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head

    def insert(self, pos, item):
        pass

    def remove(self, item):
        """删除一个节点"""
        if self.is_empty():
            return False
        else:
            cur = self.__head
            if cur.item == item:
                return True
            while cur.next != self.__head:
                cur = cur.next
                if cur.item == item:
                    return True
            return False
        pass

    def search(self, item):
        if self.is_empty():
            return False
        else:
            cur = self.__head
            if cur.item == item:
                return True
            while cur.next != self.__head:
                cur = cur.next
                if cur.item == item:
                    return True
            return False

