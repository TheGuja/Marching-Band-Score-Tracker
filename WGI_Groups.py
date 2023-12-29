class WGI:
    def __init__(self, school = None, division = None, score = None, date = None):
        self.school = school
        self.division = division
        self.score = score
        self.date = date

    def get_school(self):
        return self.school

    def set_school(self, school):
        self.school = school

    def get_division(self):
        return self.division

    def set_division(self, division):
        self.division = division

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date

    def __str__(self):
        return f"School: {self.school}\nClass: {self.division}\nScore: {str(self.score)}\nDate: {self.date}"