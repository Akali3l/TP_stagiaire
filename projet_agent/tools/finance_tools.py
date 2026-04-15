from langchain.tools import tool
from finance import obtenir_cours_action

@tool
def outil_cours_action(symbole: str) -> str:
    """Retourne le cours d'une action (ex: AAPL, GOOGL, MSFT, TSLA, LVMH)."""
    r = obtenir_cours_action(symbole)
    if r.get("erreur"):
        return r["message"]
    signe = "+" if r["variation_pct"] >= 0 else ""
    volume = r["volume"] if r["volume"] else "indisponible"
    return (
        f"{r['symbole']} : {r['cours']} {r['devise']}\n"
        f"- Variation du jour : {signe}{r['variation_pct']}%\n"
        f"- Volume : {volume}\n"
        f"- Source : {r['source']}"
    )