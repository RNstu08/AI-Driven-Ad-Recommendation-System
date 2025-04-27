from fastapi import FastAPI
from src.inference import load_model, recommend
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

# PROMETHEUS setup
instrumentator = Instrumentator().instrument(app).expose(app)

# Load your model
model = load_model()

@app.get("/recommend/{user_id}")
def get_recommendations(user_id: int):
    recommendations = recommend(user_id, model)
    return {"user_id": user_id, "recommendations": recommendations}
