import joblib
import numpy as np
import pandas as pd

model = joblib.load('/media/prince/5A4E832F4E83034D/TItanic Project/2.Deplyment/Titanic_survival0.pkl')
pipeline = joblib.load('/media/prince/5A4E832F4E83034D/TItanic Project/2.Deplyment/titanic_pipeline0.pkl')


def predict_survival():
    pass