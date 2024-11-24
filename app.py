import streamlit as st
import pickle
import requests

movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list = movies["title"].values

st.header("Movie Recommendation System")
selected_value = st.selectbox("Select movie from the list:",movies_list)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=53a78a6c12e54ecc259e9f7564d8f75a&language=en-US".format(movie_id)
    data = requests.get(url).json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" +poster_path
    return full_path


def recommend(title):
    index = movies[movies['title'] == title].index[0]
    distance = sorted(list(enumerate((similarity[index]))), reverse=True, key=lambda x:x[1])
    recommend_movies = []
    recommend_posters = []
    for i in distance[1:6]:
        movie_id = movies.iloc[i[0]].id
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_posters.append(fetch_poster(movie_id))
    return recommend_movies,recommend_posters

if st.button("Show recommend"):
    movies_title, movies_poster = recommend(selected_value)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(movies_title[0])
        st.image(movies_poster[0])
    with col2:
        st.text(movies_title[1])
        st.image(movies_poster[1])
    with col3:
        st.text(movies_title[2])
        st.image(movies_poster[2])
    with col4:
        st.text(movies_title[3])
        st.image(movies_poster[3])
    with col5:
        st.text(movies_title[4])
        st.image(movies_poster[4])

