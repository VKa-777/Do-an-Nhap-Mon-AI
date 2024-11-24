import streamlit as st
import pickle

movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list = movies["title"].values

st.header("Movie Recommendation System")
selected_value = st.selectbox("Select movie from the list:",movies_list)

def recommend(title):
    index = movies[movies['title'] == title].index[0]
    distance = sorted(list(enumerate((similarity[index]))), reverse=True, key=lambda x:x[1])
    recommend_movies = []
    for i in distance[1:6]:
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies

if st.button("Show recommend"):
    movies_title = recommend(selected_value)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(movies_title[0])
    with col2:
        st.text(movies_title[1])
    with col3:
        st.text(movies_title[2])
    with col4:
        st.text(movies_title[3])
    with col5:
        st.text(movies_title[4])

