from app.models.movies import Movies
from app.util.exception import read_data, write_data

def add_movie(movie_data):
    movies = read_data()  
    movie = Movies(**movie_data)
    movies.append(movie)
    write_data([m.to_dict() for m in movies]) 

def get_all_movies():
    movies = read_data()
    return [movie.to_dict() for movie in movies]

def search_movies_by_field(field, value):
    movies = read_data()
    result = []

    for movie in movies:
        attr = getattr(movie, field, None)

        if isinstance(attr, list):
            if value.lower() in [item.lower() for item in attr]:
                result.append(movie)

        elif isinstance(attr, dict):
            if any(value.lower() in [i.lower() for i in v] for v in attr.values()):
                result.append(movie)

        elif str(attr).lower() == str(value).lower():
            result.append(movie)

    return result



def update_movie_by_id(movie_id, updated_data):
    movies = read_data()
    for movie in movies:
        if movie.movie_id == movie_id:  
            for key, value in updated_data.items(): 
                setattr(movie, key, value)
            write_data([m.to_dict() for m in movies])
            return movie.to_dict()
    return None

def delete_movie_by_id(movie_id):
    movies = read_data()
    for movie in movies:
        if movie.movie_id == movie_id: 
            movies.remove(movie)
            write_data([m.to_dict() for m in movies])
            return movie.to_dict()
    return None
