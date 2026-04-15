import os
from langchain_community.tools.tavily_search import TavilySearchResults

def creer_outil_tavily():
    outil = TavilySearchResults(
        max_results=3,
        tavily_api_key=os.getenv("TAVILY_API_KEY"),
    descritpion = (
        "Effectue une recherche web pour repondre a des questions ouvertes : "
        "actualites financieres, informations sur une entreprise, resultats trimestriels. "
        "Utilise cet outil pour tout ce qui n'est pas couvert par les autres outils."
        )
    )
    
    return outil