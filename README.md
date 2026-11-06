# First Python Application — FastAPI

## Description

This project is a simple Python web application built with **FastAPI**.

The application exposes a `GET /` endpoint that returns the following JSON response:

```json
{
  "message": "it works !"
}
```

## Installation

Install the required dependencies:

```bash
pip install fastapi uvicorn
```

## Running the Application

Start the application with the following command:

```bash
uvicorn main:app --reload
```

The application will be available at:

http://127.0.0.1:8000

## How to Test the Application

### 1. Test the root endpoint

Open the following URL in your browser:

http://127.0.0.1:8000/

Expected response:

```json
{
  "message": "it works !"
}
```

### 2. Test using FastAPI Swagger UI

Open:

http://127.0.0.1:8000/docs

Click on `GET /`, then click **Try it out** and **Execute** to test the endpoint.

## Project Structure

```text
.
├── main.py
└── README.md
```
# TP3 - Intégration Continue

## Travail réalisé
- **Nouvelle fonctionnalité** : Ajout de l'endpoint `/subtract` pour effectuer des soustractions.
- **Tests Unitaires** : Création du fichier `test_main.py` contenant 8 tests avec `pytest`.
- **Couverture du code (Coverage)** : Plus de 90% du code est couvert par les tests.
- **Qualité du code** : Le code a été analysé et amélioré avec `Pylint`.
- **CI/CD** : Mise en place d'un pipeline GitHub Actions (`.github/workflows/ci.yml`) qui :
  - Lance Pylint.
  - Lance les tests pytest avec le rapport de couverture.
  - Génère un rapport JUnit XML.
  - Sauvegarde le rapport XML en tant qu'artefact téléchargeable.