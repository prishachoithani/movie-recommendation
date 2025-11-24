# search.py

from data import movies

def search_movie():
    name = input("\nEnter movie name to search: ").strip().lower()
    found = False

    print()
    for movie in movies:
        if name in movie.lower():
            print(f"Found: {movie} ({movies[movie]})")
            found = True

    if not found:
        print("No movie found.")

    print()
