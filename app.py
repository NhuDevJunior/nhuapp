from flask import Flask, render_template, request
from keras.preprocessing.image import img_to_array
import tensorflow as tf 
from PIL import Image
import numpy as np
from keras.applications import imagenet_utils
import flask
import io
import cv2
from flask import json,jsonify
import os
import pickle
# initialize our Flask application and the Keras model
app = flask.Flask(__name__)
model = None
def load_model():
    # load the pre-trained Keras model (here we are using a model
    # pre-trained on ImageNet and provided by Keras, but you can
    # substitute in your own networks just as easily)
    app.model = tf.keras.models.load_model('model2.h5')
    # Save the graph to the app framework.
    global model
    model = app.model
def prepare_image(image, target):
    # if the image mode is not RGB, convert it
    if image.mode != "RGB":
        image = image.convert("RGB")

    # resize the input image and preprocess it
    image = image.resize(target)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    #image = imagenet_utils.preprocess_input(image)
    # return the processed image
    return image
@app.route("/predict", methods=["GET","POST"])
def predict():
    if flask.request.method == "POST":
        if flask.request.files.get("image"):
            # read the image in PIL format
            image = flask.request.files["image"].read()
            image = Image.open(io.BytesIO(image))

            # preprocess the image and prepare it for classification
            image = prepare_image(image, target=(96, 96))

            # classify the input image and then initialize the list
            # of predictions to return to the client
            preds = model.predict(image)
            ngoclinh1=str(preds[0][0])
            hanquoc1=str(preds[0][1])
    # return the data dictionary as a JSON response
    return jsonify(
           ngoclinh= ngoclinh1,
           hanquoc= hanquoc1
    )
@app.route('/',methods=["GET","POST"])
def hello():
    return "OK"
if __name__ == "__main__":
    print(("* Loading Keras model and Flask starting server..."
        "please wait until server has fully started"))
    load_model()
    app.run()