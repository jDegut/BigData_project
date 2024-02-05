import pickle

import pandas as pd
from sklearn.pipeline import Pipeline

RANDOM_STATE = 1


def load_pipeline(filename: str):
    """
    Load a pipeline from a file.
    :param filename: as a string
    :return: pipeline
    """
    with open(filename, 'rb') as f:
        return pickle.load(f)


def get_data_from_json(data: dict):
    """
    Get data from a JSON.
    :param data:
    :return: data as a DataFrame
    """
    return pd.DataFrame(data, index=[0])


def predict(model: Pipeline, x):
    """
    Predict the output of a model (pipeline).
    :param model: loaded pipeline
    :param x: data to predict
    :return: predictions
    """
    return model.predict(x)
