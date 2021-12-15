from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
from PIL import ImageFont

rectcolor='green'
linewidth=4
textcolor='white'
textsize=14

subscription_key = '42f6fb25ddea41638ac14d6c948c5431'
endpoint = 'https://20211212test-kengo.cognitiveservices.azure.com/'

#クライアントの認証
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))