class Node(object):

    def __init__(self, name):
        self.name = name
        self.adjacencies = None
        self.visited = True
        self.predecessor = None

class DepthFirstSearch(object):
    
    def dfs(self, node):
        node.visited = True
        print(node.name)

        for v in node.adjacencies:
            if not v.visited:
                self.dfs(v)
