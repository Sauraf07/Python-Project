class Student:
    def __init__(self, name, math, science, english):
        self.name = name
        self.math = math
        self.science = science
        self.english = english
    
    def to_dict(self):
        return {
            'name': self.name,
            'math': self.math,
            'science': self.science,
            'english': self.english
        }