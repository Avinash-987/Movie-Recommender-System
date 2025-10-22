import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import ast

# Load CSVs
movies = pd.read_csv('movies.csv')
credits = pd.read_csv('credits.csv', usecols=['movie_id', 'cast', 'crew', 'title'])

# Merge on movie identifiers
movies = movies.merge(credits, left_on='id', right_on='movie_id')

# Preprocessing functions
def clean_data(x):
    if isinstance(x, str):
        return x.replace(" ", "").lower()
    return ''

def parse_cast(x):
    try:
        cast_list = ast.literal_eval(x)
        cast_names = [i['name'] for i in cast_list][:3]  # top 3
        return ' '.join(cast_names)
    except:
        return ''

def parse_crew(x):
    try:
        crew_list = ast.literal_eval(x)
        director = [i['name'] for i in crew_list if i['job'] == 'Director']
        return ' '.join(director)
    except:
        return ''

def parse_genres(x):
    try:
        genre_list = ast.literal_eval(x)
        genres = [i['name'] for i in genre_list]
        return ' '.join(genres)
    except:
        return ''

# Create tags column
movies['cast'] = movies['cast'].apply(parse_cast)
movies['crew'] = movies['crew'].apply(parse_crew)
movies['genres'] = movies['genres'].apply(parse_genres)
movies['overview'] = movies['overview'].fillna('')
movies['tags'] = movies['overview'] + ' ' + movies['genres'] + ' ' + movies['cast'] + ' ' + movies['crew']
movies['tags'] = movies['tags'].apply(clean_data)

# TF-IDF vectorization
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['tags'])
similarity = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Save .pkl files
pickle.dump(movies, open('movie_list.pkl', 'wb'))
pickle.dump(similarity, open('similarity.pkl', 'wb'))

print("Pickle files created successfully!")
