from fastapi import FastAPI
from app.predict import get_recommendations
from prometheus_fastapi_instrumentator import Instrumentator


app = FastAPI()

Instrumentator().instrument(app).expose(app)

@app.get("/")
def home():
    return {"message": "Ad Recommendation System Running"}

@app.get("/recommend/{user_id}")
def recommend(user_id: int):
    recommendations = get_recommendations(user_id)
    return {"user_id": user_id, "recommended_items": recommendations}
