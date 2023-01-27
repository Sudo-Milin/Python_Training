import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):

    def test_first_last_name(self):
        formatted_name = get_formatted_name("martin", "luther")
        self.assertEqual(formatted_name, "Martin Luther")

if __name__ == "__main__":
    unittest.main()
