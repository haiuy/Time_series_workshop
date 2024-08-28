from fastapi import FastAPI
import joblib
import numpy as np
#Load model
model = joblib.load('app/model.joblib')
#Create an app using FastAPI
app = FastAPI()
@app.get('/')
def reed__root():
    return {'message': 'Bitcoin return model API'}
#Make a function to send data to the model and get the prediction
@app.post('/predict')
def predict(data: dict):
    """Predict the next day return of a given set of features.
        Args:
            data (dict): a dictionary containing the features
        Returns:
            a dictionary contains the predicted value"""
    features = np.array(data['features']).reshape(1, -1)
    predictions = model.predict(features)
    prediction_list = predictions.tolist()
    return {'predicted_next_day_return': prediction_list}
