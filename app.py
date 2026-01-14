import streamlit as st
import pickle

# Load artifacts
movies = pickle.load(open("artifacts/movies.pkl", "rb"))
similarity = pickle.load(open("artifacts/similarity.pkl", "rb"))

# Recommendation function
def recommend(movie):
    movie_row = movies[movies['title'] == movie]

    if movie_row.empty:
        return []
    
    index = movie_row.index[0]
    distances = similarity[index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )

    recommendations = []
    for i in movies_list[1:6]:
        recommendations.append(movies.iloc[i[0]].title)

    return recommendations

# ---------------- UI ---------------- #
st.set_page_config(page_title="Movie Recommender", page_icon="🎬")

st.title("🎬 Movie Recommendation System")
st.write("Select a movie and get similar recommendations")

selected_movie = st.selectbox(
    "Choose a movie",
    movies['title'].values
)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)

    st.subheader("Recommended Movies:")
    for movie in recommendations:
        st.write("👉", movie)