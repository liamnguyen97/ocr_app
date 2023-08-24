from fastapi import FastAPI, File, UploadFile
from loguru import logger
import easyocr
from io import BytesIO
from PIL import Image
import numpy as np
import imagehash

# Save all files and result to cached
# by a dictionary with key is image hash
cache = {}

app = FastAPI()

@app.post("/ocr")
async def ocr(file: UploadFile = File(...)):
    reader = easyocr.Reader(
        ['vi', 'en'],
        gpu=False,
        detect_network="craft",
        model_storage_directory="./model_storage/model",
        download_enabled=False
    )
    # Read image from route
    request_object_content = await file.read()
    pil_image = Image.open(BytesIO(request_object_content))

    # Get the detection from EasyOCR
    detection = reader.readtext(pil_image)

    # Create the final result
    result = {"bboxes": [], "texts": [], "probs": []}
    for (bbox, text, prob) in detection:
        # Convert a list of NumPy int elements to premitive numbers
        bbox = np.array(bbox).tolist()
        result["bboxes"].append(bbox)
        result["texts"].append(text)
        result["probs"].append(prob)

    return result


@app.post("/cached_ocr")
async def ocr(file: UploadFile = File(...)):
    reader = easyocr.Reader(
        ['vi', 'en'],
        gpu=False,
        detect_network="craft",
        model_storage_directory="./model_storage/model",
        download_enabled=False
    )
    # Read image from route
    request_object_content = await file.read()
    pil_image = Image.open(BytesIO(request_object_content))
    pil_hash = imagehash.average_hash(pil_image)

    if pil_hash in cache:
        logger.info("Getting result from cache!")
        return cache[pil_hash]
    else:
        logger.info("Predicting. Please wait...")
        # Get the detection from EasyOCR
        detection = reader.readtext(pil_image)

        # Create the final result
        result = {"bboxes": [], "texts": [], "probs": []}
        for (bbox, text, prob) in detection:
            # Convert a list of NumPy int elements to premitive numbers
            bbox = np.array(bbox).tolist()
            result["bboxes"].append(bbox)
            result["texts"].append(text)
            result["probs"].append(prob)

        # Save the result to cache
        cache[pil_hash] = result
        
        return result