import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity
import joblib

def create_user_item_matrix(data):
    """Creates a sparse user-item matrix."""
    matrix = data.pivot_table(index='visitorid', columns='itemid', values='event', aggfunc='count', fill_value=0)
    sparse_matrix = csr_matrix(matrix.values)
    return sparse_matrix

def train_model(matrix):
    """Train a recommendation model using cosine similarity on a sparse matrix."""
    similarity_matrix = cosine_similarity(matrix)
    return similarity_matrix

def save_model(model, filename="model.pkl"):
    """Save the trained model to a file."""
    print(f"Saving model to {filename}...")
    joblib.dump(model, filename)
    print(f"Model saved to {filename}")

# Example for running the model training
if __name__ == "__main__":
    # Load the data from the events file
    data = pd.read_csv("data/retailrocket/events.csv")  # Adjust the path if needed
    
    # Create the user-item matrix from the data
    matrix = create_user_item_matrix(data)
    
    # Train the model using the user-item matrix
    model = train_model(matrix)
    
    # Save the trained model to a file
    save_model(model, "model.pkl")
