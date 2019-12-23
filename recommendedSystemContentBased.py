import pandas as pd

movie_df = pd.read_csv("./dataset/ml-latest/movies.csv")
ratings_df = pd.read_csv("./dataset/ml-latest/ratings.csv")

movie_df.head()

movie_df['year'] = movie_df.title.str.extract('(\(\d\d\d\d\))', expand=False)
movie_df['year'] = movie_df.year.str.extract('(\d\d\d\d)', expand=False)

movie_df['title'] = movie_df.title.str.replace('(\(\d\d\d\d\))', '')
movie_df['title'] = movie_df['title'].apply(lambda x: x.strip())
movie_df.head()

movie_df['genres'] = movie_df.genres.str.split('|')

movieWithGenres_df = movie_df.copy()

for index, row in movie_df.iterrows():
    for genre in row['genres']:
        movieWithGenres_df.at[index, genre] = 1
movieWithGenres_df = movieWithGenres_df.fillna(0)
movieWithGenres_df.head()

ratings_df.head()

ratings_df = ratings_df.drop('timestamp', 1)
ratings_df.head()

userInput = [
            {'title':'Breakfast Club, The', 'rating':5},
            {'title':'Toy Story', 'rating':3.5},
            {'title':'Jumanji', 'rating':2},
            {'title':"Pulp Fiction", 'rating':5},
            {'title':'Akira', 'rating':4.5}
         ]
inputMovies = pd.DataFrame(userInput)

inputId = movie_df[movie_df['title'].isin(inputMovies['title'].tolist())]

inputMovies = pd.merge(inputId, inputMovies)
inputMovies = inputMovies.drop('genres',1).drop('year',1)

userMovies = movieWithGenres_df[movieWithGenres_df['movieId'].isin(inputMovies['movieId'].tolist())]
userMovies = userMovies.reset_index(drop=True)
userGenreTable = userMovies.drop('movieId', 1).drop('title', 1).drop('genres', 1).drop('year', 1)

userProfile = userGenreTable.transpose().dot(inputMovies['rating'])

genreTable = movieWithGenres_df.set_index(movieWithGenres_df['movieId'])
genreTable = genreTable.drop('movieId', 1).drop('title', 1).drop('genres', 1).drop('year', 1)
genreTable.head()

recommendationTable_df = ((genreTable*userProfile).sum(axis=1))/(userProfile.sum())
recommendationTable_df.head()

recommendationTable_df = recommendationTable_df.sort_values(ascending=False)
recommendationTable_df.head()

ans = movie_df.loc[movie_df['movieId'].isin(recommendationTable_df.head(5).keys())]
print(ans)
