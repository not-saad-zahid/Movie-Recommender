import streamlit as st
import pickle
import pandas
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pandas.DataFrame(movies_dict)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)),reverse=True, key = lambda x:x[1])[:6]
    recommend_movies = []
    for i in movie_list:
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies


st.title('Movie Recommendation System')

selected_movie_name = st.selectbox(
    'Which movie would you like to watch?',
    movies
)

if st.button('Recommend Movie'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
