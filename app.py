# app.py
from flask import Flask, request, jsonify
import cases
import os

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_text():
    try:
        data = request.get_json()
        if not data or 'text' not in data:
            return jsonify({"error": "No text provided"}), 400
        
        user_text = data['text'].lower()
        
        # Process the text using your cases module
        response = cases.cases(user_text)
        
        # Return the response as JSON
        return jsonify({"response": response})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
