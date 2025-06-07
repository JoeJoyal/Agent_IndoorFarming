from langchain.tools import tool


@tool
def check_symptom(symptom):
    """this tool will analyze the input symptom text and return the relevant Indoor-farming catagories"""
    symptom = symptom.lower()
    
    if "nursery plant" in symptom or "mature plant" in symptom or "die" in symptom:
        return "healthy"
    elif "disease" in symptom or "turn-yellowing" in symptom :
        return "lighting issues"
    elif "Irregular Yellow Spots" in symptom or "Leaf Deformitieszzy" in symptom:
        return "fungicide"
    elif "Whole Plant Yellowing" in symptom or "Semi-Yellowing" in symptom:
        return "temperature issue"
    else:
        return "general examination is required "