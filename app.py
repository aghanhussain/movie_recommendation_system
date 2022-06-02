import pickle

import streamlit as st
import pandas as pd
import requests

movies = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies['title'].values

similarities = pickle.load(open("similarity.pkl", 'rb'))
api_key = '5bc6840255dbcfd1f5040e66a4a956b5'

def recommend(movie):
    recommended_movies = []
    recommended_movies_posters= []
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarities[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    for a in movie_list:
        movie_id = movies.iloc[a[0]]['movie_id']
        recommended_movies.append(movies.iloc[a[0]]['title'])
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters


def fetch_poster(movie_id):
    response= requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US")
    data= response.json()
    poster_path= "https://image.tmdb.org/t/p/w500/"+data['poster_path']
    return poster_path


st.title("Movie Recommender System")

selected_movie_name = st.selectbox('Select your movie here', movies_list)

if st.button("Recommend"):

    name, posters = recommend(selected_movie_name)
    col1,col2,col3,col4,col5= st.columns(5)
    with col1:
        st.text(name[0])
        st.image(posters[0])
    with col2:
        st.text(name[1])
        st.image(posters[1])
    with col3:
        st.text(name[2])
        st.image(posters[2])
    with col4:
        st.text(name[3])
        st.image(posters[3])
    with col1:
        st.text(name[4])
        st.image(posters[4])




#5bc6840255dbcfd1f5040e66a4a956b5