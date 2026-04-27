import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

st.title("🎬 Movie Recommender")
st.markdown("### Find movies similar to yours!")

movies_list = ['Toy Story','Jumanji','GoodFellas','Batman','Titanic',
               'The Matrix','Inception','Interstellar','Avatar','Joker',
               'Iron Man','Spider-Man','The Avengers','Frozen','Moana']

genres = ['Animation','Adventure','Crime','Action','Romance',
          'SciFi','SciFi','SciFi','SciFi','Crime',
          'Action','Action','Action','Animation','Animation']

movies = pd.DataFrame({'title': movies_list, 'genre': genres})
genre_dummies = pd.get_dummies(movies['genre'])
similarity = cosine_similarity(genre_dummies)

st.write("---")
movie = st.selectbox("🎥 Pick a movie:", movies_list)
num = st.slider("How many recommendations?", 3, 10, 5)

if st.button("🎯 Get Recommendations"):
    idx = movies[movies['title'] == movie].index[0]
    scores = sorted(list(enumerate(similarity[idx])),
                    key=lambda x: x[1], reverse=True)
    st.success("You might also like:")
    count = 0
    for i, score in scores[1:]:
        st.write(f"**{count+1}.** {movies['title'][i]}")
        count += 1
        if count == num:
            break