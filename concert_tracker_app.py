from band import Band
from band_members.drummer import Drummer
from band_members.guitarist import Guitarist
from band_members.singer import Singer
from concert import Concert


class ConcertTrackerApp:
    MUSICIAN_TYPES = ['Singer', 'Guitarist', 'Drummer']
    REQUIRED_SKILLS = {
        'Rock': {
            'Drummer': 'play the drums with drumsticks',
            'Singer': 'sing high pitch notes',
            'Guitarist': 'play rock'
        },
        'Metal': {
            'Drummer': 'play the drums with drumsticks',
            'Singer': 'sing low pitch notes',
            'Guitarist': 'play metal'
        },
        'Jazz': {
            'Drummer': 'play the drums with drum brushes',
            'Singer': ['sing high pitch notes', 'sing low pitch notes'],
            'Guitarist': ['play jazz']
        }
    }
    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def get_band_by_name(self, band_name):
        if self.bands:
            for band in self.bands:
                if band.name == band_name:
                    return band
        raise Exception(f'{band_name} isn\'t a band!')

    def get_musician_by_name(self, musician_name):
        for musician in self.musicians:
            if musician.name == musician_name:
                return musician

    def create_musician(self, musician_type, name, age):
        if musician_type not in self.MUSICIAN_TYPES:
            raise ValueError('Invalid musician type!')
        if self.get_musician_by_name(name):
            raise Exception(f'{name} is already a musician!')
        if musician_type == 'Singer':
            self.musicians.append(Singer(name,age))
        elif musician_type == 'Guitarist':
            self.musicians.append(Guitarist(name, age))
        elif musician_type == 'Drummer':
            self.musicians.append(Drummer(name, age))
        return f'{name} is now a {musician_type}.'

    def create_band(self, name):
        for band in self.bands:
            if name == band.name:
                raise Exception(f'{name} band is already created!')
        self.bands.append(Band(name))
        return f'{name} was created.'

    def create_concert(self, genre, audience, ticket_price, expenses, place):
        for concert in self.concerts:
            if place == concert.place:
                raise Exception(f'{place} is already registered for {genre} concert!')
        self.concerts.append(Concert(genre, audience, ticket_price, expenses, place))
        return f'{genre} concert in {place} was added.'

    def add_musician_to_band(self, musician_name, band_name):
        musician = self.get_musician_by_name(musician_name)
        if musician:
            band = self.get_band_by_name(band_name)
            if band:
                band.members.append(musician)
                return f'{musician_name} was added to {band_name}.'
            raise Exception(f'{band_name} isn\'t a band!')
        raise Exception(f'{musician_name} isn\'t a musician!')

    def remove_musician_from_band(self, musician_name, band_name):
        band = self.get_band_by_name(band_name)
        musician = self.get_musician_by_name(musician_name)
        if musician in band.members:
            band.members.remove(musician)
            return f'{musician_name} was removed from {band_name}.'
        raise Exception(f'{musician_name} isn\'t a member of {band_name}!')


    def check_skills(self, genre, band):
        for musician in band.members:
            musician_type = musician.__class__.__name__
            for skill in musician.skills:
                if skill not in self.REQUIRED_SKILLS[genre][musician_type]:
                    raise Exception(f'The {band.name} band is not ready to play at the concert!')

    def start_concert(self, concert_place, band_name):
        band = self.get_band_by_name(band_name)
        for type in self.MUSICIAN_TYPES:
            if type not in band.get_member_types():
                raise Exception(f'{band_name} can\'t start the concert because it doesn\'t have enough members!')
        for concert in self.concerts:
            if concert_place == concert.place:
                self.check_skills(concert.genre, band)
                profit = concert.audience * concert.ticket_price - concert.expenses
                return f'{band.name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}.'


musician_types = ['Singer', 'Drummer', 'Guitarist']
names = ['George', 'Alex', 'Lilly']

app = ConcertTrackerApp()

for i in range(3):
    print(app.create_musician(musician_types[i], names[i], 20))

print(app.musicians[0].learn_new_skill('sing high pitch notes'))
print(app.musicians[1].learn_new_skill('play the drums with drumsticks'))
print(app.musicians[2].learn_new_skill('play rock'))

print(app.create_band('RockName'))
for i in range(3):
    print(app.add_musician_to_band(names[i], 'RockName'))

print(app.create_concert('Rock', 20,5.20,56.7, 'Sofia'))

print(list(map(lambda a: a.__class__.__name__, app.bands[0].members)))
print(app.start_concert("Sofia", 'RockName'))