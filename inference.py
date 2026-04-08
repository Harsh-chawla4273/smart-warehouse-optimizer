from flask import Flask, request, jsonify
import threading
import os

app = Flask(__name__)

# --- SCALER BOT KI PASANDIDAH LINE ---
@app.route('/reset', methods=['POST'])
def reset():
    return "OK", 200

@app.route('/state', methods=['GET'])
def state():
    return jsonify({"status": "running"}), 200

# --- TUMHARA LOGIC ---
def run_inference():
    print("Inference engine active...")

if __name__ == "__main__":
    # Flask ko port 7860 par chalao (Hugging Face default)
    app.run(host='0.0.0.0', port=7860)
