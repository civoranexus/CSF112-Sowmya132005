from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/report", methods=["POST"])
def submit_report():
    return jsonify({
        "tracking_id": "CR-001",
        "status": "Report submitted successfully"
    })

if __name__ == "__main__":
    app.run(debug=True)
