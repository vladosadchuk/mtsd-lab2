import unittest
from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.cal = LinkedList()

    def test_append(self):
        self.assertEqual(self.cal.length(), 0)
        self.cal.append('A')
        self.assertEqual(self.cal.length(), 1)
        self.cal.append('B')
        self.assertEqual(self.cal.length(), 2)

    def test_length(self):
        self.assertEqual(self.cal.length(), 0)
        self.cal.append('A')
        self.assertEqual(self.cal.length(), 1)

    def test_insert(self):
        self.cal.append('A')
        self.cal.insert('B', 0)
        self.assertEqual(self.cal.get(0), 'B')
        self.assertEqual(self.cal.get(1), 'A')
        with self.assertRaises(IndexError):
            self.cal.insert('C', 10)

    def test_delete(self):
        self.cal.append('A')
        self.cal.append('B')
        self.assertEqual(self.cal.delete(0), 'A')
        self.assertEqual(self.cal.length(), 1)
        with self.assertRaises(IndexError):
            self.cal.delete(10)

    def test_deleteAll(self):
        self.cal.append('A')
        self.cal.append('B')
        self.cal.append('A')
        self.cal.deleteAll('A')
        self.assertEqual(self.cal.length(), 1)
        self.assertEqual(self.cal.get(0), 'B')

    def test_get(self):
        self.cal.append('A')
        self.assertEqual(self.cal.get(0), 'A')
        with self.assertRaises(IndexError):
            self.cal.get(1)

    def test_clone(self):
        self.cal.append('A')
        clone = self.cal.clone()
        self.assertEqual(clone.length(), 1)
        self.assertEqual(clone.get(0), 'A')
        clone.append('B')
        self.assertNotEqual(self.cal.length(), clone.length())

    def test_reverse(self):
        self.cal.append('A')
        self.cal.append('B')
        self.cal.reverse()
        self.assertEqual(self.cal.get(0), 'B')
        self.assertEqual(self.cal.get(1), 'A')

    def test_findFirst(self):
        self.cal.append('A')
        self.cal.append('B')
        self.cal.append('A')
        self.assertEqual(self.cal.findFirst('A'), 0)
        self.assertEqual(self.cal.findFirst('C'), -1)

    def test_findLast(self):
        self.cal.append('A')
        self.cal.append('B')
        self.cal.append('A')
        self.assertEqual(self.cal.findLast('A'), 2)
        self.assertEqual(self.cal.findLast('C'), -1)

    def test_clear(self):
        self.cal.append('A')
        self.cal.clear()
        self.assertEqual(self.cal.length(), 0)

    def test_extend(self):
        self.cal.append('A')
        new_list = LinkedList()
        new_list.append('B')
        new_list.append('C')
        self.cal.extend(new_list)
        self.assertEqual(self.cal.length(), 3)
        self.assertEqual(self.cal.get(1), 'B')
        self.assertEqual(self.cal.get(2), 'C')


if __name__ == '__main__':
    unittest.main()
