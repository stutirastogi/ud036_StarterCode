"""
class to store movie details.

This class contains the attributes that define movie object.

title is the title of movie to be displayed
poster_image_url is the url of the thumbnail of movie
trailer_youtube_url is the link to youtube video of it's trailer

"""


class Movie:
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
