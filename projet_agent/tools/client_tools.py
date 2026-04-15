from langchain.tools import tool
from database import rechercher_client, lister_clients

@tool
def outil_rechercher_client(client_id: str) -> str:
    """Recherche un client par son ID (ex: C001, C002, C003)."""
    r = rechercher_client(client_id)
    if not r.get("trouve"):
        return r["message"]
    return f"Client : {r['nom']} | Type : {r['type']} | Solde : {r['solde']} euros | Email : {r['email']}"

@tool
def outil_lister_clients(query: str = "") -> str:
    """Liste tous les clients disponibles."""
    clients = lister_clients()
    return "\n".join([f"- {c['id']} : {c['nom']} ({c['type']}) - {c['solde']} euros" for c in clients])