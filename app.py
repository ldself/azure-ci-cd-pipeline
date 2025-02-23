from flask import Flask, request, jsonify
from flask.logging import create_logger
import logging

import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

def scale(payload):
    """Scales Payload"""

    LOG.info(f"Scaling Payload: {payload}")
    scaler = StandardScaler().fit(payload)
    scaled_adhoc_predict = scaler.transform(payload)
    return scaled_adhoc_predict

@app.route("/")
def home():
    html = "<h3>Sklearn Prediction Home</h3>"
    return html.format(format)

@app.route("/predict", methods=['POST'])
def predict():
    # Performs an sklearn prediction
    try:
        # Load pretrained model as clf. Try any one model. 
        clf = joblib.load("./Housing_price_model/LinearRegression.joblib")
        # clf = joblib.load("./Housing_price_model/StochasticGradientDescent.joblib")
        # clf = joblib.load("./Housing_price_model/GradientBoostingRegressor.joblib")
    except:
        LOG.info(f"JSON payload: {json_payload}")
        return "Model not loaded"

    json_payload = request.json
    LOG.info(f"JSON payload: {json_payload}")
    inference_payload = pd.DataFrame(json_payload)
    LOG.info(f"inference payload DataFrame: {inference_payload}")
    scaled_payload = scale(inference_payload)
    prediction = list(clf.predict(scaled_payload))
    prediction_output = [f"{p:.6f}" for p in prediction]
    LOG.info(f"Prediction: {prediction_output}")
    return jsonify({'prediction': prediction})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
