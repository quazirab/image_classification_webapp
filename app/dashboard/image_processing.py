import base64
import os
from io import BytesIO
from time import time

import dash_html_components as html
import numpy as np
import plotly.graph_objects as go
import requests
from dash import dcc
from PIL import Image

# Variables
HTML_IMG_SRC_PARAMETERS = "data:image/png;base64, "
target_size = (224, 224)
url = os.environ["IMG_CLASS_URL"]
last_runtime_file = "last_runtime.txt"

# Some functions taken from https://github.com/plotly/dash-image-processing/blob/master/dash_reusable_components.py


#  Image utility functions
def pil_to_b64(im, enc_format="png", verbose=False, **kwargs):
    """
    Converts a PIL Image into base64 string for HTML displaying
    :param im: PIL Image object
    :param enc_format: The image format for displaying. If saved the image will have that extension.
    :return: base64 encoding
    """

    buff = BytesIO()
    im.save(buff, format=enc_format, **kwargs)
    encoded = base64.b64encode(buff.getvalue()).decode("utf-8")

    return encoded


def b64_to_pil(string):
    decoded = base64.b64decode(string)
    buffer = BytesIO(decoded)
    im = Image.open(buffer)

    return im


def img_to_list(img):
    img = img.resize(target_size)
    img_list = np.array(img).tolist()
    return img_list


def prediction(img_list):
    r = requests.post(url, json={"image": img_list})
    return r.json()


def DisplayImagePIL(image, **kwargs):
    # encoded_image = pil_to_b64(image, enc_format='png')
    encoded_image = image

    return html.Img(id=f"image", src=HTML_IMG_SRC_PARAMETERS + encoded_image, width="100%", **kwargs)


data = {
    "prediction": [
        ["Siamese_cat", 94.88406181335449],
        ["Egyptian_cat", 3.6008551716804504],
        ["wallaby", 0.7468061055988073],
        ["window_screen", 0.2883706009015441],
        ["tabby", 0.10821686591953039],
    ]
}


def barChart(prediction):
    x = []
    y = []
    for name, confidence in prediction:
        x.append(name)
        y.append(round(confidence, 2))

    fig = go.Figure(
        data=[
            go.Bar(
                x=x,
                y=y,
                text=y,
                textposition="auto",
            )
        ]
    )

    fig.update_layout(
        title=f"Classification Chart",
        yaxis_title="Confidence (%)",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(50,50,50,0)",
        margin=dict(
            l=0,
            r=0,
            b=0,
        ),
    )

    return dcc.Graph(id="graph", figure=fig)


def model_wakeup():
    """
    Very bad idea to store in txt file which can cause error in cocurrent request, but for small project: fingers X
    """
    with open(last_runtime_file, "r") as handler:
        try:
            last_open_time = float(handler.readline())
            if time() - last_open_time > 20 * 60:
                requests.post(url)
        except:
            requests.post(url)
    try:
        with open(last_runtime_file, "w") as handler:
            handler.write(str(time()))
    except:
        pass
