import streamlit as st
import numpy as np
import pandas as pd
from numpy import savetxt
from PIL import Image, ImageOps
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.image import smart_resize

#@st.cache(allow_output_mutation=True)
model = tf.keras.models.load_model('models/real_model.h5')

st.title('Is it a hot dog?')
st.subheader('Upload your image and we will tell you if we think it is a hot dog!!!')

st.write("""
         # Image Classification
         """
         )

file = st.file_uploader("Upload the image to be classified U0001F447", type=["jpg", "png", "jpeg"])
st.set_option('deprecation.showfileUploaderEncoding', False)

def upload_predict(upload_image, model):
        # reshape Image:
    test_img = smart_resize(upload_image, (256,256))
    # add 4th dimension:
    test_image = np.expand_dims(test_img, axis = 0)   
    prediction = model.predict(test_image)    
    return prediction[0,0]
if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    predictions = upload_predict(image, model)
    if predictions > 0.70:
         st.write(f"We are {round(predictions* 100)}% sure this image contains a hot dog")
    elif predictions < 0.70 and predictions > 0.50:
        st.write(f"We are not sure but we feel {round(predictions * 100)}% sure this image contains a hot dog")
    elif predictions < 0.50 and predictions > 0.30:
        st.write(f"We are not sure but we feel {round((1 - predictions) * 100)}% sure this image does not contain a hot dog")
    else:
        st.write(f"We are {round((1 - predictions) * 100)}% sure this image does not contain a hot dog")
