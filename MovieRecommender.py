from ratingsFunctions import read_ratings_data, calculate_average_rating, get_popular_movies
from genreFunctions import read_movie_genre, create_genre_dict, filter_movies, get_popular_in_genre, get_genre_rating, genre_popularity
from userRatings import read_user_ratings, get_user_genre, recommend_movies
from collections import defaultdict
from collections import Counter

'''
add an assert to make sure user inputs correct formatting
'''
def add_user_rating(file_name, user_id, movie, rating): #file_name must be input as a path to the ratings file that is being adjusted
    with open(file_name, 'a') as file:
        file.write(f'{movie}|{rating}|{user_id}\n')


def main():
    ratings_file = "ratings.txt"
    genre_file = "genres.txt"


    movie_ratings = read_ratings_data(ratings_file)
    movie_genres = read_movie_genre(genre_file)
    genre_to_movies = create_genre_dict(movie_genres)
    movie_to_avg_rating = calculate_average_rating(movie_ratings)
    user_to_movies = read_user_ratings(ratings_file)


    while True:
        print("\nCommands:")
        print("1. Add new rating (format: add user_id movie_name rating)")
        print("2. Get top-rated movies (format: popular n)")
        print("3. Get recommended movies for user (format: recommend user_id)")
        print("4. Exit")
       
        user_input = input("Enter command: ").strip().split(" ")


        if user_input[0] == "add" and len(user_input) == 4:
            user_id = int(user_input[1])
            movie = user_input[2]
            rating = float(user_input[3])
            add_user_rating(ratings_file, user_id, movie, rating)
            user_to_movies = read_user_ratings(ratings_file)  # Refresh data
       
        elif user_input[0] == "popular":
            n = int(user_input[1]) if len(user_input) > 1 else 10
            popular_movies = get_popular_movies(movie_to_avg_rating, n)
            print("\nTop Movies:")
            for movie, rating in popular_movies.items():
                print(f"{movie}: {rating:.2f}/5")
       
        elif user_input[0] == "recommend" and len(user_input) == 2:
            user_id = int(user_input[1])
            if user_id not in user_to_movies:
                print("User not found.")
                continue
            recommendations = recommend_movies(user_id, user_to_movies, movie_genres, movie_to_avg_rating)
            print("\nRecommended Movies:")
            for movie, rating in recommendations.items():
                print(f"{movie}: {rating:.2f}/5")


        elif user_input[0] == "exit":
            print("Exiting program.")
            break
       
        else:
            print("Invalid command. Try again.")


main()

