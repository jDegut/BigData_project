from fastapi import FastAPI
from scripts.utils import predict, load_pipeline, get_data_from_json

MODEL_FILENAME = "/artifacts/model.pickle"

app = FastAPI()
pipeline = load_pipeline(MODEL_FILENAME)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/predict")
async def predict(data: dict):
    """
    Predict model output with contact datas. (POST)
    :param data: data to predict (JSON)
    :return: predictions (JSON)
    """
    x = get_data_from_json(data)
    y_pred = predict(pipeline, x)
    return {"predictions": y_pred.tolist()}
