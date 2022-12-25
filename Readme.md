# Hillel rest API application

# Setup

## Mandatory steps

1. Install Python3.X
2. Install Pipenv
3. Black
4. Flake8
5. Isort

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

```

To get started right away with sensible defaults:

```bash
black src
```

You can run _Black_ as a package if running it as a script doesn't work:

```bash
python -m black src
```

####  Flake8

Setup
```bash
# Install flake8
pip install flake8
```

To start using Flake8

```bash
flake8 path/to/code/
```

#####  isort

Setup
```bash
# Install isort
pip install isort

```

To start using Flake8

```bash
isort --atomic .
```

