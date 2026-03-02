# Projet Final - Réduction de dimension et comparaison

## Équipe
- Sirine: méthode PCA
- Chaimaa: méthode t-SNE
- Sabrina: méthode UMAP

## Objectif
Ce projet simule un travail collaboratif de data science avec Git/GitHub.
Chaque membre implémente une méthode de réduction de dimension dans une branche dédiée.
Après fusion dans `main`, un script compare les méthodes avec la métrique **trustworthiness**.
Le projet est exécutable dans un conteneur Docker.

## Structure du projet
```text
data/
  city_lifestyle_dataset.csv
notebooks/
  pca.ipynb
  tsne.ipynb
  umap.ipynb
outputs/
  pca_emb_2d.csv
  tsne_emb_2d.csv
  umap_emb_2d.csv
evaluate.py
requirements.txt
Dockerfile
README.md
```

## Méthodes implémentées
Chaque notebook contient:
1. chargement et préparation des données,
2. projection en 2D,
3. visualisation,
4. courte observation,
5. export des coordonnées 2D dans `outputs/`.

## Comparaison des méthodes (Trustworthiness)
La **trustworthiness** mesure la conservation des voisinages locaux entre l'espace original et l'espace réduit.
- score proche de `1`: bonne préservation locale,
- score plus faible: plus de distorsion locale.

Le script `evaluate.py`:
1. charge les données originales depuis `data/city_lifestyle_dataset.csv`,
2. charge les embeddings 2D exportés (PCA, t-SNE, UMAP),
3. calcule `trustworthiness` pour chaque méthode,
4. affiche les scores et la meilleure méthode.

## Installation locale
```bash
python3 -m pip install -r requirements.txt
```

## Exécution de la comparaison
```bash
python3 evaluate.py
```

## Résultats de l'évaluation
Résultats obtenus avec `python3 evaluate.py`:

```text
=== Trustworthiness Comparison ===
PCA    : 0.9363
T-SNE  : 0.9714
UMAP   : 0.9665

Best method: T-SNE (0.9714)
```

Interprétation rapide:
- Les trois méthodes conservent bien la structure locale (scores proches de 1).
- **T-SNE** obtient le meilleur score de trustworthiness sur ce dataset.
- **UMAP** est très proche de T-SNE et meilleur que PCA sur cette métrique.

## Git Workflow (résumé)
- Une branche par méthode: `method/PCA`, `method/T-SNE`, `method/UMAP`
- Au moins 2 commits par membre
- Une Pull Request par branche vers `main`
- Fusion finale des PR dans `main`

## Docker
### Dockerfile (exemple minimal)
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "evaluate.py"]
```

### Build et run
```bash
docker build -t projet-final:latest .
docker run --rm projet-final:latest
```

### Option volume (bonus)
```bash
docker run --rm -v $(pwd):/app projet-final:latest
```

## Résultats attendus
- Trois notebooks (PCA, t-SNE, UMAP)
- Trois exports 2D dans `outputs/`
- Script de comparaison fonctionnel avec trustworthiness
- Exécution reproductible avec Docker

## Rendu
- Lien GitHub du projet
- Lien DockerHub (si disponible)
- Sinon: instructions de build/run Docker dans ce README

### Liens du projet
- GitHub: https://github.com/chaimaa-arsalane/Projet_finale.git
- DockerHub: https://hub.docker.com/r/sirinamarwa/projet-final
