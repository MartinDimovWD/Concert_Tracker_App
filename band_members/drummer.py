from band_members.musician import Musician


class Drummer(Musician):
    def __init__(self, name, age):
        super().__init__(name, age, skills=[])

    def learn_new_skill(self, new_skill):
        super().learn_new_skill(new_skill)
        return f'{self.name} learned to {new_skill}.'