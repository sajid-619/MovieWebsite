import webbrowser

"""This class provides a way to store movies"""

# class for movies
class Movie():
    """
    ... this is the class documentation docstring ...
    insert here some information about your class
    """

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """ ... this is the constructor method docstring ...
        here you should include some information about the function behavior and
        its input and outputs (if applicable)
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # function for showing trailer
    def show_trailer(self):
        """ show_trailer() docstring...
        here you should include information about the function
        """
        webbrowser.open(self.trailer_youtube_url)
