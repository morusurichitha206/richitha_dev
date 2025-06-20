class Movies:
    def __init__(self, movie_id, title, genre, rating, year, director, language, duration, cast, platforms, awards):
        self.movie_id = movie_id
        self.title = title
        self.genre = genre
        self.rating = rating
        self.year = year
        self.director = director
        self.language = language
        self.duration = duration
        self.cast = cast
        self.platforms = platforms
        self.awards = awards

    def __str__(self):
        return f"{self.title} ({self.year}) - Rating: {self.rating}, Genre: {', '.join(self.genre)}"

    def __repr__(self):
        return self.__str__()

    def to_dict(self):
        return {
            "movie_id": self.movie_id,
            "title": self.title,
            "genre": self.genre,
            "rating": self.rating,
            "year": self.year,
            "director": self.director,
            "language": self.language,
            "duration": self.duration,
            "cast": self.cast,
            "platforms": self.platforms,
            "awards": self.awards
        }
