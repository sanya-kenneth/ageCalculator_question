import unittest
from app.age_calc import Age_calc
class Calc_tester(unittest.TestCase):
    def test_correct_age_is_calculated(self):
           birth_year = 1990
           calculate = Age_calc()
           assert calculate.ageCalculator(birth_year) == 28