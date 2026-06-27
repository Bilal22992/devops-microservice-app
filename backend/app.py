from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():

    api_loaded = "Yes" if os.getenv("API_KEY") else "No"

    return {
        "message": "Hello from Backend!",
        "version": "1.0",
        "api_key_loaded": api_loaded
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
