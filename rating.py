# rating.py

# This module allows users to rate movies.
# It validates movie names, checks rating ranges, and stores user ratings inside the ratings dictionary.


from data import movies, ratings

def rate_movie():
    #Ask user which movie they want to rate
    movie = input("\nEnter movie name to rate: ").strip()

    if movie not in movies:
        print("Movie not found!")
        return

    try:
        #Ask user for a rating and convert input to float
        rating = float(input("Enter rating (1 to 5): "))
        if not 1 <= rating <= 5:
            print("Invalid rating! Must be between 1 and 5.")
            return

        ratings[movie].append(rating)
        print(f"Thanks! You rated {movie} {rating}")

    except ValueError:
        print("Please enter a valid number!")

    print()
