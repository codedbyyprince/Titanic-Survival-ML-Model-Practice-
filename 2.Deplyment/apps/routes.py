import joblib
import numpy as np
import pandas as pd

model = joblib.load('/media/prince/5A4E832F4E83034D/TItanic Project/2.Deplyment/Titanic_survival0.pkl')


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
