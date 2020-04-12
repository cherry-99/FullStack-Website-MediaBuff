from flask import Flask, request, Response, jsonify
import json
from sqlalchemy import create_engine
import sqlalchemy
import pandas as pd
import numpy as np

app = Flask(__name__)

df = pd.read_csv("../php/Final.csv")
# database creation --- database name = assignment1.db, tables = users
engine = create_engine("sqlite:///users.db")
try:
    sql_command1 = "create table users (username text, password text, email text primary key, actors text, directors text, genres text);"
    with engine.connect() as con:
        con.execute(sql_command1)
        con.execute("PRAGMA foreign_keys=on;")
except:
    pass

# signup API
# body : {"username": username, "password":password, "email":unique unregistered email, "actors":"actor1|actor2|actor3|.....|actorN","directors":"director1|director2|director3|.....|directorN","genres":"genre1|genre2|genre3|.....|genreN"}
# response : 200 = signed up | 400 = account already exists with that email
@app.route('/api/signup', methods=['PUT'])
def add_user():
    body = request.get_json()
    uname = body["username"]
    password = body["password"]
    email = body["email"]
    actors = body["actors"]
    directors = body["directors"]
    genres = body["genres"]
    sql_command = "select username,email from users where email='"+email+"';"
    with engine.connect() as con:
        x = con.execute(sql_command)
        l = [i for i in x]
    if (len(l)!=0):
        return "Email-id already registered",400
    sql_command = "INSERT INTO users (username,password,email,actors,directors,genres) values ('"+uname+"','"+password+"','"+email+"','"+actors+"','"+directors+"','"+genres+"');"
    with engine.connect() as con:
        con.execute(sql_command)
    return "",200

# list all genres
@app.route('/api/list/genres', methods=['GET'])
def list_genres():
    all_genres = []
    for i in df["genres"]:
        x = i.split("|")
        for gen in x:
            all_genres.append(gen)
    all_genres = list(set(all_genres))
    return jsonify(all_genres),200

# list all years
@app.route('/api/list/years', methods=['GET'])
def list_years():
    all_years = sorted(set([i for i in df["title_year"] if not pd.isnull(i)]))
    all_years = [int(i) for i in all_years]
    return jsonify(all_years),200

# top 25 rated movies from a year
@app.route('/api/top25/year/<year_required>', methods=['GET'])
def top25_year(year_required):
    year_required =int(year_required)
    top_movies = []
    for movie,year,score in zip(df["movie_title"],df["title_year"],df["imdb_score"]):
        if year_required == year:
            top_movies.append([movie,score])
    top_movies.sort(key=lambda x:x[1],reverse=True)
    top_movies = top_movies[:25]
    top_movies =[i[0] for i in top_movies]
    return jsonify(top_movies),200

# top 50 rated movies of all time
@app.route('/api/top50/all_time', methods=['GET'])
def top_all_time():
    all_time_top = [[i,j] for i,j in zip(df["movie_title"],df["imdb_score"])]
    all_time_top.sort(key=lambda x:x[1],reverse=True)
    all_time_top = all_time_top[:50]
    all_time_top =[i[0] for i in all_time_top]
    return jsonify(all_time_top),200

# top 25 rated movies from a genre
@app.route('/api/top25/genre/<genre_required>', methods=['GET'])
def top25_genre(genre_required):
    genre_based_movies = []
    for movie,genre,score in zip(df["movie_title"],df["genres"],df["imdb_score"]):
        if genre_required in genre:
            genre_based_movies.append([movie,score])
    genre_based_movies.sort(key=lambda x:x[1],reverse=True)
    genre_based_movies = genre_based_movies[:25]
    genre_based_movies =[i[0] for i in genre_based_movies]
    return jsonify(genre_based_movies),200

# 25 movies related to a particular movie
@app.route('/api/top25/movie', methods=['GET'])
def top25_movie():
    body = request.get_json()
    movie_name = body["movie_name"]
    with open("Predicted_Similar_movies.json","r") as f:
        similarity_scores = json.load(f)
    if "\xa0" not in movie_name:
        movie_name+="\xa0"
    res = similarity_scores[movie_name]
    res =[i[0] for i in res]
    return jsonify(res),200

# 25 movies suggested for a user
# body required : {"email":"email-id"}
@app.route('/api/top25/user', methods=['GET'])
def get_user_suggestions():
    email = request.get_json()["email"]
    sql_command = "select actors,directors,genres from users where email='"+email+"';"
    with engine.connect() as con:
        x = con.execute(sql_command)
        l = [i for i in x]
    users_actors,users_directors,users_genres = l[0][0],l[0][1],l[0][2]
    users_genres = users_genres.split("|")
    users_director = users_directors.split("|")
    users_actors = users_actors.split("|")
    suggestions = []
    for i in df.T.iteritems():
        score = 0
        movie = i[1]["movie_title"]
        actor1 = i[1]["actor_1_name"]
        actor2 = i[1]["actor_2_name"]
        actor3 = i[1]["actor_3_name"]
        director = i[1]["director_name"]
        genres = i[1]["genres"].split("|")
        imdb_score = i[1]["imdb_score"]
        if actor1 in users_actors:
            score+=1.25
        if actor2 in users_actors:
            score+=1.25
        if actor3 in users_actors:
            score+=1.25
        if director in users_director:
            score+=1.25
        gen_score = sum([1 for i in genres if i in users_genres])
        gen_score = (gen_score/len(users_genres))*3
        score+=gen_score
        score = score/8
        suggestions.append([movie,score,imdb_score])
    suggestions.sort(key=lambda x:[-x[1],-x[2]])
    suggestions = suggestions[:50]
    suggestions = [i[0] for i in suggestions]
    return jsonify(suggestions),200

app.run(debug=True)