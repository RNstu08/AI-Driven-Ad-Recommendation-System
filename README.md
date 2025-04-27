## Getting Started

Follow these steps to set up and run the project on your local machine.

### Prerequisites

* **Python 3.10+**
* **pip** (Python package installer)
* **Docker** and **Docker Compose** (for containerization)
* **(Optional) VS Code with WSL2 (Ubuntu)** for a recommended development environment.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/RNstu08/AI-Driven-Ad-Recommendation-System.git](https://github.com/RNstu08/AI-Driven-Ad-Recommendation-System.git)
    cd AI-Driven-Ad-Recommendation-System
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    # venv\Scripts\activate   # On Windows
    ```

3.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Download the Retail Rocket dataset:**
    * Navigate to the `data/retailrocket` directory.
    * Download the necessary CSV files (e.g., `events.csv`, `item_properties_part1.csv`, `category_tree.csv`). You might need to create this directory structure if it doesn't exist. The project seems to be set up to use this specific dataset.

### Running the Application

You have two main ways to run the application: locally or using Docker.

#### Running Locally (for development and testing)

1.  **Train the recommendation model:**
    ```bash
    python src/model_training.py
    # This will train the model and save it as model.pkl
    ```

2.  **Run the FastAPI API server:**
    ```bash
    uvicorn src.api_server:app --reload --host 0.0.0.0 --port 8000
    ```
    Or if you want to run the API defined in the `app` directory:
    ```bash
    uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
    ```

3.  **Access the API:**
    * Open your browser and go to `http://localhost:8000/docs` to see the interactive Swagger UI.

#### Running with Docker

1.  **Build and run the Docker containers:**
    ```bash
    docker-compose up --build -d
    ```
    This command will build the Docker image defined in the `docker/Dockerfile` and start the application container in the background.

2.  **Access the API:**
    * The API will be accessible at `http://localhost:8000/recommend/{user_id}`.

### Monitoring (using Docker Compose)

This project includes basic monitoring using Prometheus and Grafana, configured via `docker-compose.yml`.

1.  **Ensure Docker Compose is running:** Follow the steps in the "Running with Docker" section.

2.  **Access Prometheus:** Open your browser and go to `http://localhost:9090`. You can query metrics related to your FastAPI application here.

3.  **Access Grafana:** Open your browser and go to `http://localhost:3000`.
    * Default credentials are `admin` / `admin`. You will likely be prompted to change the password upon the first login.
    * You might need to configure a Prometheus data source in Grafana, pointing to `http://prometheus:9090` (if running within Docker Compose network) or `http://localhost:9090` (if accessing from your host).
    * The `grafana_dashboard.json` file (if present) can be imported into Grafana to provide pre-configured dashboards for your application metrics.

## Project Details

This project implements a personalized ad recommendation system using a collaborative filtering approach.

* **Data Handling:** The `data` directory contains the raw Retail Rocket dataset. Scripts in `src/data_loading.py` and `src/data_preprocessing.py` handle loading and preparing this data.
* **Model Training:** The `src/model_training.py` script trains a recommendation model (likely using techniques like cosine similarity on a user-item interaction matrix). The trained model is saved as `model.pkl`.
* **Inference:** The `src/inference.py` script loads the trained model and provides functions to generate recommendations for users.
* **API Serving:** The `src/api_server.py` (or `app/main.py`) uses FastAPI to expose the recommendation functionality as a RESTful API.
* **Monitoring:** The `docker-compose.yml` sets up Prometheus to scrape metrics from the FastAPI application (you might need to instrument your FastAPI application to expose these metrics) and Grafana for visualization. The `docker/prometheus.yml` configures Prometheus to target your API.

## Potential Improvements and Future Work

* Implement more advanced recommendation algorithms (e.g., Matrix Factorization, Neural Collaborative Filtering).
* Enhance data preprocessing and feature engineering.
* Implement user and item cold-start strategies.
* Improve monitoring with more detailed metrics and custom Grafana dashboards.
* Set up automated testing and CI/CD pipelines.
* Consider deploying the application to a cloud platform.

