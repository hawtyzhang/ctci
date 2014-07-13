class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)

def init_list(vals):
    if len(vals) == 0:
        return None
    head = Node(vals[0])
    previous = head
    for val in vals[1:]:
        node = Node(val)
        previous.next = node
        previous = node
    return head

def pretty_print(node):
    if node == None:
        print None
        return
    print node.val,
    while node.next != None:
        node = node.next
        print ' -> ',
        print node.val,
    print

def remove_duplicate_with_buffer(head):
    freq = {}
    previous = None
    while head != None:
        if head.val in freq:
            previous.next = head.next
        else:
            freq[head.val] = True
            previous = head
        head = head.next

def remove_duplicate_without_buffer(head):
    if head == None:
        return None
    end, cur = head, head.next
    while cur != None:
        runner = head
        append = True
        while runner != end.next:
            if cur.val == runner.val:
                append = False
                break
            runner = runner.next
        if append:
            end.next = cur
            end = end.next
        cur = cur.next
    end.next = None

def find_n_to_last(head, n):
    if n < 1:
        return None
    n_runner, n_last = head, head
    for i in range(n):
        if n_runner == None:
            return None
        n_runner = n_runner.next
    while n_runner != None:
        n_runner = n_runner.next
        n_last = n_last.next
    return n_last

def delete_in_middle(node):
    if node.next == None:
        raise ValueError("node cannot be the last element")
    node.val = node.next.val
    node.next = node.next.next

def sum_two_lists(list1, list2):
    def sum_two_lists_with_carry(list1, list2, carry):
        if list1 == None and list2 == None:
            if carry == 0:
                return None
            else:
                return Node(carry)
        elif list1 == None:
            node = Node((list2.val+carry)%10)
            node.next = sum_two_lists_with_carry(list1, list2.next, (list2.val+carry)/10)
        elif list2 == None:
            node = Node((list1.val+carry)%10)
            node.next = sum_two_lists_with_carry(list1.next, list2, (list1.val+carry)/10)   
        else:         
            node = Node((list1.val+list2.val+carry)%10)
            node.next = sum_two_lists_with_carry(list1.next, list2.next, (list1.val+list2.val+carry)/10)
        return node
    return sum_two_lists_with_carry(list1, list2, 0)

def begin_of_loop(head):
    if head == None:
        return None
    slow, fast = head, head
    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break
    if fast == None or fast.next == None:
        return None
    fast = head
    while fast != slow:
        fast = fast.next
        slow = slow.next
        if fast == slow:
            return fast

def test1():
    list1 = init_list([3, 2, 4, 1, 4])
    list2 = init_list([3, 3, 3, 1, 3, 3])
    list3 = init_list([3, 5, 6, 3, 4, 2, 6, 5, 9, 2])
    remove_duplicate_with_buffer(list1)
    remove_duplicate_with_buffer(list2)
    remove_duplicate_with_buffer(list3)
    pretty_print(list1)
    pretty_print(list2)
    pretty_print(list3)

def test2():
    list1 = init_list([3, 2, 4, 1, 4])
    list2 = init_list([3, 3, 3, 1, 3, 3])
    list3 = init_list([3, 5, 6, 3, 4, 2, 6, 5, 9, 2])
    remove_duplicate_without_buffer(list1)
    remove_duplicate_without_buffer(list2)
    remove_duplicate_without_buffer(list3)
    pretty_print(list1)
    pretty_print(list2)
    pretty_print(list3)

def test3():
    list1 = init_list([3, 2, 4, 1, 4])
    list2 = init_list([3, 3, 3, 1, 3, 3])
    list3 = init_list([3, 5, 6, 3, 4, 2, 6, 5, 9, 2])
    print find_n_to_last(list1, 3)
    print find_n_to_last(list2, 5)
    print find_n_to_last(list3, 2)
    print find_n_to_last(list1, 5)
    print find_n_to_last(list1, 6)
    print find_n_to_last(list1, 0)

def test4():
    list1 = init_list([3, 2, 4, 1, 4])
    list2 = init_list([3, 3, 3, 1, 3, 3])
    list3 = init_list([3, 5, 6, 3, 4, 2, 6, 5, 9, 2])
    #delete_in_middle(list1.next.next.next.next)
    delete_in_middle(list2.next.next)
    delete_in_middle(list3.next.next.next.next)
    pretty_print(list1)
    pretty_print(list2)
    pretty_print(list3)

def test5():
    list1 = init_list([3, 2, 4, 1, 5])
    list2 = init_list([6, 6, 6, 1, 6, 6])
    list3 = init_list([3, 5, 6, 3, 4, 2, 6, 5, 9, 2])
    pretty_print(sum_two_lists(list1, list1))
    pretty_print(sum_two_lists(list1, list2))
    pretty_print(sum_two_lists(list2, list3))

def test6():
    list1 = init_list([3, 2, 4, 1, 5])
    print begin_of_loop(list1)
    list1.next.next.next.next.next = list1.next
    print begin_of_loop(list1)

#test1()
#test2()
#test3()
#test4()
#test5()
test6()