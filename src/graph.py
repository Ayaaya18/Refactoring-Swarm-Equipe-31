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
        current_file = state.get("current_file_path")
        if current_file is None:
            return END  
        return "auditor"







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
        files = state["files"]

        next_path = files[next_index] if next_index < len(files) else None

        print(f"➡️ Passage au fichier suivant : {next_path}")

        return {
            "current_file_index": next_index,
            "current_file_path": next_path,
            "iteration_count": 0,
            "test_results": {}, # IMPORTANT : Réinitialiser pour le prochain fichier
            "status": "STARTING_NEXT"
        }

        

    workflow.add_node("next_file_processor", next_file_node)




    # Edges

    workflow.set_entry_point("manager")



    workflow.add_conditional_edges(

        "manager",

        manager_router,

        {

            "auditor": "auditor",
            END: END
            

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