import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import trustworthiness


def load_original_data(path="data/city_lifestyle_dataset.csv"):
    df = pd.read_csv(path)
    X = df.drop(columns=["city_name", "country"])
    X_scaled = StandardScaler().fit_transform(X)
    return X_scaled


def load_2d_embedding(path):
    emb = pd.read_csv(path)

    # Cas attendu: colonnes nommées dim1/dim2
    if "dim1" in emb.columns and "dim2" in emb.columns:
        return emb[["dim1", "dim2"]].values

    # Fallback: prendre les 2 premières colonnes
    return emb.iloc[:, :2].values


def main():
    X_original = load_original_data()

    files = {
        "PCA": "outputs/pca_emb_2d.csv",
        "T-SNE": "outputs/tsne_emb_2d.csv",
        "UMAP": "outputs/umap_emb_2d.csv",
    }

    print("=== Trustworthiness Comparison ===")
    scores = {}

    for method, file_path in files.items():
        X_reduced = load_2d_embedding(file_path)
        score = trustworthiness(X_original, X_reduced, n_neighbors=10)
        scores[method] = score
        print(f"{method:6s} : {score:.4f}")

    best_method = max(scores, key=scores.get)
    print("\nBest method:", best_method, f"({scores[best_method]:.4f})")


if __name__ == "__main__":
    main()