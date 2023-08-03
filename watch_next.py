# Import spacy
import spacy
# Load language model
nlp = spacy.load("en_core_web_md")
# Open and read movie descriptions
with open("movies.txt") as mov_file:
    movie_descs = [line for line in mov_file.readlines()]
# Collect movie title and description for access
movies_dict = {movie[:7]: nlp(movie[9:]) for movie in movie_descs}


def up_next(movie_desc):
    """Return a movie title based on description similarity.

       Compare semantic similarity of a given movie description to those found
       in movies_dict.
    """
    desc_nlp = nlp(movie_desc)
    next_to_watch = ["", 0]
    # Iterate through movies
    for movie in movies_dict:
        # Compare similarities and keep highest
        if desc_nlp.similarity(movies_dict[movie]) > next_to_watch[1]:
            next_to_watch = [movie, desc_nlp.similarity(movies_dict[movie])]
    return next_to_watch[0]


test_movie = "Will he save their world or destroy it? When the Hulk becomes \
    too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and \
    launch him into space to a planet where the Hulk can live in peace. \
    Unfortunately, Hulk lands on the planet Sakaar where he is sold into \
    slavery and trained as a gladiator"

print(up_next(test_movie))
