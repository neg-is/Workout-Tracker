import requests
from datetime import datetime

GENDER = "your gender"
WEIGHT_KG = "your weight"
HEIGHT_CM = "your heigth"
AGE = "your age"

API_KEY = "your api key from nutritionix.com"
API_ID = "your api id from nutritionix.com"

SHEETY_USERNAME = "your username for sheety"
SHEETY_PASSWORD = "your password for sheety"

exercise_endpoint = "your nutritionix.com url"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-key": API_KEY,
    "x-app-id": API_ID
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

#today's date
today = datetime.now()
today_date = today.strftime("%Y%m%d")
print(today_date)
#current hour
now_time = today.strftime("%H:%M:%S")
print(now_time)

sheet_endpoint = "your sheety url"

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
# #No Authentication
# sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

# print(sheet_response.text)

#Basic Authentication
sheet_response = requests.post(
    sheet_endpoint,
    json=sheet_inputs,
    auth=(
        SHEETY_USERNAME,
        SHEETY_PASSWORD,
        )
    )
print("Basic Auth:", sheet_response.text)


