from fastapi import FastAPI, Path
import json
import pandas as pd

app = FastAPI()
dataset = pd.read_csv("dataset/vgsales.csv")

print(dataset.loc[dataset["id"]==3].to_json(orient="records"))

@app.get("/")
async def home():
    return {"status":"Online"}


@app.get("/item_id/{id}")
async def get_item (id: int = Path(None, gt=0, lt=16601)):
    data = dataset.loc[dataset["id"] == id]
    data = data.to_json(orient="records")
    jsn = json.loads(data)
    return jsn


@app.get("/dataset")
async def get_all_dataset():
    data = dataset.to_json(orient="records")
    parsed = json.loads(data)
    return(parsed)