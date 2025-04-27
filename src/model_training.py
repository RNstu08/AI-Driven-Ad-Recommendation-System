import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
import joblib

def create_user_item_matrix(data):
    """Creates a user-item matrix."""
    matrix = data.pivot_table(index='visitorid', columns='itemid', values='event', aggfunc='count', fill_value=0)
    return matrix

def train_model(matrix):
    """Train a recommendation model using cosine similarity on the user-item matrix."""
    similarity_matrix = cosine_similarity(matrix)
    return similarity_matrix

def save_model(model, filename="model.pkl"):
    """Save the trained model to a file."""
    print(f"Saving model to {filename}...")
    joblib.dump(model, filename)
    print(f"Model saved to {filename}")

# Main code for loading data, training the model, and saving the model
if __name__ == "__main__":
    # Load the data from the events file
    data = pd.read_csv("data/retailrocket/events.csv")  # Adjust path if needed

    # Limit the number of unique users and items (adjust N as needed)
    N_users = 5000  # Limit to the first 5000 users (for example)
    N_items = 1000  # Limit to the first 1000 items (for example)

    # Get top N users and items based on frequency
    top_users = data['visitorid'].value_counts().nlargest(N_users).index
    top_items = data['itemid'].value_counts().nlargest(N_items).index

    # Filter the data to include only the top N users and items
    data_sampled = data[data['visitorid'].isin(top_users) & data['itemid'].isin(top_items)]
    print(f"Sampled {len(data_sampled)} rows from {len(data)}")

    # Create the user-item matrix from the sampled data
    matrix = create_user_item_matrix(data_sampled)
    
    # Train the model using the user-item matrix
    model = train_model(matrix)
    
    # Save the trained model to a file
    save_model(model, "model.pkl")
