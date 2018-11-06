from stack.stack_by_array import Stack


class MinStack:
    """http://alrightchiu.github.io/SecondRound/stack-neng-gou-zai-o1qu-de-zui-xiao-zhi-de-minstack.html"""
    def __init__(self):
        self.data_stack = Stack()
        self.min_stack = Stack()

    def is_empty(self):
        return self.data_stack.is_empty()

    def push(self, element):
        if isinstance(element, int):
            self.data_stack.push(element)
            if self.min_stack.is_empty():
                self.min_stack.push(element)
            else:
                min_element = self.min_stack.peek()
                if element < min_element:
                    self.min_stack.push(element)
                else:
                    self.min_stack.push(min_element)

    def pop(self):
        if self.data_stack.is_empty():
            return None
        else:
            self.min_stack.pop()
            return self.data_stack.pop()

    def peek(self):
        return self.data_stack.peek() if not self.data_stack.is_empty() else None

    def min(self):
        return self.min_stack.peek() if not self.min_stack.is_empty() else None

    def size(self):
        return self.data_stack.size()


if __name__ == '__main__':
    s = MinStack()
    s.push(9)
    s.push(6)
    s.push(1)
    s.push(7)
    s.push(5)
    print('Top element: {}'.format(s.peek()))
    print('Min element: {}'.format(s.min()))
    print('Stack size: {}'.format(s.size()))
    print('Pop element: {}'.format(s.pop()))
    print('Pop element: {}'.format(s.pop()))
    print('Stack size: {}'.format(s.size()))
    print('Pop element: {}'.format(s.pop()))
    print('Min element: {}'.format(s.min()))
    print('Pop element: {}'.format(s.pop()))
    print('Stack size: {}'.format(s.size()))
    print('Pop element: {}'.format(s.pop()))

