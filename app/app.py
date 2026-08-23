from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Contoso Retail - Application running on Azure Kubernetes Service. Containerized Flask application."

@app.route("/health")
def health():
    return jsonify(status="healthy")

@app.route("/api")
def api():
    return jsonify(
        application="Contoso Retail",
        platform="Azure Kubernetes Service",
        version="v1"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
