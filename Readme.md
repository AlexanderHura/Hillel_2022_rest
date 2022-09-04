# Hillel rest API application

# Setup

## Mandatory steps

1. Install Python3.X
2. Install Pipenv

# Setup project
Setup environment
```bash
# Create virtual environment
pipenv sync
# pipenv install --dev

pipenv shell
```

Run django server
```bash
# Run migrations only on a project setup
python src/manage.py migrate

# Run server
python src/manage.py runserver
```
