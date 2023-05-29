def has_cycle(head):
    val = list()
    curr = head
    while curr != None:
        if curr in val:
            return 1
        val.append(curr)
        curr = curr.next
    return 0