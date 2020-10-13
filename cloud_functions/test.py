from PIL import Image

img = Image.open(r"cat.4001.jpg")
target_size=(224, 224)
img = img.resize(target_size) 

# ==============================================
import numpy as np

img_list = np.array(img).tolist()
# ==============================================

import requests

url = 'https://us-central1-helpful-house-292423.cloudfunctions.net/tensorflow_prediction'

json_data = {'image':img_list}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

r = requests.post(url,json=json_data ,headers = headers )

print(r.json())