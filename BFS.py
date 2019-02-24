class Node(object):

    def __init__(self, name):
        self.name = name
        self.adjacencies = []
        self.visited = False
        self.predecessor = None

class BreadFirstSearch(object):

    def dfs(self, start_node):
        queue = []
        queue.append(start_node)
        start_node.visited = True

        while queue:
            actual_node = queue.pop(0)
            print(actual_node.name)
            for v in actual_node.adjacencies:
                if not v.visited:
                    v.visited = True
                    queue.append(v)