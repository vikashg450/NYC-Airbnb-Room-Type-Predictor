from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import pandas as pd
import joblib


# ──────────────────────────────────────────────
# App setup
# ──────────────────────────────────────────────
app = FastAPI(
    title="NYC Airbnb Room Type Predictor",
    description="Predict whether a NYC Airbnb listing is an entire home, private room, or shared room.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Restrict to your domain in production if needed
    allow_methods=["*"],
    allow_headers=["*"],
)

# ──────────────────────────────────────────────
# Model
# ──────────────────────────────────────────────
COLUMNS = [
    "latitude", "longitude", "price", "minimum_nights",
    "number_of_reviews", "reviews_per_month",
    "calculated_host_listings_count", "availability_365",
    "neighbourhood_group", "neighbourhood",
]

model = joblib.load("Model_Pipeline.pkl")


# ──────────────────────────────────────────────
# Request schema
# ──────────────────────────────────────────────
class Features(BaseModel):
    latitude:                       float = Field(..., ge=-90,  le=90,  description="Latitude coordinate")
    longitude:                      float = Field(..., ge=-180, le=180, description="Longitude coordinate")
    price:                          float = Field(..., gt=0,            description="Price per night (USD)")
    minimum_nights:                 int   = Field(..., ge=1,   le=365, description="Minimum nights required")
    number_of_reviews:              int   = Field(..., ge=0,            description="Total review count")
    reviews_per_month:              float = Field(..., ge=0,            description="Average monthly reviews")
    calculated_host_listings_count: int   = Field(..., ge=0,            description="Host's total listings")
    availability_365:               int   = Field(..., ge=0,   le=365, description="Days available per year")
    neighbourhood_group:            str   = Field(..., min_length=1,    description="NYC borough")
    neighbourhood:                  str   = Field(..., min_length=1,    description="Neighbourhood name")


# ──────────────────────────────────────────────
# Routes
# ──────────────────────────────────────────────
@app.get("/", tags=["health"])
def health_check():
    return {"status": "ok", "message": "NYC Airbnb Room Type Predictor API is running."}


@app.post("/predict", tags=["prediction"])
def predict(features: Features):
    # Use model_dump() (Pydantic v2) with fallback to dict() (Pydantic v1)
    data = features.model_dump() if hasattr(features, "model_dump") else features.dict()
    row  = pd.DataFrame([data], columns=COLUMNS)

    prediction  = model.predict(row)
    probability = model.predict_proba(row)

    return {
        "Predicted_room_type": prediction[0],
        "Probability":         probability.tolist()[0],
    }