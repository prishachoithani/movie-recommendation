# data.py

# MOVIE DATABASE (Title: Genre)
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
