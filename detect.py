import json
import platform
from typing import List, NamedTuple

import cv2
import numpy as np
import tensorflow as tf
from tflite_support import metadata

Interpreter = tf.lite.Interpreter
load_delegate = tf.lite.experimental.load_delegate


class ObjectDetectorOptions(NamedTuple):
    """A config to initialize an object detector."""

    enable_edgetpu: bool = False
    """Enable the model to run on EdgeTPU."""

    label_allow_list: List[str] = None
    """The optional allow list of labels."""

    label_deny_list: List[str] = None
    """The optional deny list of labels."""

    max_results: int = -1
    """The maximum number of top-scored detection results to return."""

    num_threads: int = 1
    """The number of CPU threads to be used."""

    score_threshold: float = 0.0
    """The score threshold of detection results to return."""


class Rect(NamedTuple):
    """A rectangle in 2D space."""

    left: float
    top: float
    right: float
    bottom: float


class Category(NamedTuple):
    """A result of a classification task."""

    label: str
    score: float
    index: int


class Detection(NamedTuple):
    """A detected object as the result of an ObjectDetector."""

    bounding_box: Rect
    categories: List[Category]


def edgetpu_lib_name():
    """Returns the library name of EdgeTPU in the current platform."""
    return {
        "Darwin": "libedgetpu.1.dylib",
        "Linux": "libedgetpu.so.1",
        "Windows": "edgetpu.dll",
    }.get(platform.system(), None)
