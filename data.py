import requests

# Parameters for Open Trivia DB API to provide 10 True / False questions
parameters = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get("https://opentdb.com/api.php", params=parameters)  # Fetch the question data from Open Trivia DB API
response.raise_for_status()  # Raise an exception for any errors
data = response.json()
question_data = data["results"]  # The question data in JSON format
