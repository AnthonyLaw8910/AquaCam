from flask import Flask, request, jsonify

app = Flask(__name__)

# Route to return student number
@app.route('/')
def home():
    return jsonify({"student_number": "200599082"})

# Webhook route for Dialogflow fulfillment
@app.route('/webhook', methods=["POST"])
def webhook():
    req = request.get_json(silent=True, force=True)

    # Extract intent name
    intent_name = req.get("queryResult", {}).get("intent", {}).get("displayName")

    # Response for weather_info intent

    if intent_name == "weather_info":
        response_text = "Today's weather is sunny with a high of 25°C."

    return jsonify({"fulfillmentText": response_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)