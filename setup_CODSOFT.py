import os

base_dir = "CodSoft"
projects = [f"Project{i}" for i in range(1, 6)]

for i, project in enumerate(projects, start=1):
    project_path = os.path.join(base_dir, project)
    os.makedirs(project_path, exist_ok=True)

    # Create .ipynb file
    with open(os.path.join(project_path, f"{project.lower()}.ipynb"), "w") as f:
        f.write("")  # Empty notebook

    # Create README.md
    with open(os.path.join(project_path, "README.md"), "w") as f:
        f.write(f"# {project}\n\nThis is the README for {project}.")

    # Create dataset file
    with open(os.path.join(project_path, f"dataset{i}.csv"), "w") as f:
        f.write("feature1,feature2,feature3\n")  # Sample CSV header