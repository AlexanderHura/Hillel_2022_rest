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

###  Black

Setup
```bash
# Install black
pip install black
# pipenv install --dev
```

To get started right away with sensible defaults:

```bash
black src
```

You can run _Black_ as a package if running it as a script doesn't work:

```bash
python -m black src
```


