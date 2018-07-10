class Stack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

if __name__ == "__main__":
    def revstring(mystr):
        s = Stack()
        output_string = ""
        for c in mystr:
            s.push(c)
        while not s.is_empty():
            output_string += s.pop()

        return output_string

    def dec_to_bin(dec_number):
        bin_string = ""
        s = Stack()

        while dec_number > 0:
            digit = dec_number % 2
            s.push(digit)
            dec_number = dec_number // 2

        while not s.is_empty():
            bin_string += str(s.pop())

        return bin_string

    print(revstring("apple"))

    print(dec_to_bin(42))
