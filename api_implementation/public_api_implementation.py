import json
import requests

url="https://calciferous-makeda-nonbotanically.ngrok-free.dev/predict_loads"
input_data_for_model = {
    
    "Compactness_Index":345,
    "Overall_Height":456,
    "Glazing_Area"     : 543
    
    }



response = requests.post(url, json=input_data_for_model)

print(response.json())