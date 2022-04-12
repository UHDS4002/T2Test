from unittest import TestCase, main


class TestCharacters(TestCase):
    def test_api(self):
        import main
        self.assertTrue(hasattr(main, "Characters"))
        self.assertTrue(hasattr(main.Characters, "push"))
        self.assertTrue(hasattr(main.Characters, "pop"))

    def test_abcde(self):
        from main import Characters
        c = Characters()
        for char in ["a", "b", "c", "d", "e"]:
            c.push(char)
        for char in ["e", "c", "a", "b", "d"]:
            self.assertEqual(char, c.pop())

    def test_abcdef(self):
        from main import Characters
        c = Characters()
        for char in ["a", "b", "c", "d", "e", "f"]:
            c.push(char)
        for char in ["e", "c", "a", "b", "d", "f"]:
            self.assertEqual(char, c.pop())


if __name__ == '__main__':
    main()
