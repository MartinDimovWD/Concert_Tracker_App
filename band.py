
class Band:
    def __init__(self,name):
        self.name = name
        if name == '':
            raise ValueError('Band name should contain at least one character!')
        self.members = []

    def __str__(self):
        return f'{self.name} with {len(self.members)} members.'

    def get_member_types(self):
        musician_types = []
        for member in self.members:
            musician_types.append(member.__class__.__name__)
        return musician_types
