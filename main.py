# main.py

import argparse
import os
import sys
from dotenv import load_dotenv
from termcolor import colored  # Pour affichage coloré
import time
from src.utils.logger import log_experiment, ActionType
from src.graph import create_graph
from src.tools import SwarmTools

load_dotenv()


# Définition de quelques couleurs pour lisibilité
class Colors:
    HEADER = "cyan"
    OKBLUE = "blue"
    OKGREEN = "green"
    WARNING = "yellow"
    FAIL = "red"
    BOLD = None  # Utilisé avec termcolor attr=["bold"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--target_dir", type=str, required=True)
    parser.add_argument("--cooldown", type=int, default=0)
    parser.add_argument("--disable_llm", action="store_true")
    parser.add_argument("--output_mode", type=str, choices=["overwrite", "copy"], default="overwrite")
    parser.add_argument("--output_dir", type=str, default="refactored")
    parser.add_argument("--model", type=str, default="llama-3.1-8b-instant")
    parser.add_argument("--max_files", type=int, default=0)
    args = parser.parse_args()

    # Chemins et options
    target_dir = os.path.abspath(args.target_dir)
    cooldown = args.cooldown
    disable_llm = args.disable_llm
    output_mode = args.output_mode
    output_dir = args.output_dir
    model_name = args.model
    max_files = args.max_files

    if not os.path.exists(target_dir):
        print(colored(f"❌ Dossier {target_dir} introuvable.", Colors.FAIL))
        sys.exit(1)

    tools = SwarmTools(target_dir)
    python_files = tools.list_files()
    if max_files > 0:
        python_files = python_files[:max_files]

    if not python_files:
        print(colored("⚠️ Aucun fichier Python trouvé dans le dossier cible.", Colors.WARNING))
        sys.exit(0)

    print(colored(f"\n🚀 DÉMARRAGE DU SWARM - {len(python_files)} fichiers Python détectés\n", Colors.HEADER))
    for i, f in enumerate(python_files, 1):
        print(f"📄 [{i}] {f}")

    # Créer le graph
    app = create_graph(target_dir, model_name)

    # État initial
    initial_state = {
        "target_dir": target_dir,
        "files": python_files,
        "current_file_index": 0,
        "current_file_path": python_files[0],
        "current_file_content": "",
        "pylint_report": "",
        "refactoring_plan": "",
        "test_results": {},
        "iteration_count": 0,
        "max_iterations": 10,
        "status": "STARTING",
        "messages": [],
        "cooldown_seconds": cooldown,
        "disable_llm": disable_llm,
        "output_mode": output_mode,
        "output_dir": output_dir,
        "results": []
    }

    print(colored("\n🔄 EXÉCUTION EN COURS...\n", Colors.OKBLUE))

    # Fonction pour afficher l'état après chaque fichier
    def print_file_status(state):
        file_path = state.get("current_file_path")
        iteration = state.get("iteration_count", 0)
        test_results = state.get("test_results", {})
        success = test_results.get("success", False)
        status_str = colored("✅ Passed", Colors.OKGREEN) if success else colored("❌ Failed", Colors.FAIL)
        print(f"📝 Fichier : {file_path} | Iteration : {iteration} | Test : {status_str}")

    # Exécution du Swarm
    final_state = app.invoke(initial_state, config={"recursion_limit": 200})

    print(colored("\n✅ TRAITEMENT TERMINÉ\n", Colors.OKGREEN))

    all_results = final_state.get("results", [])

    if not all_results:
        print(colored("Aucune correction appliquée.", Colors.WARNING))
        return

    # Résumé final
    print(colored("\n📊 Résumé des corrections :", Colors.HEADER))
    for idx, r in enumerate(all_results, 1):
        time.sleep(5)
        file_str = colored(r.get("original_path", "N/A"), Colors.OKBLUE)
        mode_str = r.get("mode", "N/A")
        iter_str = r.get("iterations", "N/A")
        before_score = r.get("before_score", "N/A")
        after_score = r.get("after_score", "N/A")
        status = r.get("status", "N/A")
        status_colored = colored(status, Colors.OKGREEN) if status == "UPDATED" else colored(status, Colors.FAIL)

        print(f"[{idx}] 📄 {file_str}")
        print(f"     ➜ Mode        : {mode_str}")
        print(f"     ➜ Itérations  : {iter_str}")
        print(f"     ➜ Score Avant : {before_score}")
        print(f"     ➜ Score Après : {after_score}")
        print(f"     ➜ Statut      : {status_colored}\n")


if __name__ == "__main__":
    main()
