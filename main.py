#main.py
#This is the central file of the Movie Recommendation System.
#It controls menu navigation, connects all modules, and handles user interaction.
from data import movies
from search import search_movie
from rating import rate_movie
from recommend import recommend_movie


def view_all_movies():
    print("\n--- ALL MOVIES ---")
    for movie, genre in movies.items():
        print(f"{movie} ({genre})")
    print()


def main():
    while True:
        print("=== MOVIE RECOMMENDATION SYSTEM ===")
        print("1. View All Movies")
        print("2. Search Movie")
        print("3. Rate a Movie")
        print("4. Recommend a Movie")
        print("5. Exit")

        # Get user's menu choice 
        choice = input("Enter choice (1-5): ")

        if choice == "1":
            view_all_movies()
        elif choice == "2":
            search_movie()
        elif choice == "3":
            rate_movie()
        elif choice == "4":
            recommend_movie()
        elif choice == "5":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice! Try again.\n")


if __name__ == "__main__":
    main()
