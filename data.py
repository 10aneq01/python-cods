class Stack:
    def __init__(self, capacity):
        self.stack = []
        self.capacity = capacity

    def push(self, value):
        if len(self.stack) >= self.capacity:
            print("Stack Overflow! Cannot push", value)
        else:
            self.stack.append(value)
            print(value, "pushed into stack.")

    def pop(self):
        if not self.stack:
            print("Stack Underflow! Stack is empty.")
            return None
        else:
            return self.stack.pop()

    def peek(self):
        if not self.stack:
            print("Stack is empty.")
            return None
        else:
            return self.stack[-1]

    def display(self):
        if not self.stack:
            print("Stack is empty.")
        else:
            print("Stack elements:", self.stack)
