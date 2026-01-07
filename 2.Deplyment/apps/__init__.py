from flask import Flask, render_template, request
from apps.routes import predict_survival

app = Flask(__name__)


fare_range = range(1,301)
age_range = range(1, 101)
family_size_range = range(1, 12)

@app.route('/')
def home():
    return render_template(
        'home.html',
        fare_min=1, fare_max=300,
        age_min=1, age_max=100,
        family_min=1, family_max=11,
        result=None
    )

@app.route('/predict', methods= ['POST'])
def predict():
    Age = float(request.form.get('Age', 0))
    Fare = float(request.form.get('Fare', 0))
    Family_size = float(request.form.get('Family_size', 0))
    Embarked = request.form.get('Embarked', '')
    Sex = request.form.get('Sex', '')
    Pclass = request.form.get('Pclass', '')

    result = predict_survival(Pclass, Sex, Age, Fare, Embarked, Family_size)
    return render_template(
        'home.html',
        fare_min=1, fare_max=300,
        age_min=1, age_max=100,
        family_min=1, family_max=11,
        result=result
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)