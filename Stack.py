class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)
        print("PUSH:\n  Pushed value:", value, "\n  Stack:", self.stack, "\n")

    def pop(self):
        if self.stack:
            popped = self.stack.pop()
            print ("POP:\n  Popped value:", popped, "\n  Stack:", self.stack, "\n")
            return popped
        return None

    def peek(self):
        if self.stack:
            peeked = self.stack[-1]
            print("PEEK:\n  Peeked value:", peeked, "\n  Stack:", self.stack, "\n")
            return peeked
        return None

def main():
    s = Stack()

    s.push(1)
    s.push(2)
    s.push(3)
    
    s.peek() == 3
    s.pop() == 3
    s.peek() == 2
    
    s.pop()
    s.pop()
    
    pop = s.pop() is None
    peek = s.peek() is None

    print("s.pop() is None: ", pop)
    print("s.peek() is None: ", peek)

if __name__ == '__main__':
    main()