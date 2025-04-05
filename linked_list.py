class LinkedList:
    def __init__(self):
        self.data = []

    def length(self) -> int:
        return len(self.data)

    def append(self, element: str) -> None:
        self.data.append(element)

    def insert(self, element: str, index: int) -> None:
        if index < 0 or index > len(self.data):
            raise IndexError("Index out of range")
        self.data.insert(index, element)

    def delete(self, index: int) -> str:
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of range")
        return self.data.pop(index)

    def deleteAll(self, element: str) -> None:
        self.data = [x for x in self.data if x != element]

    def get(self, index: int) -> str:
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of range")
        return self.data[index]

    def clone(self):
        cloned_list = LinkedList()
        cloned_list.data = self.data.copy()
        return cloned_list

    def reverse(self) -> None:
        self.data.reverse()

    def findFirst(self, element: str) -> int:
        try:
            return self.data.index(element)
        except ValueError:
            return -1

    def findLast(self, element: str) -> int:
        for i in range(len(self.data) - 1, -1, -1):
            if self.data[i] == element:
                return i
        return -1

    def clear(self) -> None:
        self.data.clear()

    def extend(self, elements):
        self.data.extend(elements.data)

    def __str__(self):
        return "[" + " -> ".join(self.data) + "]"
