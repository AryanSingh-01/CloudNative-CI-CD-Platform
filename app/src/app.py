from flask import Flask, jsonify

app = Flask(__name__)
APP_VERSION = "v1.0.0"

@app.route("/")
def home():
    return f"""
    <h1>CloudNative CI/CD Platform</h1>
    <p>Status: Deployed successfully via automated CI/CD pipeline</p>
    <p>App Version: {APP_VERSION}</p>
    """

@app.route("/health")
def health():
    return jsonify(
        status="UP",
        service="cloudnative-ci-cd-platform"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

