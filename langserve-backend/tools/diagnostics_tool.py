from langchain.tools import tool 
from utils.euri_client import euri_chat_completion



@tool
def ai_indoor_farming(farming_description):
    """use EURI AI model to provide the vertical indoor-farming suggestion based on the plant condition and symptom given by users"""
    
    message = [{"role":"user","content":f"a farming reports : {farming_description} .what are the possible indoor-farming and variety of plants healthy, disease, die and even suggest me cure for this "}]
    
    return euri_chat_completion(messages=message)