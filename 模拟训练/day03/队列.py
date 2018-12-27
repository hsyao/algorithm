"""


"""


class Queue(object):
    """队列"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        """判断是否为空"""
        return self.items == []

    def enqueue(self, item):
        """进队列"""
        self.items.append(item)

    def dequeue(self):
        """出队列"""
        return self.items.pop(0)

    def size(self):
        """返回大小"""
        return len(self.items)


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue("hello")
    queue.enqueue("world")
    queue.enqueue("itcast")

    print(queue.size())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())