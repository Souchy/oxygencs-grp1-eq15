
# Laboratoire 2

## Doc

Le rapport de ce laboratoire se trouve à doc/rapport.md

## Installation

1. Créer un environement python en utilisant les dépendances ci-dessous. VSCode vous demande d'en créer un la première fois que vous roulez `python main.py`.

   Packages utilisés:  
   > pip install python-dotenv  
   > pip install SQLAlchemy  
   > pip install pydantic
   > pip install pydantic_core
   > pip install psychopg2
   > pip install requests
   > pip install signalrcore

2. Créer un fichier .env avec toutes les variables d'environnement nécessaires:
   - REPOSITORY_ACCESS_TOKEN
   - PROJECT_ACCESS_TOKEN
   - METRICS_REPOSITORY
   - OXYGENCS_REPOSITORY
   - DB_HOST
   - DB_NAME
   - DB_USER
   - DB_PASSWORD
   - HOST_SENSORS
   - TOKEN_HVAC
   - T_MAX
   - T_MIN

## Run

> python main.py
