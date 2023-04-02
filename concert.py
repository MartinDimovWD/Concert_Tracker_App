
class Concert:
    GENRES = ['Metal', 'Rock', 'Jazz']

    def __init__(self, genre, audience, ticket_price, expenses, place):
        self.genre = genre
        if genre not in self.GENRES:
            raise ValueError(f"Our group doesn't play {genre}!")
        self.audience = audience
        if audience <1:
            raise ValueError('At least one person should attend the concert!')
        self.ticket_price = ticket_price
        if ticket_price < 1:
            raise ValueError('Ticket price must be at least 1.00$!')
        self.expenses = expenses
        if expenses < 0:
            raise ValueError('Expenses cannot be a negative number!')
        self.place = place
        if len(place) < 2 or place.isspace():
            raise ValueError('Place must contain at least 2 chars. It cannot be empty!')

    def __str__(self):
        return f'{self.genre} concert at {self.place}'



