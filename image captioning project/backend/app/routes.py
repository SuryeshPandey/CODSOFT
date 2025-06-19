from flask import Flask, request, jsonify
from flask_cors import CORS  # ✅ Import CORS
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

app = Flask(__name__)
CORS(app)  # ✅ Enable CORS

# Load BLIP model and processor once
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

@app.route("/api/caption", methods=["POST"])
def caption_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400

    try:
        image_file = request.files["image"]
        image = Image.open(image_file).convert('RGB')

        inputs = processor(images=image, return_tensors="pt")
        output = model.generate(**inputs)
        caption = processor.decode(output[0], skip_special_tokens=True)

        print("✅ Caption generated:", caption)
        return jsonify({"caption": caption}), 200

    except Exception as e:
        print("❌ Error generating caption:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
