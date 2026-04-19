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


## Tester le projet

### Terminal (python main.py)
### Exemple de commande :

>> Donne-moi les infos du client C001
>> Liste tous les clients
>> Quel est le cours de AAPL ?
>> Calcule mon portefeuille : AAPL:10|GOOGL:5|MSFT:3
>> Quelles sont les dernières actualités d'Apple ?
>> Calcule la moyenne de ces valeurs : 12, 45, 7, 89, 34, 56
>> Donne-moi les infos du client C001
>> Quel produit lui recommandes-tu ?
>> Calcule le prix TTC et dis-moi si elle peut se le permettre

### Ouvrir un deuxieme terminal

### API REST (uvicorn api:app --reload)
```bash
curl http://localhost:8000/

curl -X POST http://localhost:8000/api/agent/query \
  -H "Content-Type: application/json" \
  -d '{"question": "Donne-moi les infos du client C001"}'
```

### Interface Streamlit (streamlit run app.py)
Ouvre http://localhost:8501 dans ton navigateur et tape une question dans le champ en bas de page.
