from fastapi import FastAPI, File, UploadFile, Request
from fastapi.templating import Jinja2Templates
import tensorflow as tf
import numpy as np
from PIL import Image

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Load the SavedModel
model = tf.saved_model.load("saved_model")

# Define the prediction function
@tf.function(input_signature=[tf.TensorSpec(shape=[None, 224, 224, 3], dtype=tf.float32)])
def predict_fn(images):
    return model(images)

# Preprocess the image
def preprocess_image(image):
    img = Image.open(image.file)
    img = img.resize((224, 224))  # Resize the image
    img_array = np.array(img)
    img_array = img_array / 255.0  # Normalize the image
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# Define endpoint to serve HTML page

# Define endpoint to receive image input and return prediction
@app.post("/")
async def predict_image(request: Request, file: UploadFile = File(...)):
    # Preprocess the image
    img_array = preprocess_image(file)
    
    # Make predictions
    prediction = predict_fn(img_array)
    class_names = ['Inorganic', 'Organic', 'Metal']
    predicted_class = class_names[np.argmax(prediction[0])]

    return templates.TemplateResponse("index.html", {"request": request, "predicted_class": predicted_class})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
