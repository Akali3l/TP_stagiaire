import yfinance as yf

def obtenir_cours_action(symbole: str) -> dict:
    """Retourne le cours reel d'une action via yfinance."""
    try:
        ticker = yf.Ticker(symbole.upper())
        info = ticker.info
        cours = info.get("currentPrice") or info.get("regularMarketPrice")
        if not cours:
            return {"erreur": True, "message": f"Symbole '{symbole}' invalide ou donnees indisponibles."}
        
        ouverture = info.get("open") or info.get("regularMarketOpen")
        if ouverture and ouverture != 0:
            variation = round(((cours - ouverture) / ouverture) * 100, 2)
        else:
            variation = 0.0
            
        volume = info.get("volume") or info.get("regularMarketVolume", 0)
        devise = info.get("currency", "USD")
        return {
            "symbole":      symbole.upper(),
            "cours":        round(cours, 2),
            "variation_pct":        variation,
            "volume":       volume,
            "devise":       devise,
            "source":       "yfinance   (reel)"
        }
        
    except Exception as e:
        return {"erreur": True, "message": f"Erreur lors de la recuperation de {symbole} : {str(e)}"}