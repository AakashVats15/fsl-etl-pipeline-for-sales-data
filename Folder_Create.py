import os

base_path = r"E:\Personal\GitHub\Python Code Repo\fsl-etl-pipeline-for-sales-data"

folders = [
    "data/raw",
    "data/processed",
    "src",
    "sql",
    "docs",
    "tests"
]

files = [
    "src/extract.py",
    "src/transform.py",
    "src/load.py",
    "sql/create_tables.sql",
    "sql/analytics_queries.sql",
    "tests/test_transform.py",
    "README.md"
]

# Create folders
for folder in folders:
    path = os.path.join(base_path, folder)
    os.makedirs(path, exist_ok=True)

# Create empty files
for file in files:
    path = os.path.join(base_path, file)
    with open(path, "w") as f:
        pass

print("Project structure created successfully!")
