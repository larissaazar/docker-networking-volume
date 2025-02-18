import requests
import time

DATA_SOURCE = "http://producer:5000/data"
FILE_PATH = "/data/logs.txt"

while True:
    try:
        response = requests.get(DATA_SOURCE)
        data = response.text

        # Append data to file in volume
        with open(FILE_PATH, "a") as file:
            file.write(data + "\n")
        
        print(f"Stored data: {data}")

    except Exception as e:
        print(f"Error: {e}")

    time.sleep(5)  # Fetch data every 5 seconds
