# search.py
# This module handles searching movies by name. 
# It compares user input with titles present in the movie database.
from data import movies

def search_movie():
   # Step 2: Ask the user for a movie name (or partial name)
    name = input("\nEnter movie name to search: ").strip().lower()
    found = False # Boolean flag to track 

    print()
    for movie in movies:
        if name in movie.lower():
            print(f"Found: {movie} ({movies[movie]})")
            found = True

    if not found:
        print("No movie found.")

    print()
