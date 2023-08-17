import uuid
import os


import cv2
import numpy as np
from flask import Flask, Response, request
from flask_cors import CORS
from PIL import Image
from app.api import detection

from ml.food_detector import FoodDetector, FoodDetectorOptions
from utils import utils

app = Flask(__name__)
CORS(app)

_DETECTION_THRESHOLD = 0.3
_NUM_THREADS = 4

# Load the TFLite model
options = FoodDetectorOptions(
    num_threads=_NUM_THREADS,
    score_threshold=_DETECTION_THRESHOLD,
)
detector = FoodDetector(model_path="./assets/salad_model.tflite", options=options)


@app.route("/")
def root() -> Response:
    """Health check api"""
    response = Response("Health check", mimetype="text/plain")
    return response


@app.route("/detect", methods=["POST"])
def detect() -> dict:
    """Detect api"""
    if "file[]" not in request.files:
        return "Error"
    files = request.files.getlist("file[]")

    response = detection(files, detector)

    return {"paths": response}

    # output_folder = "static"
    # response = []
    # if not os.path.isdir(output_folder):
    #     os.makedirs(output_folder)

    # for file_name in files:
    #     image = Image.open(file_name)
    #     tensor_image = np.asarray(image)

    #     # Run object detection using the model.
    #     detections = detector.detect(tensor_image)

    #     # Draws bounding boxes on the input image
    #     output_image = utils.visualize(tensor_image, detections)

    #     # Convert to RGB
    #     output_image = cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB)

    #     # Save output image
    #     output_image_name = f"{str(uuid.uuid4())}.png"
    #     output_image_path = output_folder + "/" + output_image_name
    #     cv2.imwrite(output_image_path, output_image)

    #     response.append(output_image_path)

    # return {"paths": response}


if __name__ == "__main__":
    # app.run(port=5001, debug=True)
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)