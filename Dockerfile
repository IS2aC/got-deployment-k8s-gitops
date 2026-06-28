# Image de base légère Python
FROM python:3.11-slim

# Répertoire de travail dans le conteneur
WORKDIR /app

# Copier les dépendances en premier (optimise le cache Docker)
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code
COPY . .

# Port exposé par Flask
EXPOSE 5000

# Lancer l'app (gunicorn pour la prod, pas le serveur de dev Flask)
CMD ["python", "app.py"]