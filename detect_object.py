from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from PIL import ImageDraw
from PIL import ImageFont
from PIL import Image

import config

def detect_object(file, results, img):
    # Open local image file
    local_image = open(file, "rb")
        
    # Call API with image
    results = config.computervision_client.detect_objects_in_stream(local_image)
    
def rectangle_around_object(results,file,img):
    draw = ImageDraw.Draw(img)
    #検出した物体を矩形で囲む
    for object in results:
        draw.rectangle([(object.rectangle.x, object.rectangle.y + object.rectangle.h),(object.rectangle.x + object.rectangle.w,object.rectangle.y)], fill=None, outline=config.rectcolor, width=config.linewidth)
        txpos = (object.rectangle.x, object.rectangle.y-config.textsize-config.linewidth//2)
        txw,txh = draw.textsize(object.object_property, font=config.font)
        draw.rectangle([txpos, (object.rectangle.x+txw, object.rectangle.y)], outline=config.rectcolor, fill=config.rectcolor, width=config.linewidth)
        draw.text((object.rectangle.x, (object.rectangle.y)-14-4//2),object.object_property, font=config.font, fill=config.textcolor)