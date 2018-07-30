import unittest
from app.age_calc import Age_calc
class Calc_tester(unittest.TestCase):
    def setUP(self):
        self.calculate = Age_calc()

    def test_correct_age_is_calculated(self):
           birth_year = 1990
           self.calculate = Age_calc()
           calculated = self.calculate.ageCalculator(birth_year) 
           self.assertEqual(28, calculated) 
    
    def test_year_is_input_as_integer(self):
            self.calculate = Age_calc()
            self.assertRaises(ValueError,self.calculate.ageCalculator,'nineteen ninety')
        