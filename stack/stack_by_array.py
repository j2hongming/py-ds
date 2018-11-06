class Stack:

    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.is_empty():
            return None
        else:
            element = self.stack[-1]
            del self.stack[-1]
            return element

    def peek(self):
        return self.stack[-1] if not self.is_empty() else None

    def size(self):
        return len(self.stack)


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
