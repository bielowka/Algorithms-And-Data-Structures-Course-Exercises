def partition(first):
    pivot = first.val
    temp = first
    first = first.next
    fir_l = Node(None)
    fir_e = Node(None)
    fir_r = Node(None)
    left, right, middle = fir_l, fir_r, fir_e

    while first is not None:

        if first.val > pivot:
            right.next = first
            first = first.next
            right = right.next
            right.next = None

        elif first.val < pivot:
            left.next = first
            first = first.next
            left = left.next
            left.next = None

        else:
            middle.next = first
            first = first.next
            middle = middle.next
            middle.next = None

    middle.next = temp
    middle = middle.next
    middle.next = None
    return fir_l.next, fir_e.next, fir_r.next, middle


def get_last(first):
    if first is None:
        return None
    while first.next is not None:
        first = first.next
    return first


def connect(left, right, middle, mend):
    new_list = Node(None)
    first = new_list
    last = None
    if left is not None:
        new_list.next = left
        new_list = get_last(left)
    if middle is not None:
        new_list.next = middle
        new_list = mend
    if right is not None:
        new_list.next = right

    return first.next


def quicker_sort(first):
    if first is None:
        return first
    else:
        left, mid, right, mend = partition(first)
        left = quicker_sort(left)
        right = quicker_sort(right)
        first = connect(left, right, mid, mend)

    return first


