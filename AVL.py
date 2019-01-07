class Node(object):

    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None
        self.height = 0

class AVL(object):

    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if not node:
            return Node(data)

        if data < node.data:
            node.left_child = self.insert_node(data, node.left_child)
        else:
            node.right_child = self.insert_node(data, node.right_child)

        node.height = max(self.get_height(node.left_child), self.get_height(node.right_child)) + 1

        return self.settle_violation(data, node)

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

        if not node:
            return node

        node.height = max(self.get_height(node.left_child), self.get_height(node.right_child)) + 1

        balance = self.calc_balanced(node)

        if balance > 1 and self.calc_balanced(node.left_child) >= 0:
            return self.rotate_right(node)

        if balance < -1 and self.calc_balanced(node.right_child) <= 0:
            return self.rotate_left(node)

        if balance > 1 and self.calc_balanced(node.left_child) < 0:
            node.left_child = self.rotate_left(node.left_child)
            return self.rotate_right(node)

        if balance < -1 and self.calc_balanced(node.right_child) > 0:
            node.right_child = self.rotate_right(node.right_child)
            return self.rotate_left(node)

        return node

    def get_pred(self, node):

        if node.right_child:
            return self.get_pred(node.right_child)

        return node

    def remove(self, data):
        if self.root:
            self.root = self.removeNode(data, self.root)

    def settle_violation(self, data, node):

        balance = self.calc_balanced(node)
        #case 1 left left
        if balance > 1 and data < node.left_child.data:
            return self.rotate_right(node)

        if balance < -1 and data > node.right_child.data:
            return self.rotate_left(node)

        if balance > 1 and data > node.left_child.data:
            node.left_child = self.rotate_left(node.left_child)
            return self.rotate_right(node)

        if balance < -1 and data < node.right_child.data:
            node.right_child = self.rotate_right(node.right_child)
            return self.rotate_left(node)

        return node

    def get_height(self, node):

        if not node:
            return -1

        return node.height

    def calc_balanced(self, node):
        # if return > 1, make a right rotation, if < -1, make a left rotation
        if not node:
            return -1

        return self.get_height(node.left_child) - self.get_height(node.right_child)

    def rotate_right(self, node):
        tmp_left_child = node.left_child
        t = tmp_left_child.right_child

        tmp_left_child.right_child = node
        node.left_child = t
        node.height = max(self.get_height(node.left_child), self.get_height(node.right_child)) + 1
        tmp_left_child.height = max(self.get_height(tmp_left_child.left_child),
                                    self.get_height(tmp_left_child.right_child)) \
                                + 1

        return tmp_left_child

    def rotate_left(self, node):
        tmp_right_child = node.right_child
        t = tmp_right_child.left_child

        tmp_right_child.left_child = node
        node.right_child = t
        node.height = max(self.get_height(node.left_child), self.get_height(node.right_child)) + 1
        tmp_right_child.height = max(self.get_height(tmp_right_child.left_child),
                                    self.get_height(tmp_right_child.right_child)) \
                                + 1

        return tmp_right_child

    def traverse(self):
        if self.root:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        if node.left_child:
            self.traverse_in_order(node.left_child)

        print(node.data)

        if node.right_child:
            self.traverse_in_order(node.right_child)

if __name__ == "__main__":
    avl = AVL()
    avl.insert(5)
    avl.insert(4)
    avl.insert(3)

    avl.remove(5)

    avl.traverse()