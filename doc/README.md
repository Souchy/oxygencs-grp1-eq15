
# Laboratoire 2

## Doc

Le rapport de ce laboratoire se trouve à doc/rapport.md
Le README.md du root contient plus d'informations.

## Requis

- Python 3.8+
- pipenv

## Commencer

Installer les dépendances du projet :

```bash
pipenv install
pip install --user pre-commit
pip install --user pylint
```

Installer pre-commit git hook :

```bash
pre-commit install
```

Créer un fichier .env avec toutes les variables d'environnement nécessaires:

- HOST_SENSORS
- TOKEN_HVAC
- T_MAX
- T_MIN
- DB_HOST
- DB_NAME
- DB_USER
- DB_PASSWORD

## Rouler le programme

```bash
pipenv run start
```

## Image docker

Dépot d'images: <https://hub.docker.com/repository/docker/souchy/log680-grp1-eq15/general>

```bash
docker build -t oxygencs .
docker run --env-file .env oxygencs
```
