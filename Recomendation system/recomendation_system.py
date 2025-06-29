import pandas as pd
from scipy.stats import pearsonr


rating_data = {
    'Rajeev': {'Apocalypto': 5, 'The Godfather': 5, 'Independence Day': 4, 'Kung Fu Panda': 5},
    'Rohit': {'Apocalypto': 5, 'The Godfather': 4, 'Udaan': 5, 'The Matrix': 4},
    'Chirag': {'Independence Day': 5, 'Kung Fu Panda': 4, 'Fight Club': 5, 'The Dark Knight': 5},
    'Davanshu': {'Udaan': 5, 'The Matrix': 5, 'King Kong': 4},
    'Elvish': {'The Godfather': 4, 'Fight Club': 4, 'The Dark Knight': 5, 'King Kong': 3},
    'You': {'Apocalypto': 5, 'Independence Day': 3, 'The Dark Knight': 4} # Our target user
}


def get_all_recommendations(data, target_user, n_recommendations=3):
    df = pd.DataFrame(data).transpose()
    item_similarity = df.corr(method='pearson', min_periods=2)
    user_ratings = df.loc[target_user].dropna()
    recommendation_scores = pd.Series(dtype='float64')

    for movie, rating in user_ratings.items():
        similar_movies = item_similarity[movie]
        weighted_similarities = similar_movies * rating
        recommendation_scores = recommendation_scores.add(weighted_similarities, fill_value=0)
        

    recommendation_scores = recommendation_scores.drop(user_ratings.index, errors='ignore')
    top_recommendations = recommendation_scores.sort_values(ascending=False)
    return top_recommendations.head(n_recommendations).index.tolist()

recommended_by_me = 'You'
recommendations = get_all_recommendations(rating_data, recommended_by_me)

print(f"Movies rated by '{recommended_by_me}':")
print(rating_data[recommended_by_me])
print("-" * 30)
print(f"Top recommendations for '{recommended_by_me}':")


for i, movie in enumerate(recommendations, 1):
    print(f"{i}. {movie}")