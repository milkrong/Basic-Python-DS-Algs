from LinkedLists import LinkedLists

def get_nth(node, index):
    count = 0
    if count == index:
        return node.data
    else:
        return get_nth(node.next, index-1)

def get_last_nth(list, n):
    main_ptr = list.head
    ref_ptr = list.head
    count = 0
    if list.head is not None:
        while count < n:
            if ref_ptr is None:
                print(n, "is greater than ref-ptr")
                return

            ref_ptr = ref_ptr.next
            count+=1

    while ref_ptr is not None:
        main_ptr = main_ptr.next
        ref_ptr = ref_ptr.next

    return main_ptr.data


if __name__ == '__main__':
    llist = LinkedLists()

    # Use push() to construct below list
    # 1->12->1->4->1
    llist.push(1)
    llist.push(4)
    llist.push(1)
    llist.push(12)
    llist.push(1)

    n = 3
    print(get_nth(llist.head, n))
    print(get_last_nth(llist, n))