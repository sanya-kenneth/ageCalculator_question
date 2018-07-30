class Age_calc():
    def ageCalculator(self, birth_year):
        self.birth_year = birth_year
        current_year = 2018
        year_type = (int)
        if isinstance(birth_year,year_type):
            return current_year - self.birth_year
        else:
            raise ValueError
