class Queue(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.size() == 0

    def enqueue(self, data):
        self.items.insert(0, data)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.items.pop()

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    q = Queue()
    q.enqueue(4)
    q.enqueue('god')
    q.enqueue(True)
    print(q.dequeue())