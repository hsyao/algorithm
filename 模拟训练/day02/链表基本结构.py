"""


"""


class LinkList(object):
    def __init__(self):
        self._data = None
        self._next = None


node1 = LinkList()
node1._data = 10
node2 = LinkList()
node2._data = 30
node1._next = node2

print(node1._data)
print(node1._next._data)


class SingleNode(object):
    """单链表的结点"""
    def __init__(self, item):
        # item存放数据元素
        self.item = item
        # next是下一个节点的标示
        self.next = None


node3=SingleNode(50)
node4=SingleNode(100)
node3.next=node4

print(node3.item)
print(node3.next.item)