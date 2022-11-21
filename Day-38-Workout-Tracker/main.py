import requests
from datetime import datetime

# Body details:
GENDER = "male"
WEIGHT_KG = "(int) weight here"
HEIGHT_CM = " (float) height here"
AGE = "(int)age here"


APP_ID = "APP_ID"
API_KEY = "API_KEY"
SHEETY_TOKEN = "SHEETY_AUTH_TOKEN"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_parameters = {
    "query": input("So what did you do?: \n"),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
exercise_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_endpoint_response = requests.post(url=exercise_endpoint, json=exercise_parameters, headers=exercise_headers)
result = exercise_endpoint_response.json()

today = datetime.today()
current_date = today.strftime("%d/%m/%Y")
current_time = today.strftime("%H:%M:%S")

sheety_endpoint = "https://api.sheety.co/USER_HERE/workoutTracking/workouts"
sheety_headers = {
    "Authorization": SHEETY_TOKEN
}
for exercise in result["exercises"]:
    sheety_parameters = {
        "workout": {
         "date": current_date,
         "time": current_time,
         "exercise": exercise["name"].title(),
         "duration": round(exercise["duration_min"]),
         "calories": round(exercise["nf_calories"]),
        }
    }
    sheety_post = requests.post(url=sheety_endpoint, json=sheety_parameters, headers=sheety_headers)

print("Spreadsheet updated")

