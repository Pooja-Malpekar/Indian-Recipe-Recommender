import pickle
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load pickled components
with open("model/irs_recipes_df.pkl", "rb") as f:
    df = pickle.load(f)

with open("model/irs_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("model/irs_tfidf_matrix.pkl", "rb") as f:
    tfidf_matrix = pickle.load(f)

# Core recommendation function
def recommend_recipes(user_ingredients, user_cuisine, max_time=None, top_n=10):
    # Preprocess user input
    user_input = user_ingredients.lower().strip() + ' ' + user_cuisine.lower().strip()
    
    # Convert user input into vector
    user_vector = vectorizer.transform([user_input])
    
    # Compute cosine similarities
    similarities = cosine_similarity(user_vector, tfidf_matrix).flatten()
    
    # Get recipe indices sorted by similarity
    sorted_indices = similarities.argsort()[::-1]
    
    # Filter by max cooking time (if provided)
    filtered_indices = []
    for idx in sorted_indices:
        if max_time is None or df.iloc[idx]["TotalTime"] <= max_time:
            filtered_indices.append(idx)
        if len(filtered_indices) == top_n:
            break
    
    # Get recommended recipes
    results = df.iloc[filtered_indices][['RecipeName', 'Ingredients', 'Instructions', 'TotalTime']]
    return results.reset_index(drop=True)
