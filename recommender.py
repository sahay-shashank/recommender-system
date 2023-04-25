from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import pandas as pd
import ast
from sklearn.metrics.pairwise import cosine_similarity
def getname(i):
    genre=[]
    for i in ast.literal_eval(i):
        genre.append(i['name'])
    return " ".join(genre)
data = pd.read_csv('movies_metadata.csv',low_memory=False)
# data.dropna(inplace=True)
print(1)

cv = CountVectorizer()
data_matrix = cv.fit_transform(data["genres"].map(getname))
print(2)
similarity_matrix = cosine_similarity(data_matrix)
print(3)
def recommend_items(title, similarity_matrix, data):
    # Get index of user
    user_index = data.index[data['original_title'] == title].tolist()[0]
    print(4)
    # Compute similarities between user and all other items
    similarities = list(enumerate(similarity_matrix[user_index]))
    print(5)
    # Sort similarities by highest to lowest
    similarities = sorted(similarities, key=lambda x: x[1], reverse=True)
    print(6)
    # Get top 10 similar items
    top_similar_items = [i[0] for i in similarities[1:11]]
    print(7)
    # Return recommended items
    return data.iloc[top_similar_items]

recommendations = recommend_items(title="Toy Story", similarity_matrix=similarity_matrix, data=data)
print(8)
print(recommendations['original_title'])


