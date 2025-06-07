from typing import TypedDict
from langgraph.graph import StateGraph,END
from langchain_core.runnables import RunnableLambda
from tools.diagnostics_tool import ai_indoor_farming
from tools.sysmptom_checker import check_symptom


class DiagnosticState(TypedDict):
    plantType:str
    plantCondition : str
    symptom_area: str
    
def build_graph():
    graph = StateGraph(DiagnosticState)
    
    def symptom_step(state):
        return {
                "plantType":state["plantType"],
                "plantCondition" : check_symptom.invoke(state["plantType"]),
                "symptom_area": state.get("diagnosis","")
        }
    
    graph.add_node("symptomcheck",RunnableLambda(symptom_step))
    
    
    def diagnosis_step(state):
        return {
                "plantType":state["plantType"],
                "plantCondition" : state['symptom_area'],
                "symptom_area":ai_indoor_farming.invoke(state['plantType'])
        }
        
        
    graph.add_node("Aidiagnosis" , RunnableLambda(diagnosis_step))
    
    
    graph.set_entry_point("symptomcheck")
    graph.add_edge("symptomcheck","Aidiagnosis")
    graph.add_edge("Aidiagnosis",END)
    
    return graph.compile()