AI Image Caption Generator

This is a simple AI-powered web application that generates captions for uploaded images using the **BLIP (Bootstrapped Language-Image Pretraining) model** from **Hugging Face**.  

Features 
✅ Upload an image and get an AI-generated caption  
✅ Uses the Salesforce/BLIP model for accurate caption generation  
✅ User-friendly interface with Bootstrap styling  
✅ Error handling for invalid files and unsupported formats  
✅ Flask-based backend for lightweight deployment  

## **Tech Stack**  
- **Frontend**: HTML, CSS (Bootstrap), JavaScript  
- **Backend**: Flask (Python)  
- **AI Model**: BLIP (Salesforce/blip-image-captioning-base)  
- **Image Processing**: Pillow (PIL)  


### **2. Create a Virtual Environment (Optional but Recommended)**  
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### **3. Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **4. Run the Application**  
```bash
python app.py
```
Visit **http://127.0.0.1:5000/** in your browser to use the application.

## **Project Structure**  
```
AI-Image-Caption-Generator/
│── static/
│   ├── uploads/         # Stores uploaded images
│── templates/
│   ├── index.html       # Frontend UI
│── app.py               # Flask application
│── requirements.txt      # Required dependencies
│── README.md            # Project documentation
```

## **Requirements (requirements.txt)**  

Flask
transformers
torch
Pillow

## **Future Enhancements**  
- Add support for multiple image captions  
- Implement GPU acceleration for faster inference  
- Improve UI with real-time progress updates  

## **Contributing**  
Pull requests are welcome! Feel free to fork the repository and suggest improvements.  

