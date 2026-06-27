from flask import Flask
import requests
import os

app = Flask(__name__)

BACKEND_URL = os.getenv("BACKEND_URL")
APP_TITLE = os.getenv("APP_TITLE")

@app.route("/")
def home():
    response = requests.get(BACKEND_URL)
    data = response.json()

    return f"""
    <h1>{APP_TITLE}</h1>

    <p><b>Backend Message:</b> {data["message"]}</p>

    <p><b>Version:</b> {data["version"]}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
