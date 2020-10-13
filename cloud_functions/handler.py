import tensorflow as tf
from flask import jsonify
import numpy as np

model = None

def error_response(msg:str):
  return jsonify((dict(error=msg)))


def handler(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    
    global model

    request_json = request.get_json()

    if request_json and 'image' in request_json:

        if model is None:
            model = tf.keras.applications.inception_v3.InceptionV3()
            
        try:
            image = np.array(request_json['image'])
            image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
            image = tf.keras.applications.inception_v3.preprocess_input(image)
            yhat = model.predict(image)
            labels = tf.keras.applications.inception_v3.decode_predictions(yhat)[0]

            predictions = []

            for label in labels:
                predictions.append([label[1],float(label[2]*100)])

            return jsonify(dict(prediction=predictions))
        
        except Exception as e:
            return error_response(e)
    
    elif request_json:
        return request_json

    return error_response("No image in request")