__author__ = "Eugene Alekseev"


class Node:
    def __init__(self, payload, next=None):
        self.payload = payload
        self.next = next

    @property
    def next(self):
        return self.next

    @property
    def payload(self):
        return self.payload

    def set_next(self, next):
        self.next = next

    def set_payload(self, payload):
        self.payload = payload

    def __str__(self):
        return str(self.payload)


class LinkedList:
    def __init__(self):
        self.head = None
        self.current_node = self.head

    def insert_in_front(self, node):
        self.head = node
        self.current_node = self.head

    def __iter__(self):
        while self.current_node != None:
            yield self.current_node
            self.current_node = self.current_node.next
        self.current_node = self.head

    def insert(self, after, node_to_insert):
        node_to_insert.next = after.next
        after.next = node_to_insert

    def delete(self, node):
        if node == self.head:
            self.head = self.head.next
        else:
            current = self.head
            while current.next != node:
                current = current.next
                continue
            current.next = node.next
            node = None



def main():
    forth = Node(0)
    third = Node(1, forth)
    second = Node(2, third)
    first = Node(4, second)
    lst = LinkedList()
    lst.insert_in_front(first)
    new_node = Node(6)
    lst.insert(second, new_node)
    lst.delete(third)
    for node in iter(lst):
        print(node)


if __name__ == "__main__":
    main()