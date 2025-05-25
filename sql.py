import sqlite3

# Connexion (crée le fichier bistro.db s'il n'existe pas)
conn = sqlite3.connect('bistro.db')
cursor = conn.cursor()

# Lecture du script SQL
with open('script.sql', 'r', encoding='utf-8') as f:
    sql_script = f.read()

# Exécution du script SQL
cursor.executescript(sql_script)

# Sauvegarde et fermeture
conn.commit()
conn.close()

print("Base de données créée avec succès !")
