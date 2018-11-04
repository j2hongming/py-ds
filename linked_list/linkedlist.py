class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # basic
    def insert_start(self, data):
        """Basic function"""
        insert_node = ListNode(data)
        if self.head is not None:
            insert_node.next = self.head
            self.head = insert_node
        else:
            # empty
            print('empty list: insert_start')
            self.head = insert_node

    # basic
    def traversal(self):
        """Basic function"""
        view = ''
        cur = self.head
        while cur is not None:
            view = view + '{}->'.format(cur.data)
            cur = cur.next
        view = view + 'null'
        return view

    def insert_end(self, data):
        insert_node = ListNode(data)
        if self.head is None:
            print('empty list: insert_end')
            self.head = insert_node
            return

        cur = self.head
        while cur.next is not None:
            cur = cur.next
        
        cur.next = insert_node

    def remove_with_dummy(self, r_data):
        if self.head is None:
            # empty list case
            return
        self.insert_start('dummy')
        cur = self.head
        prev = None
        while cur.data != r_data:
            prev = cur
            cur = cur.next
            if cur is None:
                # not found and reach list end
                self.head = self.head.next
                return
        prev.next = cur.next
        del cur
        self.head = self.head.next

    def remove(self, r_data):
        if self.head is None:
            # empty list case
            return
        cur = self.head
        prev = None
        while cur.data != r_data:
            prev = cur
            cur = cur.next
            if cur is None:
                # not found and reach list end
                return
        if prev is None:
            # head node case
            self.head = cur.next
            del cur
        else:
            prev.next = cur.next
            del cur

    def clear(self):
        while self.head is not None:
            del_cand = self.head
            self.head = del_cand.next
            del del_cand

    # interview
    def reverse(self):
        """interview"""
        if self.head is None or self.head.next is None:
            # empty list case
            return
        previous = None
        cur = self.head
        preceding = cur.next
        while preceding is not None:
            cur.next = previous
            previous = cur
            cur = preceding
            preceding = preceding.next
        cur.next = previous
        self.head = cur

    # interview
    def check_cycle(self):
        """interview"""
        if self.head is None or self.head.next is None:
            # empty list case
            return
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def break_cycle(self):
        pass


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_end(2)
    ll.insert_start(9)
    ll.insert_start(5)
    ll.insert_end(1)
    print(ll.traversal())

    ll.remove_with_dummy(5)
    ll.remove_with_dummy(2)
    ll.remove_with_dummy(8)
    print(ll.traversal())

    ll.insert_start(6)
    ll.insert_end(7)
    ll.insert_end(8)
    print(ll.traversal())

    ll.remove(2)
    ll.remove(6)
    ll.remove(8)
    print(ll.traversal())
    ll.remove(1)
    ll.remove(9)
    ll.remove(7)
    print(ll.traversal())

    ll.insert_end(2)
    ll.insert_start(9)
    ll.insert_start(5)
    ll.insert_end(1)
    print(ll.traversal())
    ll.clear()
    print(ll.traversal())

    ll.insert_end(2)
    ll.insert_start(9)
    ll.insert_start(5)
    ll.insert_end(1)
    print(ll.traversal())
    ll.reverse()
    print(ll.traversal())
    ll.clear()
    ll.insert_start(5)
    print(ll.traversal())
    ll.reverse()
    print(ll.traversal())

    # linkedlist with loop
    ll_lcycle = LinkedList()
    a = ListNode(5)
    b = ListNode(7)
    c = ListNode(11)
    d = ListNode(15)
    e = ListNode(18)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = c
    ll_lcycle.head = a
    print('single linked list has cycle: {}'.format(ll_lcycle.check_cycle()))

    ll_without_cycle = LinkedList()
    ll_without_cycle.insert_end(2)
    ll_without_cycle.insert_start(9)
    ll_without_cycle.insert_start(5)
    ll_without_cycle.insert_end(1)
    print(ll_without_cycle.traversal())
    print('single linked list has cycle: {}'.format(ll_without_cycle.check_cycle()))
