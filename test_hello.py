import unittest
from hello import greet

class TestGreet(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet(), "Hello from GitPractice!")

if __name__ == "__main__":
    unittest.main()