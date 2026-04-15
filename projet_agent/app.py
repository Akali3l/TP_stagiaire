import streamlit as st
from agent import creer_agent

st.set_page_config(page_title="Agent Financier", page_icon="🤖")
st.title("🤖 Agent Financier")

# --- Sidebar : outils disponibles ---
with st.sidebar:
    st.header("🛠️ Outils disponibles")
    st.markdown("""
    - 🔍 Rechercher un client
    - 📋 Lister les clients
    - 📦 Rechercher un produit
    - 📋 Lister les produits
    - 📈 Cours boursiers (yfinance)
    - 🌐 Recherche web (Tavily)
    - 💼 Calcul de portefeuille
    - 🐍 Exécution Python (REPL)
    """)
    if st.button("🗑️ Réinitialiser la conversation"):
        st.session_state.historique = []
        st.rerun()

# --- Initialisation de l'historique et de l'agent ---
if "historique" not in st.session_state:
    st.session_state.historique = []

if "agent" not in st.session_state:
    st.session_state.agent = creer_agent()

# --- Affichage de l'historique ---
for message in st.session_state.historique:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- Champ de saisie ---
question = st.chat_input("Pose une question à l'agent...")

if question:
    # Affiche la question de l'utilisateur
    with st.chat_message("user"):
        st.markdown(question)
    st.session_state.historique.append({"role": "user", "content": question})

    # Appelle l'agent et affiche la réponse
    with st.chat_message("assistant"):
        with st.spinner("L'agent réfléchit..."):
            resultat = st.session_state.agent.invoke({"input": question})
            reponse = resultat["output"]
        st.markdown(reponse)
    st.session_state.historique.append({"role": "assistant", "content": reponse})