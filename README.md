# PrinceBreaker

## Introduction
PrinceBreaker est un outil conçu pour faciliter certaines tâches en utilisant des APIs comme SerpApi et Proxycn. Suivez les instructions ci-dessous pour configurer et démarrer avec PrinceBreaker.

## Configuration initiale

### 1. Activer votre environnement virtuel
Avant de commencer, assurez-vous d'activer votre environnement virtuel.
```bash
pip install virtualenv
cd venv/Scripts
./activate.bat
```

### 2. Installer les packages
```bash
pip install -r requirements.txt
```


### 3.  Renseigner vos clés API
Dans le fichier .env , renseignez les clés API openai, serpapi, proxycurl
```
OPENAI_API_KEY=CLE 
PROXYCRUL_API_KEY=CLE
SERPAPI_API_KEY=CLE
```

## Utilisation

### Lancer une inférence
Pour exécuter un script d'inférence avec PrinceBreaker, utilisez la commande suivante :
```bash
python princebreaker.py
```


### Lancer  l'api
Si vous souhaitez démarrer l'API, utilisez la commande suivante :

```bash
uvicorn app:app --reload
```
Cette commande démarre un serveur local sur le port 8000 par défaut, et vous pourrez accéder à l'API via http://localhost:8000




Par **Prince Gédéon GUEDJE** ([github.com/princeGedeon](https://github.com/princeGedeon))


