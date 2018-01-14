# This programe will take movie details as input and
# creates a list of movies and calls media.py to play
# the trailer or read movie details.Import the files
# fresh_tomatoes and media files.

import fresh_tomatoes
import media

# Shawshank is an object created for class Movie in
# media, that passes movie details as parameters.
# Movie Title, Storyline, Poster, Trailer URL.
shawshank = media.Movie(
    "The Shawshank Redemption",
    "Andy Dufresne, a successful banker, is arrested for the murders of his"
    "wifeand her lover.",
    "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=NmzuHjWmXOc")

# titanic is an object created for class Movie in
# media, that passes movie details as parameters.
# Movie Title, Storyline, Poster, Trailer URL.
titanic = media.Movie(
    "The Titanic",
    "Seventeen-year-old Rose hails from an aristocratic family and is set to"
    "be married. When she boards the Titanic,"
    "she meets Jack Dawson, an artist,"
    "and falls in love with him.",
    "https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",
    "https://www.youtube.com/watch?v=2e-eXJ6HgkQ")

# Batman is an object created for class Movie in
# media, that passes movie details as parameters.
# Movie Title, Storyline, Poster, Trailer URL.
Batman = media.Movie(
    "Batman Begins",
    "SeAfter witnessing his parents' death, Bruce learns the art of fighting"
    "to confront injustice. ",
    "https://upload.wikimedia.org/wikipedia/en/thumb/a/af/Batman_Begins_Poster.jpg/220px-Batman_Begins_Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=vak9ZLfhGnQ")

# Avengers is an object created for class Movie in
# media, that passes movie details as parameters.
# Movie Title, Storyline, Poster, Trailer URL.
Avengers = media.Movie(
    "Avengers: Age of Ultron",
    "SevTony Stark builds an artificial intelligence system named Ultron with"
    "the help of Bruce Banner.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/1/1b/Avengers_Age_of_Ultron.jpg/220px-Avengers_Age_of_Ultron.jpg",  # NOQA
    "https://www.youtube.com/watch?v=JAUoeqvedMo")

# Witch_Mountain is an object created for class Movie in
# media, that passes movie details as parameters.
# Movie Title, Storyline, Poster, Trailer URL.
Witch_Mountain = media.Movie(
    "Race to Witch Mountain",
    "SevJack, a taxi driver, finds himself helping two aliens who are trying"
    "to save Earth and themselves from Syphon, a killer from outer space.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/f/f5/Race_to_witch_mountain_film.jpg/220px-Race_to_witch_mountain_film.jpg",  # NOQA
    "https://www.youtube.com/watch?v=SX2PWpcJlrY")

# Wall_Street is an object created for class Movie in
# media, that passes movie details as parameters.
# Movie Title, Storyline, Poster, Trailer URL.
Wall_Street = media.Movie(
    "The Wolf of Wall Street",
    "SeIntroduced to life in the fast lane through stockbroking,"
    "Jordan Belfort"
    "takes a hit after a Wall Street crash.",
    "https://upload.wikimedia.org/wikipedia/en/1/1f/WallStreet2013poster.jpg",
    "https://www.youtube.com/watch?v=iszwuX1AK6A")

# Below line creates a list of movies
movies_list = [
    shawshank,
    titanic,
    Batman,
    Avengers,
    Witch_Mountain,
    Wall_Street
    ]

# Call the function "open_movies_page" from fresh_tomatoes.py
# and pass the "movies_list" as arguments.
fresh_tomatoes.open_movies_page(movies_list)
