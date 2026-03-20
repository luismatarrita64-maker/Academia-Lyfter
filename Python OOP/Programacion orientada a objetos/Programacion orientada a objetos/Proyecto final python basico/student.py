class Student:
    def __init__(self, full_name, section, spanish, english, social_studies, science):
        self.full_name = full_name
        self.section = section
        self.spanish = spanish
        self.english = english
        self.social_studies = social_studies
        self.science = science

    def average(self):
        return (self.spanish + self.english + self.social_studies + self.science) / 4

    def to_dict(self):
        return {
            'full name': self.full_name,
            'section': self.section,
            'spanish note': self.spanish,
            'english note': self.english,
            'social_studies note': self.social_studies,
            'science note': self.science
        }

    @staticmethod
    def from_dict(data):
        return Student(
            data['full name'],
            data['section'],
            int(data['spanish note']),
            int(data['english note']),
            int(data['social_studies note']),
            int(data['science note'])
        )

    def __str__(self):
        return (f"{self.full_name} | Section {self.section} | "
                f"Notas: SP {self.spanish}, ENG {self.english}, "
                f"SS {self.social_studies}, SCI {self.science}")