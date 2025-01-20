import streamlit as st
import numpy as np
from PIL import Image, ImageOps
import tensorflow as tf
from tensorflow.keras.preprocessing.image import smart_resize
from datetime import datetime

# Load the pre-trained model
@st.cache_resource
def load_model():
    """Load the TensorFlow model."""
    model = tf.keras.models.load_model('models/real_model.h5')
    return model

model = load_model()

# App title and description
st.title('🌭 Is it a Hot Dog?')
st.subheader('Upload an image, and we will tell you if we think it is a hot dog!')

# File uploader for image upload
file = st.file_uploader("Upload an image to classify", type=["jpg", "jpeg", "png"])

# Function to preprocess and predict
def upload_predict(upload_image, model):
    """Preprocess the image and predict using the model."""
    # Convert PIL image to NumPy array
    upload_image = np.array(upload_image)
    # Resize the image to the expected input shape
    test_img = smart_resize(upload_image, (256, 256))
    # Add batch dimension
    test_image = np.expand_dims(test_img, axis=0)
    # Normalize pixel values
    test_image = test_image / 255.0
    # Predict
    prediction = model.predict(test_image)
    return prediction[0, 0]

# Display logic
if file is None:
    st.text("Please upload an image file.")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True, caption="Uploaded Image")
    predictions = upload_predict(image, model)

    # Display the prediction result
    if predictions > 0.70:
        st.success(f"🌭 We are {round(predictions * 100)}% sure this image contains a hot dog!")
    elif 0.50 < predictions <= 0.70:
        st.info(f"🤔 We are somewhat sure (around {round(predictions * 100)}%) that this image contains a hot dog.")
    elif 0.30 < predictions <= 0.50:
        st.info(f"🤔 We are somewhat sure (around {round((1 - predictions) * 100)}%) that this image does NOT contain a hot dog.")
    else:
        st.error(f"🚫 We are {round((1 - predictions) * 100)}% sure this image does NOT contain a hot dog.")

# Timestamp footer
st.markdown(f"<small>Last run on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</small>", unsafe_allow_html=True)
