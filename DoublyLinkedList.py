class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while(last.next is not None):
            last = last.next

        last.next = new_node
        new_node.prev = last

        return

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("The given node could not be None")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node

        if new_node.next is not None:
            new_node.next.prev = new_node

    def print_list(self, first_node):
        while first_node is not None:
            print(first_node.data,end=" ")
            last = first_node
            first_node = first_node.next

if __name__ == "__main__":
    # Start with empty list
    llist = DoubleLinkedList()

    # Insert 6. So the list becomes 6->None
    llist.append(6)

    # Insert 7 at the beginning.
    # So linked list becomes 7->6->None
    llist.push(7)

    # Insert 1 at the beginning.
    # So linked list becomes 1->7->6->None
    llist.push(1)

    # Insert 4 at the end.
    # So linked list becomes 1->7->6->4->None
    llist.append(4)

    # Insert 8, after 7.
    # So linked list becomes 1->7->8->6->4->None
    llist.insert_after(llist.head.next, 8)

    print("Created DLL is: ")
    llist.print_list(llist.head)


