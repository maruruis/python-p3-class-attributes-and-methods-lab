class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.add_song_to_count()
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_to_genre(genre)
        self.add_to_artists(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
    
    @classmethod
    def add_to_genre(cls, new_genre):
        if new_genre not in cls.genres:
            cls.genres.append(new_genre)
        cls.add_to_genre_count(new_genre)
    
    @classmethod
    def add_to_artists(cls, new_artist):
        if new_artist not in cls.artists:
            cls.artists.append(new_artist)
        cls.add_to_artist_count(new_artist)

    @classmethod
    def add_to_genre_count(cls, new_genre):
        cls.genre_count[new_genre] = cls.genre_count.get(new_genre, 0) + 1

    @classmethod
    def add_to_artist_count(cls, new_artist):
        cls.artist_count[new_artist] = cls.artist_count.get(new_artist, 0) + 1