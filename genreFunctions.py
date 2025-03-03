'''
reads from genre file and returns a movie:genres dict
'''
def read_movie_genre(f):
    movie_genres={}
    with open(f, 'r') as file:
        for line in file:
            split = line.strip().split('|')
            genre, movie = split[0].strip(), split[2].strip()
            if movie in movie_genres:
                pass
            else:
                movie_genres[movie]=genre
    return movie_genres

'''
creates genre:movies dictionary from movie_genres dictionary
'''
def create_genre_dict(d):
    genre_to_movies = {}
    
    for movie, genre in d.items():
        if genre in genre_to_movies:
            genre_to_movies[genre].append(str(movie))
        else:
            genre_to_movies[genre] = [movie]
    
    return genre_to_movies

#below still need to be implemented in CLI

def filter_movies(d, thres_rating=3):
    # parameter d: dictionary that maps movie to average rating
    # parameter thres_rating: threshold rating, default value 3
    # return: dictionary that maps movie to average rating
    thres_movies = {}
    for movie, rating in d.items():
        if rating >= thres_rating:
            thres_movies[movie] = rating
    return thres_movies
    
# 3.3
def get_popular_in_genre(genre, genre_to_movies, movie_to_average_rating, n=5):
    # parameter genre: genre name (e.g. "Comedy")
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # parameter n: integer (for top n), default value 5
    # return: dictionary that maps movie to average rating
    
    # Create a dictionary of movies in the genre that have an average rating
    movies_to_ratings = {movie: movie_to_average_rating[movie] for movie in genre_to_movies[genre]}

    # Sort the movies by their average rating in descending order
    sorted_genre_ratings = dict(sorted(movies_to_ratings.items(), key=lambda item: item[1], reverse=True))

    # Return the top n movies (or all if fewer than n)
    return dict(list(sorted_genre_ratings.items())[:n])
    
# 3.4
def get_genre_rating(genre, genre_to_movies, movie_to_average_rating):
    # parameter genre: genre name (e.g. "Comedy")
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # return: average rating of movies in genre
    movies_and_ratings = {movie: movie_to_average_rating[movie] for movie in genre_to_movies[genre]}
    average_rating = sum(movies_and_ratings.values()) / len(movies_and_ratings.values())
    return average_rating
    
# 3.5
def genre_popularity(genre_to_movies, movie_to_average_rating, n=5):
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # parameter n: integer (for top n), default value 5
    # return: dictionary that maps genre to average rating
    genre_ratings = {genre: get_genre_rating(genre, genre_to_movies, movie_to_average_rating) for genre in genre_to_movies}
    genres_sorted_by_ratings = dict(sorted(genre_ratings.items(), key=lambda item: item[1], reverse=True)) #key=lambda item: item[1] tells us to look at the second element in every .items() tuple
    return dict(list(genres_sorted_by_ratings.items())[:n])
