class Node:
    def __init__(self, data: str):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def length(self) -> int:
        return self.size

    def append(self, element: str) -> None:
        new_node = Node(element)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def insert(self, element: str, index: int) -> None:
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        new_node = Node(element)
        if index == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            if self.size == 0:
                self.tail = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            new_node.prev = current
            if current.next:
                current.next.prev = new_node
            current.next = new_node
            if new_node.next is None:
                self.tail = new_node
        self.size += 1

    def delete(self, index: int) -> str:
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        if index == 0:
            data = self.head.data
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            data = current.data
            if current.prev:
                current.prev.next = current.next
            if current.next:
                current.next.prev = current.prev
            if current == self.tail:
                self.tail = current.prev
        self.size -= 1
        return data

    def deleteAll(self, element: str) -> None:
        current = self.head
        while current:
            if current.data == element:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                self.size -= 1
            current = current.next

    def get(self, index: int) -> str:
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def clone(self):
        cloned_list = LinkedList()
        current = self.head
        while current:
            cloned_list.append(current.data)
            current = current.next
        return cloned_list

    def reverse(self) -> None:
        current = self.head
        while current:
            current.next, current.prev = current.prev, current.next
            current = current.prev
        self.head, self.tail = self.tail, self.head

    def findFirst(self, element: str) -> int:
        current = self.head
        index = 0
        while current:
            if current.data == element:
                return index
            current = current.next
            index += 1
        return -1

    def findLast(self, element: str) -> int:
        current = self.tail
        index = self.size - 1
        while current:
            if current.data == element:
                return index
            current = current.prev
            index -= 1
        return -1

    def clear(self) -> None:
        self.head = self.tail = None
        self.size = 0

    def extend(self, elements):
        current = elements.head
        while current:
            self.append(current.data)
            current = current.next

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return "[" + " <-> ".join(result) + "]"
