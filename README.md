# Application de Classification de CV (Resume Screening App)

Une application web intelligente basée sur le machine learning qui classe automatiquement les CV en différentes catégories professionnelles. L'application utilise des modèles pré-entraînés pour analyser le contenu d'un CV et identifier la catégorie professionnelle la plus appropriée.

## Fonctionnalités

- **Classification automatique** : Analyse et classe les CV en 24 catégories professionnelles différentes
- **Interface intuitive** : Interface web simple et conviviale construite avec Streamlit
- **Support PDF** : Extraction et analyse automatique du texte depuis les fichiers PDF
- **Traitement du texte** : Nettoyage et préparation automatique du texte pour une meilleure précision
- **Prédiction en temps réel** : Résultats instantanés après l'upload du CV

## Catégories supportées

L'application peut classifier les CV dans les catégories suivantes :

- Data Science
- HR (Ressources Humaines)
- Advocate (Avocat)
- Arts
- Web Designing
- Mechanical Engineer
- Sales (Ventes)
- Health and fitness
- Civil Engineer
- Java Developer
- Business Analyst
- SAP Developer
- Automation Testing
- Electrical Engineering
- Operations Manager
- Python Developer
- DevOps Engineer
- Network Security Engineer
- PMO (Project Management Office)
- Database
- Hadoop
- ETL Developer
- DotNet Developer
- Blockchain
- Testing

## Technologies utilisées

- **Python** : Langage de programmation principal
- **Streamlit** : Framework pour l'interface web
- **scikit-learn** : Bibliothèque de machine learning
- **NLTK** : Traitement du langage naturel
- **PyPDF2** : Extraction de texte depuis les fichiers PDF
- **joblib** : Sauvegarde et chargement des modèles
- **pandas** : Manipulation des données
- **numpy** : Calculs numériques

## Installation

### Prérequis

- Python 3.7 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. **Cloner le dépôt** (ou télécharger le projet)
   ```bash
   git clone https://github.com/yann-fk-21/resume-screening-app.git
   cd resume-screening-app
   ```

2. **Créer un environnement virtuel** (recommandé)
   ```bash
   python -m venv venv
   ```

3. **Activer l'environnement virtuel**
   
   Sur Windows :
   ```bash
   venv\Scripts\activate
   ```
   
   Sur Linux/Mac :
   ```bash
   source venv/bin/activate
   ```

4. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

5. **Télécharger les données NLTK** (automatique au premier lancement)
   - Les données nécessaires (stopwords, punkt) seront téléchargées automatiquement lors du premier lancement de l'application

## Utilisation

1. **Lancer l'application**
   ```bash
   streamlit run app.py
   ```

2. **Accéder à l'interface**
   - L'application s'ouvrira automatiquement dans votre navigateur
   - L'URL par défaut est : `http://localhost:8501`

3. **Utiliser l'application**
   - Cliquez sur "Upload your resume here"
   - Sélectionnez un fichier PDF contenant votre CV
   - Attendez quelques secondes pour le traitement
   - La catégorie professionnelle détectée s'affichera automatiquement

## Structure du projet

```
resume-screening-app/
│
├── app.py                      # Application principale Streamlit
├── requirements.txt            # Dépendances Python
├── README.md                   # Documentation du projet
├── LICENSE                     # Licence du projet
│
├── models/                     # Modèles de machine learning pré-entraînés
│   ├── clf_model.pkl          # Modèle de classification
│   └── tfidf_model.pkl        # Modèle TF-IDF pour la vectorisation
│
├── dataset/                    # Dataset d'entraînement
│   └── UpdatedResumeDataSet.csv
│
├── notebook/                   # Notebook Jupyter pour l'analyse et l'entraînement
│   └── modeling.ipynb
│
└── utils/                      # Utilitaires
    └── utils.py                # Fonctions de nettoyage de texte
```

## Fonctionnement technique

1. **Extraction du texte** : Le texte est extrait du fichier PDF uploadé
2. **Nettoyage** : Le texte est nettoyé (suppression des URLs, caractères spéciaux, etc.)
3. **Vectorisation** : Le texte nettoyé est transformé en vecteur numérique via TF-IDF
4. **Classification** : Le modèle de classification prédit la catégorie professionnelle
5. **Affichage** : Le résultat est affiché à l'utilisateur

## Modèles

Les modèles pré-entraînés (`clf_model.pkl` et `tfidf_model.pkl`) sont inclus dans le dossier `models/`. Ces modèles ont été entraînés sur le dataset `UpdatedResumeDataSet.csv` et utilisent :

- **TF-IDF Vectorizer** : Pour transformer le texte en caractéristiques numériques
- **Classifier** : Modèle de classification supervisée (détails dans le notebook `modeling.ipynb`)

## Entraînement des modèles

Si vous souhaitez réentraîner les modèles :

1. Ouvrir le notebook `notebook/modeling.ipynb`
2. Exécuter toutes les cellules
3. Les nouveaux modèles seront sauvegardés dans le dossier `models/`

## Licence

Voir le fichier `LICENSE` pour plus de détails.

