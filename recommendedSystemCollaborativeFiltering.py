import pandas as pd
from math import sqrt

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

inputMovies = inputMovies.drop('year', 1)
inputMovies = inputMovies.sort_values(by='movieId')

userSubsetGroup = ratings_df[ratings_df['movieId'].isin(inputMovies['movieId'].tolist())]
userSubsetGroup.head()

userSubsetGroup = userSubsetGroup.groupby(['userId'])

userSubsetGroup = sorted(userSubsetGroup, key=lambda x: len(x[1]), reverse=True)

userSubsetGroup = userSubsetGroup[0:100]

pearsonCorrelationDict = {}

for name, group in userSubsetGroup:
    group = group.sort_values(by='movieId')
    nRatings = len(group)

    tempDef = inputMovies[inputMovies['movieId'].isin(group['movieId'].tolist())]
    tempRatingList = tempDef['rating'].tolist()
    tempGroupRatingList = group['rating'].tolist()
    Sxx = sum([i ** 2 for i in tempRatingList]) - pow(sum(tempRatingList), 2) / float(nRatings)
    Syy = sum([i ** 2 for i in tempGroupRatingList]) - pow(sum(tempGroupRatingList), 2) / float(nRatings)
    Sxy = sum(i * j for i, j in zip(tempRatingList, tempGroupRatingList)) - (sum(tempRatingList) * sum(tempGroupRatingList)) / float(
        nRatings)

    if Sxx != 0 and Syy != 0:
        pearsonCorrelationDict[name] = Sxy / sqrt(Sxx * Syy)
    else:
        pearsonCorrelationDict[name] = 0

pearsonCorrelationDict.items()

pearsonDF = pd.DataFrame.from_dict(pearsonCorrelationDict, orient='index')
pearsonDF.columns = ['similarityIndex']
pearsonDF['userId'] = pearsonDF.index
pearsonDF.index = range(len(pearsonDF))
pearsonDF.head()

topUsers=pearsonDF.sort_values(by='similarityIndex', ascending=False)[0:50]
topUsers.head()

topUsersRating=topUsers.merge(ratings_df, left_on='userId', right_on='userId', how='inner')
topUsersRating.head()

topUsersRating['weightedRating'] = topUsersRating['similarityIndex']*topUsersRating['rating']
topUsersRating.head()

tempTopUsersRating = topUsersRating.groupby('movieId').sum()[['similarityIndex','weightedRating']]
tempTopUsersRating.columns = ['sum_similarityIndex','sum_weightedRating']
tempTopUsersRating.head()

recommendation_df = pd.DataFrame()
recommendation_df['weighted average recommendation score'] = tempTopUsersRating['sum_weightedRating']/tempTopUsersRating['sum_similarityIndex']
recommendation_df['movieId'] = tempTopUsersRating.index
recommendation_df.head()

recommendation_df = recommendation_df.sort_values(by='weighted average recommendation score', ascending=False)
recommendation_df.head(10)

print(movie_df.loc[movie_df['movieId'].isin(recommendation_df.head(10)['movieId'].tolist())])
