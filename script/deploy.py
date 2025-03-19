import pickle
import json

# Charger les modèles
with open('../model/knn_model.pkl', 'rb') as f:
    knn_model = pickle.load(f)

with open('../model/svm_model.pkl', 'rb') as f:
    svm_model = pickle.load(f)

# Charger les scores
with open('../model/scores.json', 'r') as f:
    scores = json.load(f)

def classify(model_name, input_data):
    """
    Classifie les données d'entrée en utilisant le modèle spécifié.

    Parameters:
    model_name (str): Le nom du modèle à utiliser ('KNN' ou 'SVM').
    input_data (array-like): Les données d'entrée à classifier.

    Returns:
    array: Les prédictions du modèle.
    """
    if model_name == 'KNN':
        model = knn_model
    elif model_name == 'SVM':
        model = svm_model
    else:
        raise ValueError("Modèle non supporté: choisissez 'KNN' ou 'SVM'")

    predictions = model.predict(input_data)
    return predictions

# Exemple d'utilisation
if __name__ == "__main__":
    # Exemple de données d'entrée
    example_data = [[5.1, 3.5, 1.4, 0.2]]  # Remplacez par vos propres données

    # Choisissez le modèle
    model_name = 'KNN'  # ou 'SVM'

    # Obtenez les prédictions
    predictions = classify(model_name, example_data)
    print(f"Prédictions pour le modèle {model_name}: {predictions}")