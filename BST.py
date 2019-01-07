class Node(object):

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insert_data(data, self.root)

    def insert_data(self, data, node):

        if data < node.data:
            if node.left_child:
                self.insert_data(data, node.left_child)
            else:
                node.left_child = Node(data)
        else:
            if node.right_child:
                self.insert_data(data, node.right_child)
            else:
                node.right_child = Node(data)

    def removeNode(self, data, node):
        if not node:
            return node

        if data < node.data:
            node.left_child = self.removeNode(data, node.left_child)
        elif data > node.data:
            node.right_child = self.removeNode(data, node.right_child)
        else:
            if not node.right_child and node.left_child:
                del node
                return None

            if not node.left_child:
                tmp = node.right_child
                del node
                return tmp
            elif not node.right_child:
                tmp = node.left_child
                del node
                return tmp

            tmp = self.get_pred(node.lef_child)
            node.data = tmp.data
            node.left_child = self.removeNode(tmp.data, node.left_child)

        return node

    def get_pred(self, node):

        if node.right_child:
            return self.get_pred(node.right_child)

        return node

    def remove(self, data):
        if self.root:
            self.root = self.removeNode(data, self.root)

    def min(self):

        if self.root:
            return self.get_min(self.root)

    def get_min(self, node):

        if node.left_child:
            return self.get_min(node.left_child)

        return node.data

    def max(self):

        if self.root:
            return self.get_max(self.root)

    def get_max(self, node):

        if node.right_child:
            return self.get_max(node.right_child)

        return node.data

    def traverse(self):
        if self.root:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):

        if node.left_child:
            self.traverse_in_order(node.left_child)

        print("%s" % node.data)

        if node.right_child:
            self.traverse_in_order(node.right_child)



if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.traverse()
    bst.remove(5)
    bst.traverse()

