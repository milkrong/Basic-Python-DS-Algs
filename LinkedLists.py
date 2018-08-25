class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedLists:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, node_to_insert, data):
        if node_to_insert is None:
            print("The position is missing")
            return
        new_node = Node(data)
        new_node.next = node_to_insert.next
        node_to_insert.next = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def remove(self, key):
        node = self.head
        if node == None:
            return

        if node.data == key:
            self.head = node.next
            node = None
            return
        else:
            while node.next is not None:
                if node.data == key:
                    break
                prev = node
                node = node.next
            prev.next = node.next
            node = None

    def reverse(self):
        prev_node = None
        current_node = self.head
        while(current_node is not None):
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node


    def print_list(self):
        data_print = self.head
        while data_print is not None:
            print(data_print.data, end=" ")
            data_print = data_print.next

if __name__ == '__main__':
    list = LinkedLists()
    list.head = Node("Mon")
    e2 = Node("Tue")
    e3 = Node("Wed")

    list.head.next = e2
    e2.next = e3

    list.push("Sun")
    list.insert_after(e3, "Thu")
    list.append("Fri")

    list.remove("Mon")

    list.print_list()

    list.reverse()

    list.print_list()

