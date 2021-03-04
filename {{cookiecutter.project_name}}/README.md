# {{cookiecutter.project_name}}

## Description
{{cookiecutter.description}}

### Optional (but recommended)
Create a conda environment to run this project in isolation.
```[bash]
cd {{cookiecutter.project_name}}/
conda env create -f environment.yml
conda activate {{cookiecutter.project_name}} 
```

### Installation
```[bash]
cd {{cookiecutter.project_name}}/
pre-commit install
pip install --editable .
```