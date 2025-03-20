Voici une documentation `README.md` adaptée à votre projet, qui traite de la classification des objets sous-marins (mines et rochers) à partir des données sonar. Cette documentation inclut les étapes de réalisation, une explication du dataset, et le lien vers l'application déployée.

---

# CC_GROUPE_1

## 🚀 Automatiser l’entraînement, l’évaluation et le déploiement d’un modèle de classification sonar avec GitHub Actions !

Ce projet vise à automatiser l'entraînement, l'évaluation et le déploiement d'un modèle de classification pour distinguer les **mines sous-marines** des **rochers** à partir de données sonar. Le modèle est entraîné sur un dataset contenant 60 caractéristiques de signaux sonar réfléchis. L'application est déployée sur **Hugging Face Spaces** pour permettre une utilisation interactive.

---

## 📂 Structure du projet

```
CC_GROUPE_1/
├── .github/
│   └── workflows/
│       └── train_eval.yml          # Configuration GitHub Actions
├── data/
│   └── sonarall.csv               # Dataset des signaux sonar
├── Scripts/
│   ├── train_eval.py              # Script pour le préprocessing, l'entraînement et l'évaluation
│   └── send_email.py              # Script pour envoyer des emails avec les résultats
├── app.py                         # Application Streamlit pour la prédiction
├── requirements.txt               # Dépendances Python
├── README.md                      # Documentation du projet
└── output/                        # Dossier pour les artefacts (modèle, rapport, etc.)
```

---

## 🎯 Objectif du projet

L'objectif de ce projet est de créer un pipeline automatisé pour :
1. **Préprocesser** les données sonar.
2. **Entraîner** un modèle de classification binaire (mine vs rocher).
3. **Évaluer** les performances du modèle.
4. **Déployer** l'application sur Hugging Face Spaces pour permettre des prédictions interactives.

---

## 📊 Dataset : Sonar Data

Le dataset `sonarall.csv` contient des données sonar utilisées pour la classification des objets sous-marins. Il est composé de 60 caractéristiques et d'une variable cible binaire.

### Explication des colonnes

1. **`Freq_1` à `Freq_60`**  
   - Ces colonnes représentent 60 caractéristiques extraites du signal sonar.  
   - Chaque colonne correspond à une intensité de signal à une fréquence spécifique.  
   - Les valeurs sont des mesures d’amplitude du signal réfléchi pour différentes fréquences.  

2. **`Label`**  
   - C'est la variable cible (ce que le modèle doit prédire).  
   - Il y a deux classes dans ce dataset :  
     - **"R"** : Représente "Rock" (rocher).  
     - **"M"** : Représente "Mine" (mine sous-marine).  

---

## 🛠️ Étapes de réalisation

### 1. Préprocessing des données
- Normalisation des caractéristiques (`Freq_1` à `Freq_60`) pour les mettre à l'échelle.
- Encodage de la variable cible (`Label`) en valeurs numériques :
  - "R" → 0
  - "M" → 1
- Division des données en ensembles d'entraînement et de test.

### 2. Entraînement du modèle
- Utilisation d'un modèle de machine learning (par exemple, Random Forest, SVM, ou un réseau de neurones).
- Compilation avec une fonction de perte adaptée à la classification binaire (`binary_crossentropy` pour un réseau de neurones).

### 3. Évaluation du modèle
- Calcul de la précision, du rappel, et de la F1-score sur l'ensemble de test.
- Génération d'une matrice de confusion et d'un rapport de classification.

### 4. Déploiement de l'application
- Création d'une application Streamlit pour permettre aux utilisateurs de saisir des valeurs de caractéristiques et d'obtenir une prédiction (mine ou rocher).
- Déploiement de l'application sur Hugging Face Spaces.

### 5. Automatisation avec GitHub Actions
- Configuration d'un pipeline CI/CD pour :
  - Entraîner et évaluer le modèle à chaque push sur la branche `main`.
  - Archiver et téléverser le modèle et les résultats.
  - Envoyer un email avec les résultats et le lien de l'application.

---

## 🖥️ Application Streamlit

L'application permet aux utilisateurs de saisir les 60 caractéristiques sonar et d'obtenir une prédiction : **Mine (M)** ou **Rocher (R)**.

👉 **Lien de l'application** : [https://huggingface.co/spaces/armelmbia/CC_git_hub_group_1](https://huggingface.co/spaces/armelmbia/CC_git_hub_group_1)

---

## 🛠️ Comment exécuter le projet localement

### Prérequis
- Python 3.9
- Bibliothèques listées dans `requirements.txt`

### Étapes
1. Clonez le dépôt :
   ```bash
   git clone https://github.com/votre_utilisateur/CC_GROUPE_1.git
   cd CC_GROUPE_1
   ```

2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

3. Exécutez le script d'entraînement et d'évaluation :
   ```bash
   python Scripts/train_eval.py
   ```

4. Lancez l'application Streamlit :
   ```bash
   streamlit run app.py
   ```

---

## 🤖 Automatisation avec GitHub Actions

Le fichier `.github/workflows/train_eval.yml` configure un pipeline CI/CD pour :
- Entraîner et évaluer le modèle à chaque push sur la branche `main`.
- Archiver le modèle et les résultats dans un fichier `output.zip`.
- Envoyer un email avec les résultats et le lien de l'application.

---

## 📧 Notification par email

À la fin du pipeline, un email est envoyé avec :
- Un résumé des étapes accomplies.
- Le lien de l'application déployée sur Hugging Face.
- Le modèle et le rapport d'évaluation en pièce jointe.

Exemple de contenu de l'email :
```
Bonjour l'équipe ! 👋

Je suis ravi de vous informer que GitHub Actions a bien effectué toutes les étapes du pipeline avec succès ! 🎉

Voici ce qui a été accompli :
- 📂 Préprocessing des données terminé.
- 🤖 Entraînement du modèle effectué.
- 📊 Évaluation du modèle réalisée.
- 📦 Archivage du modèle et des résultats.

Vous pouvez accéder à l'application directement ici : 🌐 Lien de l'application.

Le modèle et le rapport d'évaluation sont joints à cet email. 📎

Bonne journée et à bientôt ! 😊

Cordialement,
Votre assistant GitHub Actions 🤖
```

---

## 📄 Rapport d'évaluation

Le rapport d'évaluation inclut :
- La précision, le rappel, et la F1-score sur l'ensemble de test.
- Une matrice de confusion.
- Un rapport de classification détaillé.

---

## 🔗 Liens utiles

- **Dépôt GitHub** : [https://github.com/votre_utilisateur/CC_GROUPE_1](https://github.com/votre_utilisateur/CC_GROUPE_1)
- **Application Hugging Face** : [https://huggingface.co/spaces/armelmbia/CC_git_hub_group_1](https://huggingface.co/spaces/armelmbia/CC_git_hub_group_1)

---

## 👥 Auteurs
- Bea Elie
- Mbia Armel

---

## 📝 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

Fait par l'équipe CC_GROUPE_1 ! 🚀
