# Test Code for Test 2 Of Data Structures 4002
# Tests my_queue.py
# Author: Esmail
from unittest import TestCase, main


class StackTest(TestCase):
    def test_init(self):
        from my_queue import Queue
        Queue()

    def test_api(self):
        from my_queue import Queue
        queue = Queue()
        self.assertTrue(hasattr(queue, "enqueue"))
        self.assertTrue(hasattr(queue, "dequeue"))
        self.assertTrue(hasattr(queue, "is_empty"))

    def test_stack(self):
        from my_queue import Queue
        queue = Queue()
        self.assertTrue(queue.is_empty())
        queue.enqueue("hello")
        self.assertFalse(queue.is_empty())
        self.assertEqual(queue.dequeue(), "hello")
        self.assertTrue(queue.is_empty())
        queue.enqueue("hello")
        queue.enqueue("hi")
        self.assertFalse(queue.is_empty())
        self.assertEqual(queue.dequeue(), "hello")
        self.assertEqual(queue.dequeue(), "hi")
        self.assertRaises(AssertionError, queue.dequeue)


if __name__ == '__main__':
    main()
