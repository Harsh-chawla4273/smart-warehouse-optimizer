from flask import Flask, request
import subprocess
import threading
import os

app = Flask(__name__)

# Scaler ka bot jab reset maangega, ye use "OK" bol dega
@app.route('/reset', methods=['POST'])
def reset():
    return "OK", 200

# Health check ke liye
@app.route('/')
def home():
    return "Environment is Running", 200

def run_streamlit():
    # Aapka purana dashboard side mein chalta rahega
    os.system("streamlit run app.py --server.port 8501 --server.address 0.0.0.0")

if __name__ == "__main__":
    # Streamlit ko background mein chalao
    threading.Thread(target=run_streamlit).start()
    # Flask ko main port par chalao jo Scaler check karta hai
    app.run(host='0.0.0.0', port=7860)
