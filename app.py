import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Streamlit settings
st.set_page_config(page_title='One Piece Character Classifier', page_icon='🍖')

# Load the SavedModel
@st.cache_resource
def load_model():
    return tf.saved_model.load("saved_model/1")

model = load_model()

# List of all the classes
class_names = ['Ace', 'Akainu', 'Brook', 'Chopper', 'Crocodile', 'Franky', 'Jinbei', 'Kurohige', 'Law', 'Luffy', 'Mihawk', 'Nami', 'Rayleigh', 'Robin', 'Sanji', 'Shanks', 'Usopp', 'Zoro']

def preprocess_image(image):
    img = image.resize((224, 224))  # Adjust size according to your model's input
    img_array = tf.keras.utils.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

st.title("One Piece Character Classifier")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Preprocess the image
    img = preprocess_image(image)

    # Use the loaded model to make a prediction
    predictions = model.signatures["serving_default"](tf.constant(img, dtype=tf.float32))

    # Extract the prediction probabilities
    predictions_array = predictions["final_output"].numpy()

    # Get the predicted class
    predicted_class_index = np.argmax(predictions_array[0])
    predicted_class_name = class_names[predicted_class_index]

    st.write(f"**The predicted class is:** {predicted_class_name}")

    # Create a bar chart of probabilities
    st.bar_chart(dict(zip(class_names, predictions_array[0])))