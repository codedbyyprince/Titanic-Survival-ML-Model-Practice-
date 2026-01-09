import joblib
import numpy as np
import pandas as pd
from huggingface_hub import hf_hub_download

MODEL_REPO = "mlwithprince/Titanic-Survival_predictor"
MODEL_PATH = hf_hub_download(repo_id=MODEL_REPO, filename='Titanic_survival.pkl')

model = joblib.load(MODEL_PATH)


def predict_survival(Pclass, Sex, Age, Fare, Embarked, Family_size):
    data = pd.DataFrame({
        'Pclass': [Pclass],
        'Sex':[Sex],
        'Age':[Age],
        'Fare':[Fare],
        'Embarked':[Embarked],
        'Family_size':[Family_size]
    })

    prediction = model.predict(data)
    return int(prediction[0])
