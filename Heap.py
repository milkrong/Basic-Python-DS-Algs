# the maximum number of items that can be stored in the heap
CAPACITY = 10


class Heap(object):

    def __init__(self):
        # create an array with as many slot as the CAPACITY
        self.heap = [0] * CAPACITY
        # we want to track the size (the number of items in the heap)
        self.heap_size = 0

    # insertion takes O(1) running time BUT we have to make sure that the
    # heap properties are not violated (it takes O(logN) because of the fixUp() method)
    def insert(self, item):

        # we are not able to insert more items than the value of the CAPACITY
        if CAPACITY == self.heap_size:
            return

        # insert the item + increment the counter
        self.heap[self.heap_size] = item
        self.heap_size = self.heap_size + 1

        # we insert the item to the last position of the array: of course the heap
        # properties may be violated so we have to fix it if necessary
        self.fix_up(self.heap_size - 1)

    # we consider the last item and checks whether swaps are needed or not
    # running time: O(logN)
    def fix_up(self, index):

        # the parent index of the given node in the heap
        # we store the heap in an array (!!!)
        parent_index = (index - 1) // 2

        # while the index>0 means until we consider all the items "above" the one we inserted
        # we have to swap the node with the parent if the heap property is violated
        # it is a MAX HEAP: largest items are in the higher layers (max item == root node)
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.swap(index, parent_index)
            self.fix_up(parent_index)

    # we return the root node. Because it is a max heap the root is the max item
    # of course because of the array representation it takes O(1) time
    # this is the peek() method
    def get_max(self):
        return self.heap[0]

    # it returns the maximum item + removes it from the heap
    # note: we just do not care about that item any more but because
    # we have an array with fix size we are not able to get rid of it completely
    # O(logN)
    def poll(self):

        max = self.get_max()

        self.swap(0, self.heap_size - 1)
        self.heap_size = self.heap_size - 1

        self.fix_down(0)

        return max

    # we have a given item in the heap and we consider all the item BELOW and check
    # whether the heap properties are violated or not
    def fix_down(self, index):

        # every node have  children: left child and right child
        # in the array the node i has left child with index *i+1 and right child with index 2*i+1
        index_left = 2 * index + 1
        index_right = 2 * index + 2
        # max heap so the parent node is always greater than the children
        index_largest = index

        # if the left child is greater than the parent: largest is the left node
        if index_left < self.heap_size and self.heap[index_left] > self.heap[index]:
            index_largest = index_left

        # if the right child is greater than the left child: largest is the right node
        if index_right < self.heap_size and self.heap[index_right] > self.heap[index_largest]:
            index_largest = index_right

        # we do not want to swap items with themselves
        if index != index_largest:
            self.swap(index, index_largest)
            self.fix_down(index_largest)

    # we have N items and we want to sort them with a heap
    # every poll() operation takes O(logN) time because of the fixDown() method thats why
    # the overall running time complexity is O(NlogN) for heapsort
    def heap_sort(self):

        # we decrease the size of the heap in the poll() method so we have to store it (!!!)
        size = self.heap_size

        for i in range(0, size):
            max = self.poll()
            print(max)

    # swap two items with (index1,index2) in the heap array
    def swap(self, index1, index2):
        self.heap[index2], self.heap[index1] = self.heap[index1], self.heap[index2]


if __name__ == "__main__":
    heap = Heap()

    heap.insert(10)
    heap.insert(8)
    heap.insert(12)
    heap.insert(20)
    heap.insert(-2)
    heap.insert(0)
    heap.insert(1)
    heap.insert(321)

    heap.heap_sort()