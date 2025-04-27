import joblib
import numpy as np

def load_model(filename="model.pkl"):
    """Load the trained model from a file."""
    return joblib.load(filename)

def recommend(user_index, model, top_k=5):
    """Recommend top K items for a given user based on cosine similarity."""
    user_scores = model[user_index]  # Get the scores (similarity values) for the given user
    recommended = np.argsort(user_scores)[-top_k:]  # Sort and get the top K recommended items
    return recommended
