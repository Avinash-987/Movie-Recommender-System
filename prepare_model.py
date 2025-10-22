import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1️⃣ Load CSV files
movies = pd.read_csv('movies.csv')
credits = pd.read_csv('credits.csv')

# Inspect columns to find the correct merge keys
# print(movies.columns)
# print(credits.columns)

# 2️⃣ Merge on correct columns
# Adjust if your columns differ
movies = movies.merge(credits, left_on='id', right_on='movie_id')

# 3️⃣ Fill missing overviews with empty strings
movies['overview'] = movies['overview'].fillna('')

# 4️⃣ TF-IDF Vectorization on movie overviews
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['overview'])

# 5️⃣ Compute cosine similarity
similarity = cosine_similarity(tfidf_matrix, tfidf_matrix)

# 6️⃣ Save the processed movie list and similarity matrix
with open('movie_list.pkl', 'wb') as f:
    pickle.dump(movies, f)

with open('similarity.pkl', 'wb') as f:
    pickle.dump(similarity, f)

print("Model and data prepared successfully!")
# Rename 'original_title' to 'title' for consistency
movies.rename(columns={'original_title': 'title'}, inplace=True)

