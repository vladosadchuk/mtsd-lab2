from linked_list import LinkedList


def main():
    # Create a list
    my_list = LinkedList()

    # Append elements
    my_list.append("A")
    my_list.append("B")
    my_list.append("C")
    print("After appending elements:", my_list)

    # Insert element
    my_list.insert("X", 1)
    print("After inserting 'X' at position 1:", my_list)

    # Get length
    print("List length:", my_list.length())

    # Delete element by index
    removed_element = my_list.delete(2)
    print(f"Removed element: {removed_element}, updated list:", my_list)

    # Delete all occurrences of an element
    my_list.append("A")
    my_list.deleteAll("A")
    print("After deleting all 'A':", my_list)

    # Get element by index
    print("Element at position 1:", my_list.get(1))

    # Clone list
    cloned_list = my_list.clone()
    print("Cloned list:", cloned_list)

    # Reverse list
    my_list.reverse()
    print("After reversing:", my_list)

    # Find first occurrence
    print("First occurrence of 'B':", my_list.findFirst("B"))

    # Find last occurrence
    print("Last occurrence of 'B':", my_list.findLast("B"))

    # Clear list
    my_list.clear()
    print("After clearing:", my_list)

    # Extend list with another list
    my_list.append("1")
    my_list.append("2")
    another_list = LinkedList()
    another_list.append("3")
    another_list.append("4")
    my_list.extend(another_list)
    print("After extending with another list:", my_list)


if __name__ == "__main__":
    main()
