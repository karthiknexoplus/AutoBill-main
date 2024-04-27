import requests
import json
import time
import random

# List of product names
products = ["apple", "banana", "coke", "lays", "orange"]

# URL of the Flask server
url = 'http://192.168.87.224:5000/'

while True:
    # Generate random sample data
    data_dict = {
        "id": random.randint(100, 999),
        "name": random.choice(products),  # Choose a random product name
        "price": round(random.uniform(1.0, 100.0), 2),
        "units": "units",
        "taken": random.randint(1, 1000),  # Weight in grams
        "payable": round(random.uniform(1.0, 100.0), 2)
    }

    # Convert data to JSON
    data_json = json.dumps(data_dict)
    print(data_json)

    # Post data to Flask server
    response = requests.post(url, data={'data': data_json})

    # Print response status code
    print("Response Status Code:", response.status_code)

    # Wait for a while before sending the next sample data
    time.sleep(random.uniform(5, 5))  # You can adjust the sleep time interval as needed
