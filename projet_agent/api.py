from fastapi import FastAPI
from pydantic import BaseModel
from agent import creer_agent

app = FastAPI(title="Agent Financier API")
agent = creer_agent()
class QueryRequest(BaseModel):
    question: str
    
class QueryResponse(BaseModel):
    question: str
    reponse: str
    
@app.post("/api/agent/query", response_model=QueryResponse)
def query_agent(request: QueryRequest):
    """Envoi une question a l'agent et retourne sa reponse en JSON.
    Exemple : {"question": "Donne moi les infos du client C001"}"""
    resultat = agent.invoke({"input": request.question})
    
    return QueryResponse(
        question=request.question,
        reponse=resultat["output"]
    )

@app.get("/")
def accueil():
    return {"message": "API Agent FInancier - fonctionne !"}