from flask import Flask, jsonify, send_file
from datetime import datetime
import logging
from utils import get_team_info

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("backend-service")

@app.route("/")
def home():
    logger.info("Home endpoint accessed")
    return jsonify({
        "message": "Backend Running Successfully",
        "service": "Dockerized Flask Backend",
        "status": "OK",
        "timestamp": datetime.utcnow().isoformat()
    })

@app.route("/image")
def image():
    logger.info("Image endpoint accessed")
    return send_file("myimage.jpg", mimetype="image/jpeg")

@app.route("/health")
def health():
    logger.info("Health check endpoint accessed")
    return jsonify({"status": "healthy", "uptime": "OK"})

@app.route("/team")
def team():
    logger.info("Team endpoint accessed")
    return jsonify(get_team_info())

@app.route("/project")
def project_details():
    logger.info("Project details endpoint accessed")
    return jsonify({
        "project_name": "DevOps Final Project",
        "description": "A Docker-based microservices application by Prasad & Tarun.",
        "technologies": ["Flask", "Docker", "Nginx", "Python"],
        "version": "1.0.0"
    })

if __name__ == "__main__":
    logger.info("Starting backend Flask server...")
    app.run(host="0.0.0.0", port=5000)
