import numpy as np
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)       # __name__ - gets the name of the current variable, 

# Loading the saved models 

model = joblib.load('titanic_rf_model.joblib')
scaler = joblib.load('titanic_scaler.joblib')

# define the prediction endpoint

@app.route('/predict', methods=['POST'])

def predict():
    
    """
        Fuction to handle prediction requests.
        It expects a JSON payload with passenger data
    """

    # preprocessing the input data

    data = request.get_json()

    pclass = data['pclass']
    sex = 0 if data['sex'] == 'female' else 1

    age = data['age']
    fare = data['fare']
    parch = data['parch']


    input_features = np.array([[pclass, sex, age, fare, parch]])

    input_features_scaled = scaler.transform(input_features)        # scale the input data

    prediction_raw = model.predict(input_features_scaled)

    prediction_text = 'Survived' if prediction_raw[0] == 1 else 'Did not Survived!'

    return jsonify({'prediction': prediction_text})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)



