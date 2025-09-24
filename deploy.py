import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

ps = PorterStemmer()

def stem(text):
    y=[]
    for i in text.split():
        y.append(ps.stem(i))

        return " ".join(y)
    
def recommend(movie):
    if movie not in new_df['title'].values:
        return ["Sorry, we couldn't find this movie in our database."]
    
    movie_index=new_df[new_df['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(new_df.iloc[i[0]]['title'])  # Append the movie titles
    return recommended_movies

movies=pd.read_csv("tmdb_5000_movies.csv")
credits=pd.read_csv("tmdb_5000_credits.csv")
new_df=pd.read_csv("main_data.csv")
new_df['tags'] = new_df['tags'].astype(str)

cv=CountVectorizer(max_features=5000,stop_words='english')
cv.fit_transform(new_df['tags'])
vectors=cv.fit_transform(new_df['tags']).toarray()
ps=PorterStemmer()
new_df['tags']=new_df['tags'].apply(stem)
similarity=cosine_similarity(vectors)

st.title("MOVIE RECOMMENDATION SYSTEM")
movie_name = st.selectbox("Select a Movie", options=["Select a Movie"] + new_df['title'].tolist())

if movie_name != "Select a Movie":
    recommendations = recommend(movie_name)
    st.subheader(f"Recommended Movies based on '{movie_name}':")
    for movie in recommendations:
        st.write(f"- {movie}")
else:
    st.info("Please enter a movie name to get recommendations.")
