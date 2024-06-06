import unittest

class TestStringMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print(">>>>>>setUpClass")
        return super().setUpClass()
    
    @classmethod
    def tearDownClass(cls) -> None:
        print(">>>>>>tearDownClass")
        return super().tearDownClass()

    def setUp(self) -> None:
        print(">>>>>>setUp")
        return super().setUp()
    
    def tearDown(self) -> None:
        print(">>>>>>tearDown")
        return super().tearDown()

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()