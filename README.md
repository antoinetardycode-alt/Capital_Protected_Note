# Capital Protected Note (CPN) - Pricing & Simulation Tool

Ce projet est un outil d'aide à la structuration d'un produit financier à **capital garanti** (CPN) sur l'indice S&P 500.

## Présentation du Projet
L'objectif est de valoriser et de simuler le profil de remboursement d'une note structurée combinant :
1. **Une jambe obligataire** : Un Zéro-Coupon pour assurer la protection du capital à 100%.
2. **Une jambe optionnelle** : Un Call européen permettant de capter la performance du sous-jacent.

## Caractéristiques Techniques
- **Modèle de Pricing** : Utilisation de la formule analytique de **Black-Scholes-Merton** pour calculer la Fair Value du produit.
- **Simulation de Risque** : Moteur de simulation de **Monte Carlo** basé sur un Mouvement Brownien Géométrique (GBM).
- **Analyse de Scénarios** : Possibilité de tester des volatilités extrêmes (Stress-Testing) pour observer la déformation du payoff.

## Installation et Utilisation
1. **Installation des dépendances** :
   ```bash
   pip install -r requirements.txt
2. **Lancement du programme** :
   ```bash
   streamlit run dashboard.py
