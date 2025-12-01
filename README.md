# Wine Quality Classification

This project uses the Wine dataset and a Logistic Regression model to classify wine samples.

## How to Run

### Local Setup (Virtual Environment)

It is recommended to use a virtual environment to avoid dependency conflicts.

1.  **Create a virtual environment:**
    ```bash
    python3 -m venv venv
    ```

2.  **Activate the virtual environment:**
    ```bash
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r src/requirements.txt
    ```

4.  **Run the script:**
    ```bash
    python src/main.py
    ```

### Docker Setup

Run the project using Docker.

1.  **Build the Docker image:**
    ```bash
    docker build -t mlops-lab6 .
    ```

2.  **Run the Docker container:**
    ```bash
    docker run mlops-lab6
    ```

The script will train the model and save it as `wine_model.pkl`.