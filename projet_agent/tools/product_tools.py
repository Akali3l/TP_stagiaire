from langchain.tools import tool
from database import rechercher_produit, lister_produits

@tool
def outil_rechercher_produit(produit_id: str) -> str:
    """Recherche un produit financier par son ID (ex: P001, P002, P003)."""
    r = rechercher_produit(produit_id)
    if not r.get("trouve"):
        return r["message"]
    return f"Produit : {r['nom']} | Prix : {r['prix']} euros | Min. requis : {r['minimun_requis']} euros | {r['description']}"

@tool
def outil_lister_produits(query: str = "") -> str:
    """Liste tous les produits financiers disponibles."""
    produits = lister_produits()
    return "\n".join([f"- {p['id']} : {p['nom']} ({p['type']}) - {p['prix']} euros" for p in produits])