# app.py
from flask import Flask, request, jsonify
import cases
import base64

app = Flask(__name__)
def process_image(base64_image):
    print("Received Base64 Image Length:", len(base64_image))
    
    return {
        "message": "Image processed successfully",
        "size": len(base64_image)
    }
    
@app.route('/upload', methods=['POST'])
def upload():

    text = request.form.get("text")

    if not text:
        return jsonify({"error": "Text is required"}), 400

    if 'image' in request.files:

        image = request.files['image']

        if image.filename != "":
            image_path = "new_image.jpeg"

            image.save(image_path)

    result = cases.cases(text)

    return jsonify({
        "status": "success",
        "text": text,
        "result": result
    })



    
@app.route('/process', methods=['POST'])
def process_text():
    try:
        data = request.get_json()
        if not data or 'text' not in data:
            return jsonify({"error": "No text provided"}), 400
        
        user_text = data['text'].lower()
        
        response = cases.cases(user_text)
        
        return jsonify({"response": response})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
