# 🎬 Movie Recommendation System

A content-based movie recommendation system built using Machine Learning and deployed with Streamlit.  
The system recommends similar movies based on movie metadata such as genres, keywords, cast, crew, and plot overview.

---

## 🔍 Project Overview

This project uses a **content-based filtering approach** to recommend movies.  
Each movie is represented as a vector of textual features, and **cosine similarity** is used to find movies with similar content.

---

## 🛠️ Tech Stack

- Python
- Pandas & NumPy
- Scikit-learn
- Streamlit
- Pickle

---

## 📊 Dataset

- TMDB Movie Metadata Dataset (Kaggle)
- Files used:
  - `movies.csv`
  - `credits.csv`

---

## ⚙️ How It Works

1. Load and merge movie metadata and credits
2. Perform feature engineering on:
   - Genres
   - Keywords
   - Top 3 cast members
   - Director
   - Movie overview
3. Combine features into a single `tags` column
4. Convert text to vectors using **CountVectorizer**
5. Compute similarity using **cosine similarity**
6. Recommend top 5 similar movies
7. Deploy using **Streamlit**

---

## 🚀 Live Demo

👉 (Deployment link coming soon)

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py