from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from PIL import ImageDraw
from PIL import ImageFont

import requests
from array import array
import os
from PIL import Image
import sys
import time
import json
import streamlit as st
import io
import numpy as np

rectcolor='green'
linewidth=4
textcolor='white'
textsize=14
font = ImageFont.truetype("arial.ttf", size=textsize)
    

st.title('顔認識アプリ')

subscription_key = '42f6fb25ddea41638ac14d6c948c5431'
endpoint = 'https://20211212test-kengo.cognitiveservices.azure.com/'

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

uploaded_file = st.file_uploader("choose an image . . . ", type='jpg')
if uploaded_file is not None:
    
    img = Image.open(uploaded_file.name)
    # Open local image file
    local_image = open(uploaded_file.name, "rb")
    
    
    # Open local image file
    
    # Call API with local image
    detect_objects_results_local = computervision_client.detect_objects_in_stream(local_image)

    # Print results of detection with bounding boxes
    print("Detecting objects in local image:")
    if len(detect_objects_results_local.objects) == 0:
        print("No objects detected.")
    else:
        for object in detect_objects_results_local.objects:
            print("'{}'object at location {}, {}, {}, {}".format(object.object_property, \
            object.rectangle.x, object.rectangle.x + object.rectangle.w, \
            object.rectangle.y, object.rectangle.y + object.rectangle.h))
            
    draw = ImageDraw.Draw(img)

    for object in detect_objects_results_local.objects:
        draw.rectangle([(object.rectangle.x, object.rectangle.y + object.rectangle.h),(object.rectangle.x + object.rectangle.w,object.rectangle.y)], fill=None, outline=rectcolor, width=4)
        txpos = (object.rectangle.x, object.rectangle.y-textsize-linewidth//2)
        txw,txh = draw.textsize(object.object_property, font=font)
        draw.rectangle([txpos, (object.rectangle.x+txw, object.rectangle.y)], outline=rectcolor, fill=rectcolor, width=linewidth)
        draw.text((object.rectangle.x, (object.rectangle.y)-14-4//2),object.object_property, font=font, fill=textcolor)
    
    st.image(img,caption='Uploaded Image.', use_column_width=True)