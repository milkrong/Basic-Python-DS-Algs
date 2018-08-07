from LinkedLists import LinkedLists

def find_middle(list):
    slow_ptr = list.head
    fast_ptr = list.head

    if list.head is not None:
        while slow_ptr is not None and fast_ptr is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next

        return slow_ptr.data
    else:
        print("the list is empty")
        return

if __name__ == "__main__":
    llist = LinkedLists()

    # Use push() to construct below list
    # 1->12->1->4->1
    llist.push(1)
    llist.push(4)
    llist.push(1)
    llist.push(12)
    llist.push(1)

    llist.print_list()
    print(find_middle(llist))