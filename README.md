# 🍽️ Projet Base de Données – Bistro "Le Vichy"

Ce projet consiste à modéliser et implémenter une base de données pour un bistro-restaurant, permettant de gérer les serveurs, les tables, les produits, les commandes, et les paiements.

## 🗃️ Contenu du projet

- `script.sql` : contient le script de création des tables et l'insertion d'un jeu de données complet.
- `sql.py` : script Python permettant d'exécuter automatiquement le fichier `script.sql` et de générer la base `bistro.db`.
- `bistro.db` : base de données SQLite générée automatiquement.
- `README.md` : ce fichier de documentation.

## 📊 Structure de la base

La base de données contient 8 tables :
- `Serveur` : liste des serveurs.
- `Tables` : tables du restaurant.
- `Affectation` : lie un serveur à une table un jour donné.
- `Produit` : boissons, entrées, plats, desserts.
- `Commande` : commande passée à une table, un jour, par un serveur.
- `LigneCommande` : détail des produits commandés.
- `Paiement` : enregistre les paiements, mode et TVA.

## ✅ Exécution

1. Ouvrir un terminal dans le dossier du projet.
2. Exécuter le script Python pour créer la base :

```bash
python sql.py
