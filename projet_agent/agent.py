import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_openai_tools_agent, AgentExecutor
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from tools.client_tools import outil_rechercher_client, outil_lister_clients
from tools.product_tools import outil_rechercher_produit, outil_lister_produits
from tools.finance_tools import outil_cours_action
from tools.tavily_tools import creer_outil_tavily
from tools.portefeuille import outil_calculer_portefeuille
from langchain_experimental.tools import PythonREPLTool
from langchain.memory import ConversationBufferMemory

load_dotenv()
def creer_agent() -> AgentExecutor:
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0,
                     openai_api_key=os.getenv("OPENAI_API_KEY"))
    python_repl = PythonREPLTool()
    python_repl.description = (
        "Execute du code Python pour des calculs complexes ou traitements "
        "de donnees non couverts par les autres outils."
        "Entree : code Python valide sous forme de chaine."
        "IMPORTANT : utilise toujours print() pour afficher les resultats, "
        "sinon aucun resultat ne sera retourne."
    )
    tools = [
        outil_rechercher_client, outil_lister_clients,
        outil_rechercher_produit, outil_lister_produits,
        outil_cours_action,
        creer_outil_tavily(),
        outil_calculer_portefeuille,
        python_repl,
    ]
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Tu es un assistant financier. Utilise les outils disponibles. Reponds en francais."),
        MessagesPlaceholder(variable_name="chat_history", optional=True),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])
    
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )
    
    agent = create_openai_tools_agent(llm, tools, prompt)
    return AgentExecutor(
        agent=agent, 
        tools=tools, 
        memory=memory,
        verbose=True, 
        max_iterations=10)