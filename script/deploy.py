import streamlit as st
import numpy as np
import joblib  # Pour charger ton modèle
import json

# Charger les modèles (à remplacer par tes vrais fichiers .pkl)
svm_model = joblib.load("svm_model.pkl")
knn_model = joblib.load("knn_model.pkl")

# Seuils de performance des modèles
THRESHOLD_SCORE = json.loads('{"svm": 0.7857142857142857, "knn": 0.9047619047619048}')

# Titre et description du projet
st.title("🛳️ Détection Sonar : Mine ou Rocher ?")
st.write("Ce projet utilise des signaux sonar pour classer un objet sous-marin en Mine (M) ou Rocher (R).")

# Affichage des métriques
col1, col2 = st.columns(2)
with col1:
    st.metric(label="🔹 Score SVM", value=THRESHOLD_SCORE["svm"])
with col2:
    st.metric(label="🔹 Score KNN", value=THRESHOLD_SCORE["knn"])

# Formulaire pour entrer les 60 fréquences
st.subheader("📡 Entrez les valeurs des fréquences")
input_data = []
cols = st.columns(6)
for i in range(60):
    with cols[i % 6]:  # Organiser en 6 colonnes
        val = st.number_input(f"Freq_{i+1}", min_value=0.0, max_value=1.0, step=0.01, value=simulated_data[i])
        input_data.append(val)

# Prédiction
if st.button("🔍 Prédire"):
    input_array = np.array(input_data).reshape(1, -1)
    
    # Prédictions des modèles
    svm_pred = svm_model.predict(input_array)[0]
    knn_pred = knn_model.predict(input_array)[0]
    
    # Résultats
    st.subheader("🛠️ Résultat de la classification")
    st.write(f"🔹 **SVM** prédit : `{svm_pred}`")
    st.write(f"🔹 **KNN** prédit : `{knn_pred}`")
    
    # Affichage du résultat final
    final_prediction = "Mine (M)" if (svm_pred == 'M' or knn_pred == 'M') else "Rocher (R)"
    st.success(f"✅ Objet classé comme : **{final_prediction}**")
    
# Bouton pour remplir automatiquement les champs
if st.button("🎲 Remplir automatiquement les champs (simulation)"):
    # Générer des valeurs aléatoires pour les 60 fréquences
    simulated_data = np.random.uniform(0.0, 1.0, size=60).tolist()
else:
    simulated_data = [0.0] * 60  # Valeurs par défaut