# data.py

# MOVIE DATABASE (Title: Genre)
# Step 1: Create a dictionary containing movie titles and their genres 
movies = {
    "Inception": "Sci-Fi",
    "Interstellar": "Sci-Fi",
    "The Dark Knight": "Action",
    "The Lion King": "Animation",
    "Titanic": "Romance",
    "Avengers": "Action",
    "Zootopia": "Animation"
}

# Dictionary to store user ratings
ratings = {movie: [] for movie in movies}
