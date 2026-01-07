import joblib
import numpy as np
import pandas as pd

model = joblib.load('/media/prince/5A4E832F4E83034D/TItanic Project/2.Deplyment/Titanic_survival0.pkl')
pipeline = joblib.load('/media/prince/5A4E832F4E83034D/TItanic Project/2.Deplyment/titanic_pipeline0.pkl')



def predict_survival(Pclass, Sex, Age, Fare, Embarked, Family_size):
    data = pd.DataFrame({
        'Pclass': [Pclass],
        'Sex':[Sex],
        'Age':[Age],
        'Fare':[Fare],
        'Embarked':[Embarked],
        'Family_size':[Family_size]
    })

    transformed = pipeline.transform(data)
    if hasattr(transformed, "toarray"):
        transformed = transformed.toarray()
    transformed = np.array(transformed, dtype=float).reshape(1, -1)

    prediction = model.predict(transformed)
    return float(np.ravel(prediction)[0])

