from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "API is running"


@app.route("/lookup")
def lookup():
    number = request.args.get("num", "")

    if not number.isdigit() or len(number) != 10:
        return jsonify({
            "ok": False,
            "error": "10 digit number required"
        }), 400

    # Demo response only.
    # Yahan sirf apna/authorized data process karein.
    return jsonify({
        "ok": True,
        "number": number,
        "message": "Demo API response"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
