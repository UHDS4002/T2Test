from unittest import TestCase, main


class TestHospital(TestCase):
    def test_api(self):
        import hospital
        self.assertTrue(hasattr(hospital, 'Hospital'))
        self.assertTrue(hasattr(hospital.Hospital, 'push'))
        self.assertTrue(hasattr(hospital.Hospital, 'pop'))

    def test_case1(self):
        from hospital import Hospital
        hos = Hospital()
        hos.push("Ali", 2)
        hos.push("Hosein", 1)
        hos.push("Reza", 2)
        self.assertEqual(hos.pop(), "Hosein")
        self.assertEqual(hos.pop(), "Ali")
        self.assertEqual(hos.pop(), "Reza")

    def test_case2(self):
        from hospital import Hospital
        hos = Hospital()
        for element, priority in [("Ali", 2),
                                  ("Mammad", 1),
                                  ("Reza", 1),
                                  ("Hosein", 1),
                                  ("Jalal", 1)]:
            hos.push(element, priority)

        for element in ["Mammad", "Reza", "Hosein", "Ali", "Jalal"]:
            self.assertEqual(hos.pop(), element)


if __name__ == "__main__":
    main()
