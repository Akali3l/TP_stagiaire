# Agent Financier — Projet TP LangChain

## Prérequis
- Python 3.11
- Une clé API OpenAI → https://platform.openai.com
- Une clé API Tavily → https://tavily.com

## Installation

### 1. Cloner le projet
```bash
git clone <ton-lien-github>
cd projet_agent
```

### 2. Créer et activer l'environnement virtuel
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Configurer les clés API
```bash
cp .env.example .env
```
Ouvre le fichier `.env` et remplis tes clés :

### 5. Initialiser la base de données
```bash
python init_db.py
```

## Lancer le projet

### Terminal
```bash
python main.py
```

### Interface web (Streamlit)
```bash
streamlit run app.py
```

### API REST (FastAPI)
```bash
uvicorn api:app --reload
```
