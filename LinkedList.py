class Link:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.first = None

    def insert_first(self, data):
        new_link = Link(data)
        new_link.next = self.first
        self.first = new_link

    def insert_last(self, data):
        new_link = Link(data)
        current = self.first

        if current == None:
            self.first = new_link
            return
        
        while current.next != None:
            current = current.next
        
        current.next = new_link

    # String representation of LinkedList
    def __str__ (self):
        string = "Linked List: ["
        current = self.first

        if current == None:
            return string

        while current.next != None:
            string += str(current.data) + " "
            current = current.next
        string += str(current.data) + "]"
        return string

def main():
    linked_list = LinkedList()
    for i in range(9, 0, -1):
        linked_list.insert_first(i)
    print(linked_list)

    linked_list.insert_first(0)
    linked_list.insert_last(10)
    print(linked_list)

if __name__ == "__main__":
    main()