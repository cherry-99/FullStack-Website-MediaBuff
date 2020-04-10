# RESTful API routes to access the intelligent feature of our website
# Hosted as a Flask app on server at localhost:5000

# API to list all genres

route : localhost:5000/api/list/genres || response : a list of all genres in database || response code : 200

# API to list all years from which movies are available

route : localhost:5000/api/list/years || response : a list of all years which are present in database || response code : 200

# API to list top 25 movies from a year

route : localhost:5000/api/top25/year/(year_required) || response : a list of top movies of the year || response code : 200

# API to list top 25 movies from a genre

route : localhost:5000/api/top25/genre/(genre_required) || response : a list of top movies of the genre || response code : 200

# API to list top 50 of all time

route : localhost:5000/api/top50/all_time || response : a list of top movies || response code : 200

# API to list top 25 movies related to a particular movie

route : localhost:5000/api/top25/movie || request body : {"movie_name":"(name of movie)"} || response : a list of movies most related to it || response code : 200

# API to list top 25 movies for a user based on their preferences of actors, directors and genres

route : localhost:5000/api/top25/user || request body : {"user_genres":"genre1,genre2,genre3....genreN","user_directors":"dir1,dir2,dir3...dirN","user_actors":"actor1,actor2....,actorN"} || response : a list of movies best suited to user || response code : 200