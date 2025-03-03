'''
Reads data from ratings file
'''
def read_ratings_data(f):   
    movie_ratings = {}
    with open(f, 'r') as file:
        for line in file:
            split = line.strip().split('|') 
            movie, rating = split[0].strip(), split[1].strip()
            rating=float(rating)
            if movie in movie_ratings:
                movie_ratings[movie].append(rating)
            else:
                movie_ratings[movie] = [rating]
    return movie_ratings 

'''
parameter d - movie: ratings dictionary
return: dictionary that maps each movie to their average rating
'''
def calculate_average_rating(d):
    movie_to_avg_rating={}
    for movie in d:
        ratings = d[movie]
        ratings_average = sum(ratings) / len(ratings)
        movie_to_avg_rating[movie] = ratings_average
    return movie_to_avg_rating

'''
parameter d: dictionary that maps movie to average rating
parameter n: top n most popular movies
return: movie:average rating dict w/ n items, sorted from highest to lowest avg rating
'''
def get_popular_movies(d, n=10):
    movies_sorted = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    return dict(list(movies_sorted.items())[:n])