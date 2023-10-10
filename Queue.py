class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, value):
        self.queue.append(value)
        print("ENQUEUE:\n  Enqueued value:", value, "\n  Queue:", self.queue, "\n")

    def dequeue(self):
        if self.queue:
            dequeued = self.queue.pop(0)
            print("DEQUEUE:\n  Dequeued value:", dequeued, "\n  Queue:", self.queue, "\n")
            return dequeued
        return None

def main():
    q = Queue()

    q.enqueue(7)
    q.enqueue(8)
    q.enqueue(9)

    q.dequeue()
    q.dequeue()

if __name__ == '__main__':
    main()