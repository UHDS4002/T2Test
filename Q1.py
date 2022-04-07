# Test Code for Test 2 Of Data Structures 4002
# Tests my_stack.py
# Author: Esmail
from unittest import TestCase, main


class StackTest(TestCase):
    def test_init(self):
        from my_stack import Stack
        Stack()

    def test_api(self):
        from my_stack import Stack
        stack = Stack()
        self.assertTrue(hasattr(stack, "push"))
        self.assertTrue(hasattr(stack, "pop"))
        self.assertTrue(hasattr(stack, "is_empty"))

    def test_stack(self):
        from my_stack import Stack
        stack = Stack()
        self.assertTrue(stack.is_empty())
        stack.push("hello")
        self.assertFalse(stack.is_empty())
        self.assertEqual(stack.pop(), "hello")
        self.assertTrue(stack.is_empty())
        stack.push("hello")
        stack.push("hi")
        self.assertFalse(stack.is_empty())
        self.assertEqual(stack.pop(), "hi")
        self.assertEqual(stack.pop(), "hello")
        self.assertRaises(AssertionError, stack.pop)
        for i in range(50):
            stack.push(i)
        self.assertRaises(AssertionError, stack.push, "Something")


if __name__ == '__main__':
    main()
