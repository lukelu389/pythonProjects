def has_cycle(head):
    pointer_1 = head
    pointer_2 = head
    while pointer_2 and pointer_2.next:
        pointer_2 = pointer_2.next.next
        pointer_1 = pointer_1.next

        if pointer_1 == pointer_2:
            return True

    return False


