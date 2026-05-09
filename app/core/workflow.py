from langgraph.graph import StateGraph
from typing import TypedDict

class GraphState(TypedDict):
    query: str
    retrieved_chunks: list
    summary: str


def create_workflow(retrieval_agent, summary_agent):

    workflow = StateGraph(GraphState)

   
    # RETRIEVE NOD

    def retrieve(state):

        query = state.get("query", "")

        results = retrieval_agent.retrieve(query)

        return {
            "query": query,
            "retrieved_chunks": results
        }

   
    # SUMMARIZE NODE
 
    def summarize(state):

        summary = summary_agent.summarize(
            state.get("query", ""),
            state.get("retrieved_chunks", [])
        )

        return {
            "query": state.get("query", ""),
            "retrieved_chunks": state.get("retrieved_chunks", []),
            "summary": summary
        }

    # Nodes
    workflow.add_node("retrieve", retrieve)
    workflow.add_node("summarize", summarize)

    # Flow
    workflow.set_entry_point("retrieve")
    workflow.add_edge("retrieve", "summarize")
    workflow.set_finish_point("summarize")

    return workflow.compile()