import os
from pathlib import Path

# Name of the root project directory where source code will reside
project_name = "src"

# List of all files & directories to be created in the project structure
list_of_files = [

    # Source directory initializations
    f"{project_name}/__init__.py",

    # Components – each file will hold different stages of ML pipeline
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",

    # Configuration related modules
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/mongo_db_connection.py",
    f"{project_name}/configuration/aws_connection.py",

    # Cloud storage utilities
    f"{project_name}/cloud_storage/__init__.py",
    f"{project_name}/cloud_storage/aws_storage.py",

    # Data access layer
    f"{project_name}/data_access/__init__.py",
    f"{project_name}/data_access/proj1_data.py",

    # Constant definitions
    f"{project_name}/constants/__init__.py",

    # Entities for configuration, artifacts, and estimator classes
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/entity/estimator.py",
    f"{project_name}/entity/s3_estimator.py",

    # Exception and logger modules
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",

    # Pipeline modules
    f"{project_name}/pipline/__init__.py",
    f"{project_name}/pipline/training_pipeline.py",
    f"{project_name}/pipline/prediction_pipeline.py",

    # Utility functions
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",

    # Application and setup files
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "pyproject.toml",

    # Configuration YAMLs
    "config/model.yaml",
    "config/schema.yaml",
]

# Creating files & directories
for filepath in list_of_files:
    filepath = Path(filepath)  # Convert to Path object for easy path handling
    filedir, filename = os.path.split(filepath)

    # Create directory if it doesn't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    # Create the file if it does not exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # Create an empty file
    else:
        print(f"file is already present at: {filepath}")
