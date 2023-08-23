class Song:
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    count = 0

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.genres.append(genre)
        Song.artists.append(artist)
        Song.count += 1

    @classmethod
    def add_to_genres(cls):
        cls.genres = list(set(cls.genres))

    @classmethod
    def add_to_artists(cls):
        cls.artists = list(set(cls.artists))

    @classmethod
    def add_to_genre_count(cls):
        cls.genre_count = {}
        for genre in cls.genres:
            cls.genre_count[genre] = cls.genres.count(genre)

    @classmethod
    def add_to_artist_count(cls):
        cls.artist_count = {}
        for artist in cls.artists:
            cls.artist_count[artist] = cls.artists.count(artist)

# Instantiating objects
ninety_nine_problems = Song("99 Problems", "Jay Z", "Rap")
another_song = Song("SOS Song", "Avicii", "Pop")
yet_another_song = Song("Lean on Me", "Major Lazer", "Pop")

# Calling methods to update class attributes
Song.add_to_genres()
Song.add_to_artists()
Song.add_to_genre_count()
Song.add_to_artist_count()

# Accessing attributes and histogram data
print(ninety_nine_problems.name)
print(ninety_nine_problems.artist)
print(ninety_nine_problems.genre)
print(Song.count)
print(Song.genres)
print(Song.artists)
print(Song.genre_count)
print(Song.artist_count)
