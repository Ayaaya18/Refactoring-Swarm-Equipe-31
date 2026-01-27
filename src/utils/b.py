from langgraph.graph import StateGraph, END
from src.state import SwarmState
from src.agents import SwarmAgents
from src.tools import SwarmTools

def create_graph(target_dir: str, model_name: str = "llama-3.1-8b-instant"):
    tools = SwarmTools(target_dir)
    agents = SwarmAgents(tools, model_name)

    workflow = StateGraph(SwarmState)

    # Define Nodes
    workflow.add_node("manager", lambda state: state) # Pass-through node for routing
    workflow.add_node("auditor", agents.auditor_node)
    workflow.add_node("fixer", agents.fixer_node)
    workflow.add_node("judge", agents.judge_node)

    # Define Logic for Manager (Router)
    def manager_router(state: SwarmState):
        if state.get("status") == "DONE":
            return END
        files = state["files"]
        index = state["current_file_index"]
        if index < len(files):
            return "auditor"
        return END


    # Define Logic for Judge (Router)
    def judge_router(state: SwarmState):
        results = state["test_results"]
        success = results.get("success", False)
        iteration = state["iteration_count"]
        max_iter = state["max_iterations"]
        if state.get("disable_llm", False):
            return "next_file"
        if state.get("status") == "LLM_FAILURE":
            return "next_file"
        if success or iteration >= max_iter:
            return "next_file"
        return "retry"

    # Node to update state for next file
    def next_file_node(state: SwarmState):
        next_index = state["current_file_index"] + 1
        new_state = state.copy()
    
        if next_index >= len(state["files"]):
            new_state["status"] = "DONE"  # Marque la fin
            new_state["current_file_path"] = None
            return new_state

        # Sinon, on passe au fichier suivant
        new_state["current_file_index"] = next_index
        new_state["current_file_path"] = state["files"][next_index]
        new_state["iteration_count"] = 0
        new_state["current_file_content"] = ""
        new_state["pylint_report"] = ""
        new_state["refactoring_plan"] = ""
        new_state["test_results"] = {}
        new_state["status"] = "STARTING"
    
        return new_state



    workflow.add_node("next_file_processor", next_file_node)

    # Edges
    workflow.set_entry_point("manager")

    workflow.add_conditional_edges(
        "manager",
        manager_router,
        {
            "auditor": "auditor",
            "end": END
        }
    )

    workflow.add_edge("auditor", "fixer")
    workflow.add_edge("fixer", "judge")

    workflow.add_conditional_edges(
        "judge",
        judge_router,
        {
            "retry": "fixer",
            "next_file": "next_file_processor"
        }
    )

    workflow.add_edge("next_file_processor", "manager")

    app = workflow.compile()
    return app