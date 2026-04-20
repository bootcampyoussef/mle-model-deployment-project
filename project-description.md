# Model Deployment Project

## Project Goal

Train and locally deploy a machine learning model that predicts the duration of New York City yellow taxi trips.

Use:

- `scikit-learn` to train a `RandomForestRegressor`
- `MLflow` to track experiments locally
- `FastAPI` to serve predictions through an API
- a local request client such as `curl` or `requests` to validate the endpoint

This project is intentionally local first.

## Dataset

Yellow Taxi trip records: [NYC TLC trip record data](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

- Year: `2025`
- Month: `01`
- Target: trip `duration`

## Core Deliverables

1. Train a baseline `RandomForestRegressor` model.
2. Track the training run in local MLflow.
3. Package the preprocessing and model logic into reusable Python code.
4. Build a prediction API that runs locally.
5. Send at least one request to the API and confirm that it returns a prediction.

## Suggested Workflow

1. Load the January 2025 taxi data and inspect the columns that influence trip duration.
2. Create a clean training dataset and define the target variable.
3. Split the data into train and validation sets.
4. Train a baseline random forest model.
5. Evaluate the model with RMSE and log the run in MLflow.
6. Refactor feature preparation and model loading into modules you can reuse from both training code and the API.
7. Build a FastAPI app with a `/predict` endpoint.
8. Run the API locally and send a sample request.
9. Document your results and tradeoffs in the README.

## Local-First Deployment Guidance

Choose one of these local deployment paths:

- run the API directly with `uvicorn`
- package the API in Docker and run it locally

Keep the deployment workflow easy to build, run, and review on a single machine.

## What To Submit

- training code
- preprocessing or feature engineering code
- model tracking setup with MLflow
- a local prediction API
- one example request to the API
- a README that explains setup, how to run the project, and the answers to the project questions

## Stretch Goals

- test your data pipeline, model, or API
- use `GridSearchCV` or `optuna` for hyperparameter tuning
- compare the tuned model against the baseline and explain whether the extra complexity was worth it

## Questions To Answer In Your README

1. What is the RMSE of your model?
2. What would you do differently if you had more time?

## Submission

Upload your finished project to your own GitHub repository and submit the link. Use pull requests to track your work, even if you are working alone.
