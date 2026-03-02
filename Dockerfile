FROM python:3.12-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier d'abord requirements.txt (pour profiter du cache Docker)
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le reste du projet
COPY . .

# Commande par défaut : exécuter le script de comparaison
CMD ["python", "evaluate.py"]