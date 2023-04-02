from abc import ABC, abstractmethod


class Musician(ABC):
    skills = {
        'Singer': ['sing high pitch notes', 'sing low pitch notes'],
        'Drummer': ['play the drums with drumsticks', 'play the drums with drum brushes', 'read sheet music'],
        'Guitarist': ['play metal', 'play rock', 'play jazz'],
    }

    def __init__(self, name: str, age: int, skills: list):
        self.name = name
        if name == '':
            raise ValueError('Musician name cannot be empty!')
        self.age = age
        if self.age < 16:
            raise ValueError('Musicians should be at least 16 years old!')
        self.skills = []

    @abstractmethod
    def learn_new_skill(self, new_skill):
        if new_skill not in self.skills:
            if new_skill not in Musician.skills[self.__class__.__name__]:
                raise ValueError(f'{new_skill} is not a needed skill!')
            self.skills.append(new_skill)
            return
        raise Exception(f'{new_skill} is already learned!')


