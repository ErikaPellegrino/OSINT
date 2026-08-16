
import os
import sys
from modules.github_module import analyze_github_user
from modules.stackoverflow_module import analyze_stackoverflow_user
from modules.reddit_module import analyze_reddit_user  # <--- IMPORT REDDIT
from modules.correlator import correlate_target_data

def main_menu():
    while True:
        print("\n==================================================")
        print("    SUITE OSINT & SOCMINT - MULTI PLATFORM TOOL   ")
        print("==================================================")
        print("1. Analizza profilo GitHub")
        print("2. Analizza profilo Stack Overflow")
        print("3. Analizza profilo Reddit 🤖")
        print("4. 🔥 GENERATORE MAPPA CORRELATA (Analisi Report JSON)")
        print("5. Esci")
        print("--------------------------------------------------")

        choice = input("Seleziona un'opzione (1-5): ").strip()

        if choice == "1":
            user = input("\nInserisci l'username di GitHub da analizzare: ").strip()
            analyze_github_user(user)

        elif choice == "2":
            query = input("\nInserisci l'username o l'ID di Stack Overflow: ").strip()
            analyze_stackoverflow_user(query)

        elif choice == "3":
            user = input("\nInserisci l'username di Reddit da analizzare: ").strip()
            analyze_reddit_user(user)

        elif choice == "4":
            target = input("\nInserisci il nome/parola chiave del target da correlare (es. google): ").strip()
            correlate_target_data(target)

        elif choice == "5":
            print("\nChiusura dello strumento OSINT. Arrivederci!")
            sys.exit()

        else:
            print("\n[-] Opzione non valida. Riprova.")

if __name__ == "__main__":
    main_menu()