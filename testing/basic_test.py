import unittest

class TestStringMethods(unittest.TestCase):

    a = 1

    @classmethod
    def setUpClass(cls) -> None:
        print(">>>>>>setUpClass", cls.a)
        return super().setUpClass()
    
    @classmethod
    def tearDownClass(cls) -> None:
        print(">>>>>>tearDownClass", cls.a)
        return super().tearDownClass()

    def setUp(self) -> None:
        self.a = 2
        return super().setUp()
    
    def tearDown(self) -> None:
        self.a = 3
        return super().tearDown()

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        self.assertEqual(self.a, 2)

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    @unittest.skip("not implemented")
    def test_super_new_impl(self):
        pass

    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")

if __name__ == '__main__':
    unittest.main()