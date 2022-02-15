import unittest
import some_code

class TestSomeCode(unittest.TestCase):
    
    def test_square_positive_number(self):
        square = some_code.get_square(2)
        
        self.assertEqual(square, 4)
    
if __name__ == '__main__':
    unittest.main()