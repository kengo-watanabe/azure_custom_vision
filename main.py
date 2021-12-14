from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

from PIL import ImageDraw
from PIL import ImageFont
from PIL import Image

import os
import streamlit as st

import config
import detect_object
    
st.title('物体検出アプリ')

uploaded_file = st.file_uploader("choose an image . . . ", type='jpg')
if uploaded_file is not None:
    
    img = Image.open(uploaded_file.name)
    # Open local image file
    local_image = open(uploaded_file.name, "rb")
    
    # Call API with local image
    detect_objects_results_local = config.computervision_client.detect_objects_in_stream(local_image)
    
    print(detect_objects_results_local)

    # Print results of detection with bounding boxes
    print("Detecting objects in local image:")
    if len(detect_objects_results_local.objects) == 0:
        print("No objects detected.")
            
    img = Image.open(uploaded_file.name)       
    draw = ImageDraw.Draw(img)

    #検出した物体を矩形で囲む
    for object in detect_objects_results_local.objects:
        draw.rectangle([(object.rectangle.x, object.rectangle.y + object.rectangle.h),(object.rectangle.x + object.rectangle.w,object.rectangle.y)], fill=None, outline=config.rectcolor, width=config.linewidth)
        txpos = (object.rectangle.x, object.rectangle.y-config.textsize-config.linewidth//2)
        txw,txh = draw.textsize(object.object_property, font=config.font)
        draw.rectangle([txpos, (object.rectangle.x+txw, object.rectangle.y)], outline=config.rectcolor, fill=config.rectcolor, width=config.linewidth)
        draw.text((object.rectangle.x, (object.rectangle.y)-14-4//2),object.object_property, font=config.font, fill=config.textcolor)
    
    st.image(img,caption='Uploaded Image.', use_column_width=True)