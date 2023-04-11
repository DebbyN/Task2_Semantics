# L3T12 - Semantic Similarity(NLP)
# Using en_core_web_md language module to select similar movies to watch.

# Import NLP module
import spacy


# Function to select the most appropriate movie to watch next based on its
# description's similarity level to that of the movie 'Planet Hulk'.
def next_movie(fave_movie):
    # Setup variables to manage the check for highest level of similarity  
    nlp = spacy.load('en_core_web_md')
    favourite = nlp(fave_movie)
    movie_list = []
    movie_level = 0
    similar_level = 0

    # Read the movies file to check movie descriptions.
    with open("movies.txt", "r") as movies:
        lines = movies.readlines()

        # Compare movie descriptions against the favourite movie's description
        # to find the one most similar according the the vectorisation language
        # module.
        for l in lines:
            movie_list = l.split(":")
            movie_choice = nlp(movie_list[1])
            movie_level = movie_choice.similarity(favourite)
            # Print details and levels for each movie
            print(f"\n Movie: {movie_list[0]}, Level: {movie_level}")
            print(f"\n Movie Description: {movie_list[1]}")
            
            #Compare the various movie's simalrity level to find the best fit
            if movie_level > similar_level:
                next_movie = movie_list[0]
                similar_level = movie_level

    # Return the movie title for display
    return next_movie

# Main program

# Description of favourite movie to be compared to the other movies
fave_movie = "Will he save their world or destroy it? When the Hulk\
becomes too dangerous for the Earth, the Illuminati trick Hulk\
into a shuttle and launch him into space to a planet where the Hulk can\
live in peace. Unfortunately, Hulk land on the planet Sakaar where\
he is sold into slavery and trained as a gladiator."

#Print favourite movie title and description
print(f"\nMovie Title: 'World Hulk', Description: \n {fave_movie}")

# Run the function to check for the movie with the most similar description to
# favourite and display the Movie title as per the movie.txt file.
watch_next = next_movie(fave_movie)
print(f"\nNext movie to watch is: {watch_next}")
 
    


        
