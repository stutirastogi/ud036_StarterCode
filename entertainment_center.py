import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "https://images-na.ssl-images-amazon.com/images/I/51Q3H0JX9FL._SY445_.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
frozen = media.Movie("Frozen",
                     "https://vignette.wikia.nocookie.net/world-of-media/images/1/16/Frozen.jpg/revision/latest?cb"
                     "=20151202220439",
                     "https://www.youtube.com/watch?v=TbQm5doF_Uc")
maleficent = media.Movie("Maleficent",
                         "https://geekxlovin.files.wordpress.com/2014/05/wpid-photo-11.jpg",
                         "https://www.youtube.com/watch?v=w-XO4XiRop0")
infinity_war = media.Movie("Infinity War",
                           "https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg",
                           "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

movies = [toy_story, frozen, maleficent, infinity_war]
fresh_tomatoes.open_movies_page(movies)

