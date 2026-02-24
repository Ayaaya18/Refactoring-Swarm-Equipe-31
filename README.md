# 🐝 The Refactoring Swarm

🎓 **TP du module IGL (Ingénierie du Génie Logiciel)**  
🏫 École Nationale Supérieure d’Informatique (ENSI)  
📅 Année universitaire : 2025–2026  
👥 Projet en équipe (4 étudiants)  
⏱ Durée : 2 à 3 semaines (Sprint unique)

---

## 🔬 Contexte scientifique

Ce projet s’inscrit dans une expérience de **Génie Logiciel Empirique** visant à étudier la capacité
de systèmes multi-agents autonomes (basés sur des LLMs) à effectuer de la **maintenance logicielle automatique**.

L’objectif n’est pas seulement de produire du code fonctionnel, mais de concevoir une **architecture
collaborative d’agents intelligents** capable d’analyser, corriger et valider du code Python défectueux
sans intervention humaine directe.

---

## 🎯 Objectif du TP

Construire un système multi-agents nommé **The Refactoring Swarm** capable de :

- Prendre en entrée un dossier contenant du **code Python mal conçu** (buggé, non documenté, non testé)
- Analyser la qualité et les erreurs du code
- Appliquer automatiquement des corrections
- Vérifier la validité du code corrigé via des **tests unitaires**
- Générer des **logs expérimentaux exploitables pour l’évaluation automatique**

---

## 🧠 Architecture du système

Le système repose sur la collaboration de **trois agents autonomes minimum** :

### 1️⃣ The Auditor (Agent Auditeur)
- Analyse le code source
- Lance l’analyse statique (ex : `pylint`)
- Génère un **plan de refactoring**

### 2️⃣ The Fixer (Agent Correcteur)
- Applique les corrections fichier par fichier
- Corrige les erreurs logiques, syntaxiques et structurelles
- Suit le plan généré par l’Auditeur

### 3️⃣ The Judge (Agent Testeur)
- Exécute les tests unitaires (`pytest`)
- Valide ou invalide la correction
- Met en place une **boucle de self-healing** en cas d’échec

➡️ Le système s’arrête automatiquement lorsque tous les tests sont validés ou après un nombre
maximal d’itérations.

---

## 👥 Organisation de l’équipe

Chaque membre de l’équipe est responsable d’un rôle précis :

- 🧠 **Orchestrateur (Lead Dev)**  (AOUICHAT Ayeterrahmane)
  Conception du flux d’exécution, coordination des agents, gestion du `main.py` et des arguments CLI.

- 🛠 **Ingénieur Outils (Toolsmith)**  (HEMAIZIA Abderrahmane)
  Développement des outils internes (lecture/écriture, pylint, pytest), sandboxing et sécurité.

- 💬 **Ingénieur Prompt (Prompt Engineer)**  (DJAFAR Aya) 
  Rédaction, optimisation et versioning des prompts système des agents.

- 📊 **Responsable Qualité & Data (Data Officer)** (BRAHIMI Aya)
  Gestion de la télémétrie, génération et validation du fichier `experiment_data.json`.

⚠️ Le projet est **fortement collaboratif** : toute modification impactant les interfaces doit être
communiquée à l’équipe.

---

## 🗂 Structure du projet
├── agents/ # Définition des agents (Auditor, Fixer, Judge)
├── tools/ # Outils internes (pylint, pytest, sandbox, etc.)
├── prompts/ # System prompts versionnés
├── logs/
│ └── experiment_data.json
├── sandbox/ # Dossier cible pour le refactoring
├── tests/ # Tests internes
├── main.py # Point d’entrée du système
├── check_setup.py # Vérification de l’environnement
└── README.md

---

## ▶️ Exécution du projet

1. Créer un environnement virtuel :
```bash
py -3.11 -m venv venv
venv\Scripts\activate
```
```Installer les dépendances :

pip install -r requirements.txt
```
```Vérifier l’installation :

python check_setup.py

```
```Lancer le système :

python main.py --target_dir "./sandbox/dataset_inconnu"
```
📊 Logs & Données expérimentales

-Toutes les actions des agents sont enregistrées dans :
logs/experiment_data.json
-Ce fichier respecte un schéma strict et contient :
L’historique complet des décisions
Les scores de qualité
Les résultats des tests
Les timestamps et identifiants uniques

🤖 Critères d’évaluation automatisée:
Dimension	Poids
Performance (tests + qualité)	40%
Robustesse technique	30%
Qualité des données	30%
L’évaluation est réalisée automatiquement sur un jeu de données caché.

⚠️ Intégrité académique:

Ce projet est soumis à une politique stricte anti-plagiat :

Analyse de similarité du code
Analyse des prompts
Vérification de l’historique Git
Détection de signatures dans les logs
Tout manquement entraîne une disqualification immédiate.

✍️ Auteurs:

Étudiant 1 – AOUICHAT Ayeterrahmane

Étudiant 2 – HEMAIZIA Abderrahamne

Étudiant 3 – DJAFAR Aya

Étudiant 4 – BRAHIMI Aya

👨‍🏫 Encadrement:

Enseignant : BATATA Sofiane
Module : IGL
Niveau : 1CS – ESI
