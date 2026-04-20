# Model Deployment Project

Build, track, and serve a trip-duration model on the January 2025 NYC Yellow Taxi dataset.

This repository is a local-first template for an MLE deployment project. The goal is to train a regression model, track experiments with MLflow, expose predictions through an API, and verify the full workflow on your own machine.

## Project Hub

- [README.md](./README.md): repository overview, setup, and workflow
- [project-description.md](./project-description.md): assignment brief, deliverables, and stretch goals
- [requirements.txt](./requirements.txt): pinned Python dependencies for the local environment
- [.github/pull_request_template.md](./.github/pull_request_template.md): PR checklist for tracking project progress

## Learning Path

1. Read the assignment brief in [project-description.md](./project-description.md).
2. Download and inspect the January 2025 Yellow Taxi dataset.
3. Train a baseline `RandomForestRegressor` and track runs locally with MLflow.
4. Refactor preprocessing and training logic into reusable Python modules.
5. Build a local prediction API with FastAPI.
6. Send a test request to the API and document the outcome in your README or PR.

## Suggested Repository Layout

This repo starts lightweight on purpose. As you implement the project, a practical learner-friendly structure is:

- `notebooks/`: EDA, feature checks, and experiment notes
- `src/`: reusable data preparation, feature engineering, and training code
- `app/`: FastAPI application and prediction schema
- `tests/`: data, model, and API tests
- `artifacts/`: saved model files or exports that should not be committed if they are large

## Local Workflow

```mermaid
flowchart LR
    A["Download Yellow Taxi Data"] --> B["Explore And Clean Features"]
    B --> C["Train Random Forest Regressor"]
    C --> D["Track Runs In MLflow"]
    D --> E["Package Preprocessing And Model"]
    E --> F["Serve Predictions With FastAPI"]
    F --> G["Send Local Test Request"]
```

## Local Data Services

- `MLflow`: run experiment tracking and inspect runs locally, for example at `http://127.0.0.1:5000`.
- `FastAPI`: serve predictions locally, for example at `http://127.0.0.1:8000`.
- `Docker` is optional if you want a containerized local workflow.

## Mermaid Diagrams

GitHub renders Mermaid diagrams in Markdown automatically. For local preview in VS Code, install the `Markdown Preview Mermaid Support` extension:

- [Install in VS Code](vscode:extension/bierner.markdown-mermaid)
- [View on Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid)

## Environment

Use `Python 3.11.3` for this project. If you manage Python with `pyenv`, pin that version before creating the virtual environment.

## Setup

Please set up a new virtual environment. You can use the following commands:

### `macOS` / Linux

```bash
pyenv local 3.11.3
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### `Windows`

For `PowerShell`:

```powershell
pyenv local 3.11.3
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

For `Git-Bash` CLI:

```bash
pyenv local 3.11.3
python -m venv .venv
source .venv/Scripts/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Working Locally

Once you have implemented the project code, a typical local workflow looks like this:

1. Train the model and log runs to the local `mlruns/` directory with MLflow.
2. Start the tracking UI with `mlflow ui --backend-store-uri ./mlruns --port 5000`.
3. Run the API locally with `uvicorn app.main:app --reload --port 8000`.
4. Send a request such as `curl -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json" -d @sample-request.json`.

## Learning Objectives

- Build an end-to-end regression workflow for real-world taxi-trip data.
- Separate exploration, preprocessing, training, and serving concerns into maintainable code.
- Track experiments locally with MLflow and compare model runs.
- Serve model predictions through a local API.
- Communicate results clearly through pull requests and README documentation.

## Submission Notes

Use this repository as a template for your own project repo. Open pull requests even if you are working solo so you can track progress and leave yourself a clear implementation history.

Answer these questions in your project README:

1. What is the RMSE of your final model?
2. What would you do differently if you had more time?
