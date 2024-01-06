import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
import numpy as np
from bardapi import Bard

token = 'xxxxxxxxxxxx'
bard = Bard(token=token)

model = keras.models.load_model('aqidl.h5')
def post(photo):

    img_path = photo  
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    
    predictions = model.predict(img_array)
    
    predicted_index = np.argmax(predictions)
    print(predictions)
    print(f"Predicted Index: {predicted_index}")
    if predicted_index == 0:
        return "The AQI is 0-50, the air quality is good\n"+bard.get_answer("The air quality is Good, AQI ranges from 0-50, give instructions for public and workers when going outside, dont give the text in bold and dont say anything, just give instructions in bullet points")['content']
    elif predicted_index == 1:
        return "The AQI is 50-100, the air quality is Moderate\n"+bard.get_answer("The air quality is Moderate, AQI ranges from 51-100, give instructions for public and workers when going outside, dont give the text in bold and dont say anything, just give instructions in bullet points")['content']
    elif predicted_index == 2:
        return "The AQI is 101-150, the air quality is Unhealthy for severe groups\n"+bard.get_answer("The air quality is Unhealthy for sensitive groups, AQI ranges from 101-150, give instructions for public and workers when going outside, dont give the text in bold and dont say anything, just give instructions in bullet points")['content']
    elif predicted_index == 3:
        return "The AQI is 151-200, the air quality is unhealthy\n"+bard.get_answer("The air quality is Unhealthy, AQI ranges from 151-200, give instructions for public and workers when going outside, dont give the text in bold and dont say anything, just give instructions in bullet points")['content']
    elif predicted_index == 4:
        return "The AQI is 201-300, the air quality is very unhealthy\n"+bard.get_answer("The air quality is Very Unhealthy, AQI ranges from 201-300, give instructions for public and workers when going outside, dont give the text in bold and dont say anything, just give instructions in bullet points")['content']
    elif predicted_index == 5:
        return "The AQI is 301-500, the air quality is hazardous\n"+bard.get_answer("The air quality is Hazardous, AQI ranges from 301-500, give instructions for public and workers when going outside, dont give the text in bold and dont say anything, just give instructions in bullet points")['content']
    