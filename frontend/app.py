from flask import Flask
import requests

app = Flask(__name__)

BACKEND_URL = "http://backend:5001"

@app.route("/")
def home():
    response = requests.get(BACKEND_URL)
    data = response.json()

    return f"""
    <h1>Simple DevOps Demo</h1>

    <p><b>Backend Message:</b> {data["message"]}</p>
    <p><b>Version:</b> {data["version"]}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
