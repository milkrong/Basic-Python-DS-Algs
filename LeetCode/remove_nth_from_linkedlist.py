def remove_n_from_end(head, n):
    '''
    Given a linked list, remove the n-th node from the end of list and return its head.
    :param head:
    :param n:
    :return:
    '''
    fast = slow = head
    for _ in range(n):
        fast = fast.next

    if not fast:
        return 0

    while fast.next:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return head
