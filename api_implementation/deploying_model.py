from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json
import uvicorn
from pyngrok import ngrok
from fastapi.middleware.cors import CORSMiddleware
import nest_asyncio

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class model_input(BaseModel):
    
    Compactness_Index:int
    Overall_Height:int
    Glazing_Area     : int
        
#loading the saved model 
energy_model=pickle.load(open("energy_model.sav","rb"))

@app.post('/predict_loads')
def load_prediction(input_parameters : model_input):
    
    input_data = input_parameters.json() #apiye gelen verinin tipi model_input.
    #bu pydantic basemodel dan türetilmiş bir sınıftır.bunu jsona çeviriyoruz
    input_dictionary = json.loads(input_data)
    
    compactness = input_dictionary['Compactness_Index']
    height = input_dictionary['Overall_Height']
    glazing = input_dictionary['Glazing_Area']
  
    
    
    input_list = [compactness,height,glazing]
    
    prediction = energy_model.predict([input_list])
    
    return prediction


ngrok.set_auth_token("38iVcDD39e0m6Hw90HrVfyptS9Y_4Yrbje2buVmHqvx2n4P2i") #kendi hesabının tokenini tanıtıyorsun. yani ngrok calısırken senin hesabına baglanıyor. dısarıdan herkes baglanamıyor

ngrok_tunnel = ngrok.connect(8000) #local host olarak fastapi 8000 portunu kullanıyor ngrok da internete açıyor. o yüzden önce bir bilgisayarda local olarak 8000 portunda acıyoruz
#ngrok var olan serverı dış dünyaya açar
print('Public URL:', ngrok_tunnel.public_url)