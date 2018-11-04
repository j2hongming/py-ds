class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.trail = None

    def insert_start(self, data):
        """Basic function"""
        insert_node = ListNode(data)
        if self.head is not None:
            insert_node.next = self.head
            self.head.prev = insert_node
            self.head = insert_node
        else:
            # empty
            print('empty list: insert_start')
            self.head = insert_node
            self.trail = insert_node

    # basic
    def traversal_from_start(self):
        """Basic function"""
        view = ''
        cur = self.head
        while cur is not None:
            view = view + '{}<->'.format(cur.data)
            cur = cur.next
        view = view + 'null'
        return view

    # basic
    def traversal_from_end(self):
        view = ''
        cur = self.trail
        while cur is not None:
            view = view + '{}<->'.format(cur.data)
            cur = cur.prev
        view = view + 'null'
        return view

    def remove(self, r_data):
        if self.head is None:
            # empty list case
            print('Empty list')
            return
        cur = self.head
        while cur.data != r_data:
            cur = cur.next
            if cur is None:
                # not found and reach list end
                print('Not found {}'.format(r_data))
                return

        if cur.prev is None:
            # head node case
            self.head = cur.next
            self.head.prev = None
            del cur
        else:
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
            del cur


if __name__ == '__main__':
    dll = DoubleLinkedList()
    dll.insert_start(1)
    dll.insert_start(2)
    dll.insert_start(9)
    dll.insert_start(5)
    print(dll.traversal_from_start())
    print(dll.traversal_from_end())

    dll.remove(2)
    dll.remove(6)
    dll.remove(5)
    print(dll.traversal_from_start())
    print(dll.traversal_from_end())
