'''
parameter f: movie ratings file name (e.g. "movieRatingSample.txt")
return: dictionary that maps user to list of (movie,rating)
'''
def read_user_ratings(f):
    user_to_movies = {}

    with open(f, 'r') as file:
        for line in file:
            movie, rating, user = line.strip().split('|')
            user = int(user)  # Convert user ID to integer
            rating = float(rating)  # Convert rating to float
            
            if user not in user_to_movies:
                user_to_movies[user] = []  # Initialize an empty list for the user
            
            user_to_movies[user].append((movie, rating))  # Append movie and rating tuple
    
    return user_to_movies
'''
returns top genre of specified user ID by evaluating those items in the user:movies dict
'''
def get_user_genre(user_id, user_to_movies, movie_to_genre):
    movies = user_to_movies[user_id]
    movie_names = []
    
    genre_rating = {}
    for i in movies:
        movie_names.append(i[0])
        genre = movie_to_genre[i[0]]
        rating = i[1]
        if genre not in genre_rating:
            genre_rating[genre] = [float(rating), 1]
        else:
            genre_rating[genre][0] += float(rating)
            genre_rating[genre][1] += 1

    user_genre_average_rating = {}
    for f, k in genre_rating.items():
        user_genre_average_rating[f] = k[0] / k[1]

    top_genre = max(user_genre_average_rating, key=user_genre_average_rating.get)

    return top_genre
'''
recommends three most popular movies from user's top genre that the user hasn't already rated
'''
def recommend_movies(user_id, user_to_movies, movie_to_genre, movie_to_average_rating):
    movies = user_to_movies[user_id]
    movie_names = []
    
    genre_rating = {}
    for i in movies:
        movie_names.append(i[0])
        genre = movie_to_genre[i[0]]
        rating = i[1]
        if genre not in genre_rating:
            genre_rating[genre] = [float(rating), 1]
        else:
            genre_rating[genre][0] += float(rating)
            genre_rating[genre][1] += 1

    user_genre_average_rating = {}
    for f, k in genre_rating.items():
        user_genre_average_rating[f] = k[0] / k[1]

    top_genre = max(user_genre_average_rating, key=user_genre_average_rating.get)

    movies_in_top_genre = []

    for movie in movie_to_genre:
        if (movie_to_genre[movie] == top_genre):
            movies_in_top_genre.append(movie)

    movies_top_genre_rating = []
    for movie in movies_in_top_genre:
        if (movie in movie_names):
            continue
        
        movie_rating = movie_to_average_rating[movie]
        movies_top_genre_rating.append((movie, movie_rating))

    movies_top_genre_rating.sort(key = lambda x: -x[1])
    top_movies = movies_top_genre_rating

    return_dict = {}
    counter = 0
    for movie_with_rating in top_movies:
        if (counter > 2):
            break
        return_dict[movie_with_rating[0]] = movie_with_rating[1]
        
    return return_dict