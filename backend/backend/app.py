from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/report", methods=["POST"])
def submit_report():
    response = {
        "success": True,
        "message": "Cybercrime report submitted successfully",
        "data": {
            "tracking_id": "CR-001",
            "status": "Submitted"
        }
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
