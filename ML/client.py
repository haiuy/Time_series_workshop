#Automate Inferance
import json
import requests

data = [[64333.542969, 1.882768e+10, 0.018053, 0.014010, 0.026733],
        [64178.992188, 2.143059e+10, 0.013952, 0.011276, 0.028999],
        [64094.355469, 4.253051e+10, 0.073014, 0.012506, 0.028688],
        [60381.914062, 2.762573e+10, 0.026280, 0.007034, 0.020180],
        [61175.191406, 3.273115e+10, 0.049908, 0.006023, 0.021483]]
url = 'http://localhost:8000/predict/'
#Create a list to store the predictions
#Send the data as json format to the server and get the predictions by requests
predictions = []
for record in data:
    payload = {'features': record}
    payload = json.dumps(payload)
    response = requests.post(url, data=payload)
    predictions.append(response.json()['predicted_next_day_return'])

#Run code with interactive window
print(predictions)