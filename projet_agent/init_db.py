import sqlite3

DB_PATH = "database.db"

def main():
    print("Initialisation de la base de donnees...")
    connexion = sqlite3.connect(DB_PATH)
    cursor = connexion.cursor()
    cursor.execute("DROP TABLE IF EXISTS clients")
    cursor.execute("DROP TABLE IF EXISTS produits")
    
    cursor.execute("""
                   CREATE TABLE clients (
                       id   TEXT PRIMARY KEY,
                       nom  TEXT NOT NULL,
                       type TEXT NOT NULL,
                       solde    REAL NOT NULL,
                       email    TEXT NOT NULL
                   )
                """)
    cursor.execute("""
                   CREATE TABLE produits (
                       id   TEXT PRIMARY KEY,
                       nom  TEXT NOT NULL,
                       prix REAL NOT NULL,
                       description  TEXT NOT NULL,
                       type TEXT NOT NULL,
                       minimun_requis REAL NOT NULL
                   )
                """)
    
    clients = [
        ("C001", "Sophie Bernard", "VIP", 28900, "sophie.bernard@email.com"),
        ("C002", "Marc Dupont", "Standard", 5200, "marc.dupont@email.com"),
        ("C003", "Julie Martin", "Premium", 15000, "julie.martin@email.com"),
    ]
    cursor.executemany(
        "INSERT INTO clients VALUES (?, ?, ?, ?, ?)", clients
    )
    produits = [
        ("P001", "Compte Epargne Plus", 0, "Compte epargne avec 3% d'interets annuels", "Epargne", 1000),
        ("P002", "Portefeuille Actions", 5000, "Investissement en actions diversifiees", "Investissement", 5000),
        ("P003", "Assurance Vie Premium", 12000, "Contrat assurance vie avec garanties", "Assurance", 10000),
    ]
    
    cursor.executemany(
        "INSERT INTO produits VALUES (?, ?, ?, ?, ?, ?)", produits
    )
    connexion.commit()
    connexion.close()
    print("Base de donnees creee : database.db")
    
if __name__ == "__main__":
    main()