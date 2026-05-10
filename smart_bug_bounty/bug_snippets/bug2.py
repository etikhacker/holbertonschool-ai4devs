"""
bug2.py
Intended behavior: A Stack class with push, pop, peek, and is_empty methods.
pop() and peek() should raise IndexError on an empty stack.
"""

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0   # BUG: should be `len(self.items) == 0`
                                      # is fine, but size() below is broken

    def size(self):
        return len(self.items - 1)    # BUG: items is a list, not an int;
                                      # should be len(self.items)

    def clear(self):
        self.items == []              # BUG: comparison instead of assignment


if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    print(s.peek())   # expected: 30
    print(s.pop())    # expected: 30
    print(s.size())   # expected: 2
    s.clear()
    print(s.is_empty())  # expected: True
