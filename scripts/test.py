import pandas as pd


def analyse_csv(file_path):
    # Charger le fichier CSV dans un DataFrame pandas
    df = pd.read_csv(file_path, sep=";")

    # Initialiser un dictionnaire pour stocker les résultats
    res = {}

    # Itérer sur chaque colonne pour calculer min et max
    for column in df.columns:
        min_val = df[column].min()
        max_val = df[column].max()
        res[column] = {'min': min_val, 'max': max_val}

    return res


f = '../data/credit_scoring.csv'


results = analyse_csv(f)
for col, values in results.items():
    print(f"{col}: Min = {values['min']}, Max = {values['max']}")