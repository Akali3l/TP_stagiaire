import yfinance as yf
from langchain.tools import tool

@tool
def outil_calculer_portefeuille(Actions: str) -> str:
    """Calcule la valeur totale d'un portefeuille d'actions.
    Format d'entree : SYMBOLE:QUANTITE separes par |
    Exemple : AAPL:10|MSFT:3"""
    try:
        lignes = actions.strip().split("|")
        resultats = []
        valeur_totale = 0.0
        variation_totale = 0.0
        
        for ligne in lignes:
            ligne = ligne.strip()
            if ":" not in ligne:
                resultats.append(f"Format invalide : '{ligne}' (attendu SYMBOLE:QUANTITE)")
                continue
            
            symbole, quantite_str = ligne.split(":")
            symbole = symbole.strip().upper()
            quantite = float(quantite_str.strip())
            ticker = yf.Ticker(symbole)
            
            info = ticker.info
            cours = info.get("currentPrice") or info.get("regularMarketPrice")
            if not cours:
                resultats.append(f"{symbole} : cours indisponible")
                continue
            
            ouverture = info.get("open") or info.get("regularMarketOpen")
            if ouverture and ouverture != 0:
                variation = round(((cours - ouverture) / ouverture) * 100, 2)
            else:
                variation = 0.0
                
            valeur_ligne = round(cours, quantite, 2)
            valeur_totale += valeur_ligne
            variation_totale += variation
            signe = "+" if variation >= 0 else ""
            
            resultats.append(
                f"- {symbole} : {quantite:.0f} actions x {cours} dollars "
                f"= {valeur_ligne:.2f} dollars ({signe}{variation}%)"
            )
            variation_moyenne = round(variation_totale / len(lignes), 2)
            signe_total = "+" if variation_moyenne >= 0 else ""
            
            resultats.append(f"\nValeur totale du portefeuille : {valeur_totale:.2f} dollars")
            resultats.append(f"Variation globale du jour    : {signe_total}{variation_moyenne}%")
            
            return "\n".join(resultats)
        
    except Exception as e:
        return f"Erreur lors du calcul du portefeuille : {str(e)}"