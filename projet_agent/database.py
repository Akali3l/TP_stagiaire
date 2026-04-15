import sqlite3

DB_PATH = "database.db"

def get_connection():
    connexion = sqlite3.connect(DB_PATH)
    connexion.row_factory = sqlite3.Row
    return connexion

def rechercher_client(client_id: str) -> dict:
    connexion = get_connection()
    try:
        cursor = connexion.cursor()
        cursor.execute("SELECT * FROM clients WHERE id = ?", (client_id.upper(),))
        row = cursor.fetchone()
        if row:
            return {"trouve": True, **dict(row)}
        return {"trouve": False, "message" : f"Client {client_id} non trouve"}
    finally:
        connexion.close()
        
def rechercher_produit(produit_id: str) -> dict:
    connexion = get_connection()
    try:
        cursor = connexion.cursor()
        cursor.execute("SELECT * FROM produits WHERE id = ?", (produit_id.upper(),))
        row = cursor.fetchone()
        if row:
            return {"trouve": True, **dict(row)}
        return {"trouve": False, "message": f"Produit {produit_id} non trouve"}
    finally:
        connexion.close()
        
def lister_clients() -> list:
    connexion = get_connection()
    try:
        cursor = connexion.cursor()
        cursor.execute("SELECT * FROM clients")
        return [dict(row) for row in cursor.fetchall()]
    finally:
        connexion.close()
        
def lister_produits() -> list:
    connexion = get_connection()
    try:
        cursor = connexion.cursor()
        cursor.execute("SELECT * FROM produits")
        return [dict(row) for row in cursor.fetchall()]
    finally:
        connexion.close()