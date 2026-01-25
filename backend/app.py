from flask import Flask, jsonify

# Initialize Flask application
app = Flask(__name__)

# API endpoint to submit a cybercrime report
@app.route("/api/report", methods=["POST"])
def submit_report():
    # Mock response to simulate successful report submission
    response = {
        "success": True,
        "message": "Cybercrime report submitted successfully",
        "data": {
            "tracking_id": "CR-001",
            "status": "Submitted"
        }
    }
    return jsonify(response)

# Run the application in debug mode
if __name__ == "__main__":
    app.run(debug=True)
