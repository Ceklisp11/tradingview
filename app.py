from flask import Flask, request, jsonify

app = Flask(__name__)

# Webhook endpoint to receive POST requests
@app.route('/webhook', methods=['POST'])
def webhook():
    # Check if the request contains JSON data
    if request.is_json:
        data = request.get_json()
        
        # Log the received data (optional)
        print("Received webhook data:", data)

        # Process the data (you can add your own logic here)
        # For example, retrieve specific fields
        event_type = data.get("event_type", "Unknown")
        user_id = data.get("user", {}).get("id", "N/A")
        
        # Respond to the sender
        return jsonify({"status": "success", "message": f"Received event '{event_type}' for user {user_id}"}), 200
    else:
        # Handle non-JSON data
        return jsonify({"status": "error", "message": "Invalid data format. JSON expected."}), 400

# Run the Flask app
if __name__ == '__main__':
    app.run(port=8080)
