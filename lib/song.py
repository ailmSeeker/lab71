class Song:
    count = 0
    genres = ''
    genre_count = []
    artists = ''

    def __init__(self, name, artist, genres):
        self.name = name
        self.artist = artist

        self.genre = genres
        type(self).count += 1
        type(self).genres += self.genre
        type(self).artists+= self.artist

        self.add_song_to_count()


    def add_song_to_count(self):
        self.count = self.count + 1
        return self.count

    def genre_count(self):

    pass
