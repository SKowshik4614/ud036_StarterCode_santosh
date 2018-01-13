import webbrowser

# Movie class takes movie title, storyline, poster and trailer url.
# The class play_trailer plays the trailer in the browser.
class Movie(): 
      def __init__(self, movie_title, movie_storyline, movie_poster_image, movie_triler):
            self.title = movie_title
            self.storyline = movie_storyline
            self.poster_image_url = movie_poster_image
            self.trailer_youtube_url = movie_triler
    
      def play_trailer(self):
            webbrowser.open(self.trailer_youtube_url)