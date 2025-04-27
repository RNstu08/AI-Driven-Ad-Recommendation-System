# Example for loading the model and making recommendations
model = load_model("model.pkl")

# Choose a random user (e.g., user with index 10)
user_index = 10  # Adjust based on your data

# Get top 5 recommendations
top_5_recommendations = recommend(user_index, model, top_k=5)
print(f"Top 5 recommendations for user {user_index}: {top_5_recommendations}")
