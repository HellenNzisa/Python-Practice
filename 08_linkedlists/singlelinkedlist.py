class Node:
    def __init__(self, data):
        self.data = data  # Node's data
        self.next = None  # Pointer to the next node only (singly linked)

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_index(self, index, data):
        if index == 0:
            self.insert_at_start(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(index - 1):
            if not current:
                return  # should return index out of bounds
            current = current.next
        if not current:
            return  # ioub
        new_node.next = current.next
        current.next = new_node

    def delete_at_index(self, index):
        if not self.head:
            return  # empty list
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        for _ in range(index - 1):
            if not current.next:
                return  # ioub
            current = current.next
        if not current.next:
            return  # ioub
        current.next = current.next.next

    def search(self, value):
        current = self.head
        idx = 0
        while current:
            if current.data == value:
                return idx
            current = current.next
            idx += 1
        return -1

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_end(10)
    ll.insert_at_start(2)
    ll.insert_at_index(1, 6)
    ll.display()  # expected output: 2 -> 8 -> 10 -> None
    print(ll.search(7))  # expected output: 1
    ll.delete_at_index(1)
    ll.display()  # expected output: 2 -> 10 -> None
