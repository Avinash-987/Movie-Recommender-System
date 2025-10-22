import pickle

movies = pickle.load(open('movie_list.pkl', 'rb'))
print(type(movies))       # should be <class 'pandas.core.frame.DataFrame'>
print(movies.columns)     # list all columns
print(movies.head())      # see first few rows
