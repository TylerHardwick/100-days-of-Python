import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

questions_response = requests.get(url="https://opentdb.com/api.php", params=parameters)
questions_response.raise_for_status()
question_data = questions_response.json()["results"]

