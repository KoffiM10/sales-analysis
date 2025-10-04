"""
Projet : Analyse des ventes
Description : Nettoyage, agrégation et visualisation des ventes par mois.
Auteur : Koffi M.
Date : 2025
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- Chargement des données ---
data_path = 'data/ventes.csv'

if not os.path.exists(data_path):
    raise FileNotFoundError(f"Le fichier {data_path} est introuvable. Vérifie le chemin du fichier.")

df = pd.read_csv(data_path)

# --- Aperçu du jeu de données ---
print("Aperçu du jeu de données :")
print(df.head())

# --- Nettoyage ---
df = df.dropna(subset=['Date', 'Montant'])
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna(subset=['Date'])
df['Montant'] = pd.to_numeric(df['Montant'], errors='coerce')
df = df.dropna(subset=['Montant'])

# --- Agrégation mensuelle ---
df['Mois'] = df['Date'].dt.to_period('M')
ventes_mensuelles = df.groupby('Mois', as_index=False)['Montant'].sum()

# --- Résultat ---
print("\nVentes totales par mois :")
print(ventes_mensuelles)

# --- Convertir la colonne 'Mois' en texte pour l'affichage ---
ventes_mensuelles['Mois'] = ventes_mensuelles['Mois'].astype(str)


# --- Visualisation ---
plt.figure(figsize=(10,6))
sns.lineplot(data=ventes_mensuelles, x='Mois', y='Montant', marker='o', linewidth=2.5)
plt.title('Évolution mensuelle des ventes', fontsize=14, fontweight='bold')
plt.xlabel('Mois')
plt.ylabel('Montant des ventes')
plt.grid(alpha=0.3)
plt.tight_layout()

os.makedirs("output", exist_ok=True)
plt.savefig("output/ventes_mensuelles.png", dpi=300)
plt.show()

print("\n✅ Analyse terminée : graphique enregistré dans le dossier 'output/'.")
