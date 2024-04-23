import os
import uuid

import cv2
import numpy as np
from PIL import Image

from utils import utils


def detect(files, detector):
    """
    Perform object detection on the input files using the provided detector.

    Args:
        files: A list of file paths to the input images.
        detector: An object representing the detector model.

    Returns:
        A list of paths to the output images generated after object detection.
    """
    output_folder = "static"
    response = []
    if not os.path.isdir(output_folder):
        os.makedirs(output_folder)

    for file_name in files:
        image = Image.open(file_name)
        tensor_image = np.asarray(image)

        # Run object detection using the model.
        detections = detector.detect(tensor_image)

        # Draws bounding boxes on the input image
        output_image = utils.visualize(tensor_image, detections)

        # Convert to RGB
        output_image = cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB)

        # Save output image
        output_image_name = f"{str(uuid.uuid4())}.png"
        output_image_path = output_folder + "/" + output_image_name
        cv2.imwrite(output_image_path, output_image)

        response.append(output_image_path)

    return response
