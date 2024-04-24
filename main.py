from fastapi import FastAPI, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.detector import detect
from ml.food_detector import FoodDetector, FoodDetectorOptions

app = FastAPI(title="Calorie estimation")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

_DETECTION_THRESHOLD = 0.3
_NUM_THREADS = 4

# Load the TFLite model
options = FoodDetectorOptions(
    num_threads=_NUM_THREADS,
    score_threshold=_DETECTION_THRESHOLD,
)
detector = FoodDetector(model_path="./assets/salad_model.tflite", options=options)


@app.get("/")
def root() -> JSONResponse:
    """Health check api"""
    return JSONResponse({"message": "Health check"})


@app.post("/detect")
def detection(file: bytes = File()) -> dict:
    """
    Endpoint for detecting objects in an image.

    Args:
        file: The image file to be processed.

    Returns:
        A dictionary containing the paths of the output images generated after object detection.
    """
    response = detect([file], detector)

    return {"paths": response}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
