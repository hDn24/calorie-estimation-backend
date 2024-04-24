from fastapi import APIRouter, File
from fastapi.responses import JSONResponse

from app.api.cruds import detector as crud
from app.configs import CFG
from app.ml.food_detector import FoodDetector, FoodDetectorOptions

router = APIRouter()

# Load the TFLite model
options = FoodDetectorOptions(
    num_threads=CFG.NUM_THREADS,
    score_threshold=CFG.DETECTION_THRESHOLD,
)
detector = FoodDetector(model_path="app/assets/salad_model.tflite", options=options)


@router.get("/")
def root() -> JSONResponse:
    """Health check api"""
    return JSONResponse({"message": "Health check"})


@router.post("/detect", response_model=dict)
def estimate(files: bytes = File()) -> dict:
    """
    Endpoint for detecting objects in an image.

    Args:
        file: The image file to be processed.

    Returns:
        A dictionary containing the paths of the output images generated after object detection.
    """
    response = crud.detect([files], detector)

    return {"paths": response}
