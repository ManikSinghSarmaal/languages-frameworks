import tensorflow as tf

# Load the SavedModel
model = tf.saved_model.load("saved_model")

# Define the prediction function
@tf.function(input_signature=[tf.TensorSpec(shape=[None, 224, 224, 3], dtype=tf.float32)])
def predict_fn(images):
    return model(images)

# Preprocess the image
def preprocess_image(image_path):
    image = tf.io.read_file(image_path)
    image = tf.image.decode_image(image, channels=3)
    image = tf.image.resize(image, [224, 224])
    image = tf.expand_dims(image, axis=0)
    image = image / 255.0  # Normalize
    return image

# Make predictions
image_path = "/Users/maniksinghsarmaal/Downloads/burger.jpeg"
custom_image = preprocess_image(image_path)
prediction = predict_fn(custom_image)
class_names = ['Inorganic', 'Organic', 'Metal']
predicted_class = class_names[tf.argmax(prediction[0])]
print(f'The class of the feed input image is: {predicted_class}')
