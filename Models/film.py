class Film():

    def __init__(self, id, title, category, duration):
        self.id = id
        self.title = title
        self.category = category
        self.duration = duration

    def json(self):
        return {
            'id': self.id,
            'title': self.title,
            'category': self.category,
            'duration': self.duration
        }

    @staticmethod
    def get_by_id(id):
        return Film(1, 'El resplandor', 'Terror', 140)

    @staticmethod
    def get_all():
        return [
            Film(1, 'El resplandor', 'Terror', 140),
            Film(2, 'IT', 'Terror', 90)
        ]

    @staticmethod
    def create():
        product = Film(2)
        return product.save()

    @staticmethod
    def update(self, title, category, length):
        self.title = title
        self.category = category
        self.duration = length

    @staticmethod
    def delete(self):
        return self

    def save(self):
        return self
