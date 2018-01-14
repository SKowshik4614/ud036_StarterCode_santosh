import webbrowser

# Movie class takes movie title, storyline, poster and trailer url.
# The class play_trailer plays the trailer in the browser.


class Movie():
    """ This class is used to get the details of the movies """

    def __init__(self, movie_title, movie_storyline, movie_poster_image,
                 movie_triler):
        """ This constractor is initiated when the class Movie is called """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image
        self.trailer_youtube_url = movie_triler


def play_trailer(self):
    """ This code will open the browser and play the trailer """
    webbrowser.open(self.trailer_youtube_url)
