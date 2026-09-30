from fastapi import FastAPI
from pydantic import BaseModel

import joblib
import mlflow.sklearn
import numpy as np


app = FastAPI(
    title="Florida Red Tide Classifier API",
    version="1.0.0",
)

MODEL_URI = "models:/florida-red-tide-classifier/1"
THRESHOLD = 0.3
FEATURES = [
    "latitude",
    "longitude",
    "grid_latitude",
    "grid_longitude",
    "cell_count",
    "samples_today",
    "sample_depth_m",
    "salinity",
    "water_temp_c",
    "current_severity",
    "current_log1p_cell_count",
    "year",
    "month",
    "day_of_year",
    "season_sin",
    "season_cos",
    "water_temp_missing",
    "salinity_missing",
    "wind_speed_missing",
    "hist_previous_cell_count",
    "hist_previous_log1p_cell_count",
    "hist_days_since_previous_sample",
    "hist_7d_observation_days",
    "hist_7d_mean_cell_count",
    "hist_7d_max_cell_count",
    "hist_7d_bloom_days",
    "hist_7d_bloom_fraction",
    "hist_30d_observation_days",
    "hist_30d_mean_cell_count",
    "hist_30d_max_cell_count",
    "hist_30d_bloom_days",
    "hist_30d_bloom_fraction",
    "hist_90d_observation_days",
    "hist_90d_mean_cell_count",
    "hist_90d_max_cell_count",
    "hist_90d_bloom_days",
    "hist_90d_bloom_fraction",
    "regional_grid_days",
    "regional_7d_observation_days",
    "regional_7d_max_cell_count",
    "regional_7d_bloom_days",
    "regional_30d_observation_days",
    "regional_30d_max_cell_count",
    "regional_30d_bloom_days",
    "regional_90d_observation_days",
    "regional_90d_max_cell_count",
    "regional_90d_bloom_days",
]

model = None
imputer = None


@app.on_event("startup")
def load_model():
    global model, imputer

    model = mlflow.sklearn.load_model(MODEL_URI)
    imputer = joblib.load("artifacts/imputer.joblib")


@app.get("/health")
def health():
    return {
        "status": "ok",
        "model_loaded": model is not None,
    }


class PredictionRequest(BaseModel):
    latitude: float
    longitude: float
    grid_latitude: float
    grid_longitude: float

    cell_count: float
    samples_today: int
    sample_depth_m: float
    salinity: float | None
    water_temp_c: float | None

    current_severity: float
    current_log1p_cell_count: float

    year: int
    month: int
    day_of_year: int

    season_sin: float
    season_cos: float

    water_temp_missing: int
    salinity_missing: int
    wind_speed_missing: int

    hist_previous_cell_count: float
    hist_previous_log1p_cell_count: float
    hist_days_since_previous_sample: float

    hist_7d_observation_days: int
    hist_7d_mean_cell_count: float
    hist_7d_max_cell_count: float
    hist_7d_bloom_days: int
    hist_7d_bloom_fraction: float

    hist_30d_observation_days: int
    hist_30d_mean_cell_count: float
    hist_30d_max_cell_count: float
    hist_30d_bloom_days: int
    hist_30d_bloom_fraction: float

    hist_90d_observation_days: int
    hist_90d_mean_cell_count: float
    hist_90d_max_cell_count: float
    hist_90d_bloom_days: int
    hist_90d_bloom_fraction: float

    regional_grid_days: int

    regional_7d_observation_days: int
    regional_7d_max_cell_count: float
    regional_7d_bloom_days: int

    regional_30d_observation_days: int
    regional_30d_max_cell_count: float
    regional_30d_bloom_days: int

    regional_90d_observation_days: int
    regional_90d_max_cell_count: float
    regional_90d_bloom_days: int


### Endpoint


@app.post("/predict")
def predict(request: PredictionRequest):

    raw_input = np.array(
        [
            [
                np.nan
                if getattr(request, feature) is None
                else getattr(request, feature)
                for feature in FEATURES
            ]
        ]
    )

    input_imputed = imputer.transform(raw_input)

    probability = model.predict_proba(input_imputed)[0][1]

    prediction = int(probability >= THRESHOLD)

    return {
        "prediction": prediction,
        "probability": float(probability),
        "threshold": THRESHOLD,
    }
