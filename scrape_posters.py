import pandas as pd
import requests
import urllib.request
df = pd.read_csv("php/Final.csv")
print(df.columns)

# Do not call this function. It is already called, and all images are downloaded
# For image links and image locations go to poster_locations.csv
# def download_posters():
#     for i,j in zip(df["movie_title"],df["movie_imdb_link"]):
#         try:
#             imdb_url = j
#             res = requests.get(imdb_url).text
#             img_url = res.split('<div class="poster">')[1].split('src="')[1].split('"')[0]
#             img_name = "poster/"+i+".jpg"
#             urllib.request.urlretrieve(img_url,img_name)
#             print(i,"DONE")
#         except:
#             with open("not_done.txt","a") as f:
#                 print(i," ",j," not done",file=f)
#                 print(i,"NOT DONE")

# Do not call this function. It is already called, and has generated the file poster_locations.csv
def annotate_posters():
    titles = []
    image_links = []
    image_location = []
    for i,j in zip(df["movie_title"],df["movie_imdb_link"]):
        try:
            imdb_url = j
            res = requests.get(imdb_url).text
            img_url = res.split('<div class="poster">')[1].split('src="')[1].split('"')[0]
            img_name = "poster/"+i+".jpg"
            titles.append(i)
            image_links.append(img_url)
            image_location.append(img_name)
            print(i,"DONE")
        except:
            with open("not_done.txt","a") as f:
                print(i," ",j," not done",file=f)
                print(i,"NOT DONE")   
    d = {"movie_title":titles,"poster_link":image_links,"poster_location":image_location}
    res = pd.DataFrame(d)
    res.to_csv("poster_locations.csv",index=False)

annotate_posters()