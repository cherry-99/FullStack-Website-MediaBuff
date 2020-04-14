#%%
import pandas as pd
import numpy as np
import json

#%%
df = pd.read_csv("/home/adithya/projects/wt2_project/FullStack-Website-MediaBuff/php/Final.csv")
for i in df:
    print(i)

#%%
features = ["director_name","genres","imdb_score","language","plot_keywords","content_rating"]
data = {}
count = 0
drop = []
l = []
for i in df.T.iteritems():
    if i[1]["movie_title"] in data:
        drop.append(i[0])
        l.append(i[1]["movie_title"])
        count+=1
    else:
        data[i[1]["movie_title"]]={}
        for j in features:
            if pd.isnull(i[1][j]):
                if j in ["genres","plot_keywords"]:
                    data[i[1]["movie_title"]][j] = []
                elif j == "imdb_score":
                    data[i[1]["movie_title"]][j] = 0
                else:
                    data[i[1]["movie_title"]][j] = ""
            else:
                if j in ["genres","plot_keywords"]:
                    data[i[1]["movie_title"]][j] = i[1][j].split("|")
                else:
                    data[i[1]["movie_title"]][j] = i[1][j]
        data[i[1]["movie_title"]]["actor_list"]=[]
        for j in ["actor_1_name","actor_2_name","actor_3_name"]:
            if pd.isnull(i[1][j]):
                pass
            else:
                data[i[1]["movie_title"]]["actor_list"].append(i[1][j])

#%%
# actors shall be scored out of 2.25 (3=all match, 2=two match, 1=one match)
# director shall be scored out of 0.75
# genres shall be scored out of 2 as ((number of common)/(no of genres in larger list))*2
# plot_keywords to be scored out of 1 as ((number of common)/(no of keywords in larger list))
# language scored out of 0.5
# content rating scored out of 0.25
# imdb_score as 2.5 (1-(diff(i,j))*2.5
# total score = (sum of above scores)/(9.25)
# if name is present in the name, it get +0.15 to final similarity score
def get_similarity_score(a,b,name_a,name_b):
    score = 0
    total = ((min(len(a["actor_list"]),len(b["actor_list"])))*0.75)+2.5+2
    if a["director_name"]!="" or b["director_name"]!="":
        if a["director_name"] == b["director_name"] :
            score+=0.75
        total+=0.75
    for i in a["actor_list"]:
        if i in b["actor_list"]:
            score+=0.75
    if a["language"]!="" or b["language"]!="":
        if a["language"]==b["language"]:
            score+=0.5
        total+=0.5
    if a["content_rating"]!="" or b["content_rating"]!="":
        if a["content_rating"]==b["content_rating"]:
            score+=0.25
        total+=0.25
    genre_score = 0
    for i in a["genres"]:
        if i in b["genres"]:
            genre_score+=1
    genre_score = (genre_score/(max(len(a["genres"]),len(b["genres"]))))*2
    score+=genre_score
    if len(a["plot_keywords"])!=0 and len(a["plot_keywords"])!=0: 
        plot_score = 0
        for i in a["plot_keywords"]:
            if i in b["plot_keywords"]:
                genre_score+=1
        plot_score = plot_score/(max(len(a["plot_keywords"]),len(b["plot_keywords"])))
        score+=plot_score
        total+=1
    if a["imdb_score"]>=b["imdb_score"]:
        imdb_rating_score = max(-1.5,(1-(a["imdb_score"]-b["imdb_score"]))*2.5)
    else:
        imdb_rating_score = max(-1.5,(1-(b["imdb_score"]-a["imdb_score"]))*2.5)
    score+=imdb_rating_score
    score = score/total
    if (name_a[:len(name_a)-4] in name_b) or (name_b[:len(name_b)-4] in name_a):
        score+=0.15
    return score

#%%
movies = [i for i in data]
similarity = {}
for i in movies:
    sim_scores = {}
    for j in movies:
        if i!=j:
            if j in similarity:
                sim_scores[j] = similarity[j][i]
            else:
                sim_scores[j] = get_similarity_score(data[i],data[j],i,j)
    similarity[i] = sim_scores

with open('similarity_scores.json', 'w') as fp:
    json.dump(similarity, fp)

with open("/home/adithya/projects/wt2_project/similarity_scores.json","r") as f:
    similarity = json.load(f)

results = {}
for i,j in similarity.items():
    l = [(a,b) for a,b in j.items()]
    l.sort(key = lambda x:x[1], reverse=True)
    l = l[:25]
    results[i]=l

with open("./FullStack-Website-MediaBuff/Predicted_Similar_movies.json","w") as f:
    json.dump(results,f)

#%%
# this cell is to print all actors, in decreasing order of movies they have acted in
actors_list = []
actors = {}
for i,j,k in zip(df["actor_1_name"],df["actor_2_name"],df["actor_3_name"]):
    if i in actors:
        actors[i]+=1
    else:
        actors[i]=1
    if j in actors:
        actors[j]+=1
    else:
        actors[j]=1
    if k in actors:
        actors[k]+=1
    else:
        actors[k]=1
actors = [[i,j] for i,j in actors.items()]
actors.sort(key=lambda x:-x[1])
actors.remove([np.nan,43])
with open("./FullStack-Website-MediaBuff/actors.txt","w") as f:
    for i in actors:
        print(i[0],file=f)

#%%
# this cell is to print all directors, in decreasing order of movies they have directed in
directors = {}
for i in df["director_name"]:
    if i in directors:
        directors[i]+=1
    else:
        directors[i]=1
directors = [[i,j] for i,j in directors.items()]
directors.sort(key=lambda x:-x[1])
directors.remove([np.nan,104])
with open("./FullStack-Website-MediaBuff/directors.txt","w") as f:
    for i in directors:
        print(i[0],file=f)

#%%
year_required = 2016
top_movies = []
for movie,year,score in zip(df["movie_title"],df["title_year"],df["imdb_score"]):
    if year_required == year:
        top_movies.append([movie,score])
top_movies.sort(key=lambda x:x[1],reverse=True)
top_movies = top_movies[:25]
top_movies

#%%
