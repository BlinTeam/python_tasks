from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


def is_balanced(str):
    s = Stack()
    opens = ['(', '[', '{']
    closes = [')', ']', '}']
    brackets = dict(zip(opens, closes))

    for e in str:
        if e in opens:
            s.push(e)
        elif e in closes:
            if s.is_empty():
                return False
            elem = s.pop()
            if brackets[elem] != e:
                return False
    return s.is_empty()
