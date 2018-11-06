class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, element):
        insert_element = ListNode(element)
        insert_element.next = self.top
        self.top = insert_element

    def pop(self):
        if self.is_empty():
            return None
        else:
            cur = self.top
            self.top = cur.next
            data = cur.data
            del cur
            return data

    def peek(self):
        return self.top.data

    def size(self):
        count = 0
        cur = self.top
        while cur is not None:
            count = count + 1
            cur = cur.next
        return count


if __name__ == '__main__':
    s = Stack()
    s.push(9)
    s.push(6)
    s.push(1)
    print('Top element: {}'.format(s.peek()))
    print('Stack size: {}'.format(s.size()))
    print('Pop element: {}'.format(s.pop()))
    print('Pop element: {}'.format(s.pop()))
    print('Stack size: {}'.format(s.size()))
    print('Pop element: {}'.format(s.pop()))
    print('Pop element: {}'.format(s.pop()))