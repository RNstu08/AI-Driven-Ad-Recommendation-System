from src.inference import load_model, recommend

model = load_model()

def get_recommendations(user_id):
    return recommend(user_id, model)
