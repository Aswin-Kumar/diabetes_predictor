import os
from flask import Flask, request, jsonify, send_from_directory
from predict_model import predict_diabetes

BASE = os.path.dirname(__file__)
FRONTEND_DIR = os.path.abspath(os.path.join(BASE, "..", "frontend"))

app = Flask(__name__, static_folder=FRONTEND_DIR, static_url_path="")

@app.route("/")
def index():
    return send_from_directory(FRONTEND_DIR, "index.html")

@app.route("/api/predict", methods=["POST"])
def api_predict():
    data = request.get_json()
    if not data or "inputs" not in data:
        return jsonify({"error": "No input provided"}), 400

    try:
        values = [float(v) for v in data["inputs"]]
        if len(values) != 8:
            return jsonify({"error": "Exactly 8 numeric values required"}), 400
        result = predict_diabetes(values)
        return jsonify({"prediction": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("✅ Flask server started at http://127.0.0.1:5000")
    app.run(debug=True)

