from agent import creer_agent

def main():
    print("=== Agent Financier ===")
    print("Tape 'quitter' pour arreter.\n")
    agent = creer_agent()
    
    while True:
        question = input("Ecris : ").strip()
        if not question:
            continue
        if question.lower() == "quitter":
            break
        resultat = agent.invoke({"input": question})
        print(f"\nAgent : {resultat['output']}\n")
        
if __name__ == "__main__":
    main()