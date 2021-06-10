from fastapi import FastAPI
import json
import pandas as pd

app = FastAPI()

@app.get("/")
async def home():
    return {"status":"Online"}

'''
@app.get("/{txt}")
async def str2json(txt:str):
    jsn = json.loads(txt)
    return jsn
'''

@app.get("/dataset")
async def get_all_dataset():
    dataset = pd.read_csv("dataset/Caturtunggal_Harian_all.csv")
    #dataset.sort_values(by=["precipMM"], inplace=True)
    dataset = dataset.to_json(orient="records")
    parsed = json.loads(dataset)
    return(parsed)