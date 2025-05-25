-- Création de la table Serveur
CREATE TABLE Serveur (
    idServ INTEGER PRIMARY KEY,
    nomServ TEXT NOT NULL
);

-- Création de la table Tables
CREATE TABLE Tables (
    numTable INTEGER PRIMARY KEY
);

-- Création de la table Affectation (relation Serveur/Table avec date)
CREATE TABLE Affectation (
    idServ INTEGER,
    numTable INTEGER,
    dateAffect DATE,
    PRIMARY KEY (idServ, numTable, dateAffect),
    FOREIGN KEY (idServ) REFERENCES Serveur(idServ),
    FOREIGN KEY (numTable) REFERENCES Tables(numTable)
);

-- Création de la table Produit
CREATE TABLE Produit (
    idProduit INTEGER PRIMARY KEY,
    nomProduit TEXT NOT NULL,
    prixUnitaire REAL NOT NULL CHECK (prixUnitaire >= 0),
    categorie TEXT
);

-- Création de la table Commande
CREATE TABLE Commande (
    numCommande INTEGER NOT NULL,
    dateCommande DATE NOT NULL,
    idServ INTEGER NOT NULL,
    numTable INTEGER NOT NULL,
    montantTotal REAL NOT NULL CHECK (montantTotal >= 0),
    PRIMARY KEY (numCommande, dateCommande),
    FOREIGN KEY (idServ) REFERENCES Serveur(idServ),
    FOREIGN KEY (numTable) REFERENCES Tables(numTable)
);

-- Création de la table LigneCommande (détail de chaque commande)
CREATE TABLE LigneCommande (
    idLigne INTEGER PRIMARY KEY AUTOINCREMENT,
    numCommande INTEGER NOT NULL,
    dateCommande DATE NOT NULL,
    idProduit INTEGER NOT NULL,
    quantite INTEGER NOT NULL CHECK (quantite > 0),
    prixUnitaire REAL NOT NULL CHECK (prixUnitaire >= 0),
    montantLigne REAL NOT NULL CHECK (montantLigne >= 0),
    FOREIGN KEY (numCommande, dateCommande) REFERENCES Commande(numCommande, dateCommande),
    FOREIGN KEY (idProduit) REFERENCES Produit(idProduit)
);

-- Création de la table Paiement
CREATE TABLE Paiement (
    idPaiement INTEGER PRIMARY KEY,
    numCommande INTEGER NOT NULL,
    dateCommande DATE NOT NULL,
    modePaiement TEXT NOT NULL,
    montantPaye REAL NOT NULL,
    montantHT REAL NOT NULL,
    tva19_6 REAL,
    tva7 REAL,
    FOREIGN KEY (numCommande, dateCommande) REFERENCES Commande(numCommande, dateCommande)
);

INSERT INTO Serveur (idServ, nomServ)
VALUES (1, 'Yassine'), (2, 'Camille');

INSERT INTO Tables (numTable)
VALUES (8), (12);

INSERT INTO Affectation (idServ, numTable, dateAffect)
VALUES
  (1, 12, '2024-12-05'),
  (2, 8, '2024-12-05');

INSERT INTO Produit (idProduit, nomProduit, prixUnitaire, categorie)
VALUES
  (101, 'Coca', 2.60, 'Boisson'),
  (102, 'Salade nicoise', 7.00, 'Entrée'),
  (103, 'Salade de Fruits de Mer', 6.00, 'Entrée'),
  (104, 'Magret de Canard', 9.00, 'Plat'),
  (105, 'Steak Tartare', 8.00, 'Plat'),
  (106, 'Île Flottante', 5.00, 'Dessert'),
  (107, 'Poire Belle Hélène', 6.00, 'Dessert'),
  (108, 'St Pourçain rouge', 15.00, 'Boisson');

INSERT INTO Commande (numCommande, dateCommande, idServ, numTable, montantTotal)
VALUES (81, '2024-12-05', 1, 12, 61.20);

INSERT INTO LigneCommande (numCommande, dateCommande, idProduit, quantite, prixUnitaire, montantLigne)
VALUES
  (81, '2024-12-05', 101, 2, 2.60, 5.20),
  (81, '2024-12-05', 102, 1, 7.00, 7.00),
  (81, '2024-12-05', 103, 1, 6.00, 6.00),
  (81, '2024-12-05', 104, 1, 9.00, 9.00),
  (81, '2024-12-05', 105, 1, 8.00, 8.00),
  (81, '2024-12-05', 106, 1, 5.00, 5.00),
  (81, '2024-12-05', 107, 1, 6.00, 6.00),
  (81, '2024-12-05', 108, 1, 15.00, 15.00);

INSERT INTO Paiement (idPaiement, numCommande, dateCommande, modePaiement, montantPaye, montantHT, tva19_6, tva7)
VALUES
  (1, 81, '2024-12-05', 'Carte crédit', 40.00, 55.21, 3.31, 2.68),
  (2, 81, '2024-12-05', 'Espèces', 21.20, 55.21, 3.31, 2.68);
