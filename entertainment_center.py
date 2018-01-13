# This programe will take movie details as input and creates a list of movies and calls media.py to play the trailer or read movie details.
# Import the files fresh_tomatoes and media files.

import fresh_tomatoes
import media

shawshank = media.Movie("The Shawshank Redemption",
                        "Andy Dufresne, a successful banker, is arrested for the murders of his wife and her lover.",
                        "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                        "https://www.youtube.com/watch?v=NmzuHjWmXOc")

titanic = media.Movie("The Titanic",
                        "Seventeen-year-old Rose hails from an aristocratic family and is set to be married. When she boards the Titanic, she meets Jack Dawson, an artist, and falls in love with him.",
                        "https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",
                        "https://www.youtube.com/watch?v=2e-eXJ6HgkQ")

Batman = media.Movie("Batman Begins",
                        "SeAfter witnessing his parents' death, Bruce learns the art of fighting to confront injustice. ",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/a/af/Batman_Begins_Poster.jpg/220px-Batman_Begins_Poster.jpg",
                        "https://www.youtube.com/watch?v=vak9ZLfhGnQ")

Avengers = media.Movie("Avengers: Age of Ultron",
                        "SevTony Stark builds an artificial intelligence system named Ultron with the help of Bruce Banner.",
                        "https://github.com/SKowshik4614/ud036_StarterCode_santosh/blob/master/images/Avengers.jpg",
                        "https://www.youtube.com/watch?v=JAUoeqvedMo")

Witch_Mountain = media.Movie("Race to Witch Mountain",
                        "SevJack, a taxi driver, finds himself helping two aliens who are trying to save Earth and themselves from Syphon, a killer from outer space.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/f/f5/Race_to_witch_mountain_film.jpg/220px-Race_to_witch_mountain_film.jpg",
                        "https://www.youtube.com/watch?v=SX2PWpcJlrY")

Wall_Street = media.Movie("The Wolf of Wall Street",
                        "SeIntroduced to life in the fast lane through stockbroking, Jordan Belfort takes a hit after a Wall Street crash.",
                        "https://upload.wikimedia.org/wikipedia/en/1/1f/WallStreet2013poster.jpg",
                        "https://www.youtube.com/watch?v=iszwuX1AK6A")

# Below line creates a list of movies						
movies_list = [shawshank, titanic, Batman, Avengers, Witch_Mountain, Wall_Street]

# Call the function "open_movies_page" from fresh_tomatoes.py and pass the "movies_list" as arguments.
fresh_tomatoes.open_movies_page(movies_list)
