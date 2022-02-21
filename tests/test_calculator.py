import unittest
import random
from calculator import ConversionRate

class TestCalc(unittest.TestCase):
    def test_correct(self): 

        Number1 = random.randint(0,1000000)
        Number2 = random.randint(0,1000000)

        result = ConversionRate(Number1, Number2)

        self.assertEqual(result, 10)