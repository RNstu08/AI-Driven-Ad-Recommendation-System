import os
import pathlib

def create_project_structure(base_path):
    """
    Creates the essential folder structure and files for the Ad Recommendation System project.
    """
    #project_name = "personalized-ad-recommendation"
    project_name = ""
    project_path = os.path.join(base_path, project_name)

    # Define the folder structure and essential files
    structure = {
        "data": ["raw", "processed"],
        "notebooks": ["eda.ipynb"],
        "src": ["__init__.py", "data_preprocessing.py", "model_training.py", "inference.py", "evaluation.py", "utils.py", "data_loading.py"],
        "app": ["main.py", "predict.py"],
        "docker": ["Dockerfile", "prometheus.yml"],
        "tests": [],
    }

    # Root files
    root_files = [".gitignore", "requirements.txt", "README.md", "docker-compose.yml", "LICENSE"]

    # Create project directory
    os.makedirs(project_path, exist_ok=True)

    # Create subdirectories and their files
    for folder, files in structure.items():
        folder_path = os.path.join(project_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        for file in files:
            file_path = os.path.join(folder_path, file)
            pathlib.Path(file_path).touch()  # Create empty file

    # Create root files
    for file in root_files:
        file_path = os.path.join(project_path, file)
        pathlib.Path(file_path).touch()  # Create empty file

    print(f"Project structure created successfully at: {project_path}")

if __name__ == "__main__":
    # Use the current working directory as the base path
    base_path = os.getcwd()
    create_project_structure(base_path)