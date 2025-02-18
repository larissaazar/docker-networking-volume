from flask import Flask
import random
import time

app = Flask(__name__)

@app.route('/data')
def generate_data():
    """Generates random numbers as data."""
    return str(random.randint(1, 100))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
