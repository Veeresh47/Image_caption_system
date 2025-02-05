from flask import Flask, render_template, request, redirect, url_for, flash
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import os

app = Flask(__name__)

# Configure Flask app and upload folder
UPLOAD_FOLDER = "static/uploads"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.secret_key = "your_secret_key"  # for flash messages

# Create the upload folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Load the BLIP model for image captioning
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Helper function to check allowed file types
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def home():
    caption = None
    image_path = None

    if request.method == "POST":
        # Check if the file part is in the request
        if "image" not in request.files:
            flash("No file part", "danger")
            return redirect(request.url)

        file = request.files["image"]

        # If no file is selected
        if file.filename == "":
            flash("No file selected", "danger")
            return redirect(request.url)

        # Check if the file is allowed
        if not allowed_file(file.filename):
            flash("File type not allowed. Please upload an image file.", "danger")
            return redirect(request.url)

        # Save the image to the server
        image_filename = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(image_filename)

        # Open and process the image
        try:
            image = Image.open(image_filename).convert("RGB")
        except Exception as e:
            flash(f"Error processing image: {str(e)}", "danger")
            return redirect(request.url)

        # Generate caption
        inputs = processor(image, return_tensors="pt")
        output = model.generate(**inputs)
        caption = processor.decode(output[0], skip_special_tokens=True)

        image_path = url_for('static', filename=f"uploads/{file.filename}")

    return render_template("index.html", caption=caption, image_path=image_path)

if __name__ == "__main__":
    app.run(debug=True)
