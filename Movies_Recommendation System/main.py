from app.services.service import (
    add_movie,
    get_all_movies,
    search_movies_by_field,
    update_movie_by_id,
    delete_movie_by_id
)

def main():
    while True:
        print("\n--- Movie Manager ---")
        print("1  : Add movies to the data file")
        print("2  : Get movies from the data file")
        print("3  : Search movie by title")
        print("4  : Search movie by director")
        print("5  : Search movie by genre")
        print("6  : Search movie by language")
        print("7  : Search movie by cast")
        print("8  : Search movie by platform")
        print("9  : Search movie by award")
        print("10 : Search movie by release year")
        print("11 : Search movie by rating greater than")
        print("12 : Search movie by rating less than")
        print("13 : Search movie by duration less than")
        print("14 : Search movie by duration greater than")
        print("15 : Show top N highest rated movies")
        print("16 : Show N most recently released movies")
        print("17 : Show total number of movies")
        print("18 : Show average rating of all movies")
        print("19 : List unique genres")
        print("20 : List unique directors")
        print("21 : Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            movie_data = {
                "movie_id": int(input("ID: ")),
                "title": input("Title: "),
                "director": input("Director: "),
                "genre": input("Genres (comma-separated): ").split(","),
                "language": input("Languages (comma-separated): ").split(","),
                "cast": {
                    "actors": input("Actors (comma-separated): ").split(","),
                    "actress": input("Actresses (comma-separated): ").split(",")
                },
                "platforms": input("Platforms (comma-separated): ").split(","),
                "awards": input("Awards (comma-separated): ").split(","),
                "year": int(input("Release Year: ")),
                "rating": float(input("Rating: ")),
                "duration": input("Duration (e.g., 2.5 H): ")
            }
            add_movie(movie_data)
            print("Movie added.")

        elif choice == "2":
            for movie in get_all_movies():
                print(movie)

        elif choice == "3":
            title = input("Enter title: ")
            for movie in search_movies_by_field("title", title):
                print(movie)

        elif choice == "4":
            director = input("Enter director: ")
            for movie in search_movies_by_field("director", director):
                print(movie)

        elif choice == "5":
            genre = input("Enter genre: ")
            for movie in search_movies_by_field("genre", genre):
             print(movie)

        elif choice == "6":
            lang = input("Enter language: ")
            for movie in search_movies_by_field("language", lang):
                print(movie)

        elif choice == "7":
            cast = input("Enter actor or actress: ")
            for movie in search_movies_by_field("cast", cast):
                print(movie)

        elif choice == "8":
            platform = input("Enter platform: ")
            for movie in search_movies_by_field("platforms", platform):
                print(movie)

        elif choice == "9":
            award = input("Enter award: ")
            for movie in search_movies_by_field("awards", award):
                print(movie)

        elif choice == "10":
            year = int(input("Enter release year: "))
            for movie in search_movies_by_field("year", year):
                print(movie)

        elif choice == "11":
            rating = float(input("Enter minimum rating: "))
            movies = get_all_movies()
            for movie in movies:
                if movie["rating"] > rating:
                    print(movie)

        elif choice == "12":
            rating = float(input("Enter maximum rating: "))
            movies = get_all_movies()
            for movie in movies:
                if movie["rating"] < rating:
                    print(movie)
                break       
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
