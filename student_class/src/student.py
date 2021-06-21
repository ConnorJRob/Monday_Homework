class Student:
    def __init__(self, Name, Cohort):
        self.name = Name
        self.cohort = Cohort

    def talk(self):
        return "I can talk!"

    def say_favourite_language(self, language):
        return f"I love {language}"
