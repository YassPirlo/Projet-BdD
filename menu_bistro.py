import sqlite3

def ajouter_produit():
    conn = sqlite3.connect("bistro.db")
    cursor = conn.cursor()
    idProduit = int(input("ID du produit : "))
    nomProduit = input("Nom du produit : ")
    prixUnitaire = float(input("Prix unitaire (€) : "))
    categorie = input("Catégorie (Boisson, Entrée, Plat, Dessert) : ")
    cursor.execute("INSERT INTO Produit VALUES (?, ?, ?, ?)",
                   (idProduit, nomProduit, prixUnitaire, categorie))
    conn.commit()
    conn.close()
    print(f"✅ Produit '{nomProduit}' ajouté.\n")

def ajouter_serveur():
    conn = sqlite3.connect("bistro.db")
    cursor = conn.cursor()
    idServ = int(input("ID du serveur : "))
    nomServ = input("Nom du serveur : ")
    cursor.execute("INSERT INTO Serveur VALUES (?, ?)", (idServ, nomServ))
    conn.commit()
    conn.close()
    print(f"✅ Serveur '{nomServ}' ajouté.\n")

def ajouter_table():
    conn = sqlite3.connect("bistro.db")
    cursor = conn.cursor()
    numTable = int(input("Numéro de table : "))
    cursor.execute("INSERT INTO Tables VALUES (?)", (numTable,))
    conn.commit()
    conn.close()
    print(f"✅ Table {numTable} ajoutée.\n")

def voir_produits():
    conn = sqlite3.connect("bistro.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Produit")
    produits = cursor.fetchall()
    print("=== LISTE DES PRODUITS ===")
    for p in produits:
        print(f"ID {p[0]} | {p[1]} | {p[2]} € | Catégorie : {p[3]}")
    print()
    conn.close()

def voir_serveurs():
    conn = sqlite3.connect("bistro.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Serveur")
    for s in cursor.fetchall():
        print(f"ID : {s[0]} | Nom : {s[1]}")
    print()
    conn.close()

def voir_tables():
    conn = sqlite3.connect("bistro.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Tables")
    for t in cursor.fetchall():
        print(f"Table : {t[0]}")
    print()
    conn.close()

def menu():
    while True:
        print("=== MENU BISTRO ===")
        print("1 - Ajouter un produit")
        print("2 - Ajouter un serveur")
        print("3 - Ajouter une table")
        print("4 - Voir les produits")
        print("5 - Voir les serveurs")
        print("6 - Voir les tables")
        print("7 - Quitter")
        choix = input("Votre choix : ")

        if choix == '1':
            ajouter_produit()
        elif choix == '2':
            ajouter_serveur()
        elif choix == '3':
            ajouter_table()
        elif choix == '4':
            voir_produits()
        elif choix == '5':
            voir_serveurs()
        elif choix == '6':
            voir_tables()
        elif choix == '7':
            print("👋 À bientôt !")
            break
        else:
            print("⛔ Choix invalide.\n")

if __name__ == "__main__":
    menu()
