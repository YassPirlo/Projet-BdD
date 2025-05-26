import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

# Connexion 
def connect():
    return sqlite3.connect("bistro.db")

# Ajouter un produit
def ajouter_produit():
    def save():
        try:
            conn = connect()
            cur = conn.cursor()
            cur.execute("INSERT INTO Produit VALUES (?, ?, ?, ?)",
                        (int(id_entry.get()), nom_entry.get(), float(prix_entry.get()), cat_entry.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo("Succès", "Produit ajouté")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Erreur", str(e))

    win = tk.Toplevel()
    win.title("Ajouter un produit")
    
    tk.Label(win, text="ID").pack()
    id_entry = tk.Entry(win)
    id_entry.pack()

    tk.Label(win, text="Nom").pack()
    nom_entry = tk.Entry(win)
    nom_entry.pack()

    tk.Label(win, text="Prix").pack()
    prix_entry = tk.Entry(win)
    prix_entry.pack()

    tk.Label(win, text="Catégorie").pack()
    cat_entry = tk.Entry(win)
    cat_entry.pack()

    tk.Button(win, text="Ajouter", command=save).pack(pady=10)

# Voir les produits
def voir_produits():
    win = tk.Toplevel()
    win.title("Produits")
    tree = ttk.Treeview(win, columns=("ID", "Nom", "Prix", "Catégorie"), show="headings")
    for col in tree["columns"]:
        tree.heading(col, text=col)
    tree.pack(fill="both", expand=True)

    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Produit")
    for row in cur.fetchall():
        tree.insert("", "end", values=row)
    conn.close()

# Ajouter un serveur
def ajouter_serveur():
    def save():
        try:
            conn = connect()
            cur = conn.cursor()
            cur.execute("INSERT INTO Serveur VALUES (?, ?)",
                        (int(id_entry.get()), nom_entry.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo("Succès", "Serveur ajouté")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Erreur", str(e))

    win = tk.Toplevel()
    win.title("Ajouter un serveur")

    tk.Label(win, text="ID").pack()
    id_entry = tk.Entry(win)
    id_entry.pack()

    tk.Label(win, text="Nom").pack()
    nom_entry = tk.Entry(win)
    nom_entry.pack()

    tk.Button(win, text="Ajouter", command=save).pack(pady=10)

# Voir les serveurs
def voir_serveurs():
    win = tk.Toplevel()
    win.title("Serveurs")
    tree = ttk.Treeview(win, columns=("ID", "Nom"), show="headings")
    for col in tree["columns"]:
        tree.heading(col, text=col)
    tree.pack(fill="both", expand=True)

    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Serveur")
    for row in cur.fetchall():
        tree.insert("", "end", values=row)
    conn.close()

# Ajouter une table
def ajouter_table():
    def save():
        try:
            conn = connect()
            cur = conn.cursor()
            cur.execute("INSERT INTO Tables VALUES (?)",
                        (int(num_entry.get()),))
            conn.commit()
            conn.close()
            messagebox.showinfo("Succès", "Table ajoutée")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Erreur", str(e))

    win = tk.Toplevel()
    win.title("Ajouter une table")

    tk.Label(win, text="Numéro").pack()
    num_entry = tk.Entry(win)
    num_entry.pack()

    tk.Button(win, text="Ajouter", command=save).pack(pady=10)

# Voir les tables
def voir_tables():
    win = tk.Toplevel()
    win.title("Tables")
    tree = ttk.Treeview(win, columns=("Numéro",), show="headings")
    tree.heading("Numéro", text="Numéro")
    tree.pack(fill="both", expand=True)

    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Tables")
    for row in cur.fetchall():
        tree.insert("", "end", values=row)
    conn.close()

# Fenêtre principale
root = tk.Tk()
root.title("Gestion Bistro")
root.geometry("300x350")

btns = [
    ("Ajouter un produit", ajouter_produit),
    ("Voir les produits", voir_produits),
    ("Ajouter un serveur", ajouter_serveur),
    ("Voir les serveurs", voir_serveurs),
    ("Ajouter une table", ajouter_table),
    ("Voir les tables", voir_tables)
]

for text, command in btns:
    tk.Button(root, text=text, width=30, command=command).pack(pady=5)

root.mainloop()
