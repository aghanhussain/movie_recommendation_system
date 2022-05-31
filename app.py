import pickle

import streamlit as st
import pandas as pd

movies = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies['title'].values

similarities = pickle.load(open("similarity.pkl", 'rb'))


def recommend(movie):
    recommended_movies = []
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarities[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    for a in movie_list:
        recommended_movies.append(movies.iloc[a[0]]['title'])
    return recommended_movies


st.title("Movie Recommender System")

selected_movie_name = st.selectbox('Select your movie here', movies_list)

if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)
    for rec_movie in recommendations:
        st.write(rec_movie)
