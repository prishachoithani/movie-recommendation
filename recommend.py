# recommend.py
#This module recommends a movie to the user based on their favourite movie's genre.
#It uses average ratings as a simple AI/ML logic to select the best recommended film.

from data import movies, ratings

def recommend_movie():
    print("\n--- MOVIE RECOMMENDATION ---")
    #Ask user for a movie they like
    fav = input("Enter a movie you like: ").strip()

    if fav not in movies:
        print("Movie not found! Try rating or viewing the list first.")
        return

    fav_genre = movies[fav]

    best_movie = None
    best_rating = -1

    for movie, genre in movies.items():
        if movie == fav:
            continue

        if genre == fav_genre:
            if ratings[movie]:
                avg_rating = sum(ratings[movie]) / len(ratings[movie])
            else:
                avg_rating = 3  # default neutral rating

            if avg_rating > best_rating:
                best_rating = avg_rating
                best_movie = movie

    if best_movie:
        print(f"We recommend you to watch: {best_movie}")
    else:
        print("No similar movie found yet. Try rating more movies!")

    print()
